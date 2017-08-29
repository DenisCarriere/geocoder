#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import opencage_key


class OpenCage(Base):
    """
    OpenCage Geocoding Services
    ===========================
    OpenCage Geocoder simple, easy, and open geocoding for the entire world
    Our API combines multiple geocoding systems in the background.
    Each is optimized for different parts of the world and types of requests.
    We aggregate the best results from open data sources and algorithms so you don't have to.
    Each is optimized for different parts of the world and types of requests.

    API Reference
    -------------
    https://geocoder.opencagedata.com/api
    """
    provider = 'opencage'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.opencagedata.com/geocode/v1/json'
        self.location = location
        self.params = {
            'query': location,
            'key': self._get_api_key(opencage_key, **kwargs),
        }
        self._initialize(**kwargs)

    def _catch_errors(self):
        if self.content:
            status = self.content.get('status')
            if status:
                self.status_code = status.get('code')
                message = status.get('message')
                if self.status_code:
                    self.error = message

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])
        licenses = self.parse['licenses']
        if licenses:
            self.parse['licenses'] = licenses[0]

    @property
    def lat(self):
        return self.parse['geometry'].get('lat')

    @property
    def lng(self):
        return self.parse['geometry'].get('lng')

    @property
    def address(self):
        return self.parse.get('formatted')

    @property
    def housenumber(self):
        return self.parse['components'].get('house_number')

    @property
    def house_aliases(self):
        house = self.parse['components'].get('house')
        building = self.parse['components'].get('building')
        public_building = self.parse['components'].get('public_building')
        if house:  # Priority can be rearranged
            return house
        elif building:
            return building
        elif public_building:
            return public_building

    @property
    def house(self):
        house = self.parse['components'].get('house')
        if house:
            return house
        else:
            return self.house_aliases

    @property
    def building(self):
        building = self.parse['components'].get('building')
        if building:
            return building
        else:
            return self.house_aliases

    @property
    def public_building(self):
        public_building = self.parse['components'].get('public_building')
        if public_building:
            return public_building
        else:
            return self.house_aliases

    @property
    def street_aliases(self):
        street = self.parse['components'].get('street')
        road = self.parse['components'].get('road')
        footway = self.parse['components'].get('footway')
        street_name = self.parse['components'].get('street_name')
        residential = self.parse['components'].get('residential')
        path = self.parse['components'].get('path')
        pedestrian = self.parse['components'].get('pedestrian')
        if street:
            return street
        elif road:
            return road
        elif footway:
            return footway
        elif street_name:
            return street_name
        elif residential:
            return residential
        elif path:
            return path
        elif pedestrian:
            return pedestrian

    @property
    def street(self):
        street = self.parse['components'].get('street')
        if street:
            return street
        else:
            return self.street_aliases

    @property
    def footway(self):
        footway = self.parse['components'].get('footway')
        if footway:
            return footway
        else:
            return self.street_aliases

    @property
    def road(self):
        road = self.parse['components'].get('road')
        if road:
            return road
        else:
            return self.street_aliases

    @property
    def street_name(self):
        street_name = self.parse['components'].get('street_name')
        if street_name:
            return street_name
        else:
            return self.street_aliases

    @property
    def residential(self):
        residential = self.parse['components'].get('residential')
        if residential:
            return residential
        else:
            return self.street_aliases

    @property
    def path(self):
        path = self.parse['components'].get('path')
        if path:
            return path
        else:
            return self.street_aliases

    @property
    def pedestrian(self):
        pedestrian = self.parse['components'].get('pedestrian')
        if pedestrian:
            return pedestrian
        else:
            return self.street_aliases

    @property
    def neighbourhood_aliases(self):
        neighbourhood = self.parse['components'].get('neighbourhood')
        suburb = self.parse['components'].get('suburb')
        city_district = self.parse['components'].get('city_district')
        if neighbourhood:  # Priority can be rearranged
            return neighbourhood
        elif suburb:
            return suburb
        elif city_district:
            return city_district

    @property
    def neighbourhood(self):
        neighbourhood = self.parse['components'].get('neighbourhood')
        if neighbourhood:
            return neighbourhood
        else:
            return self.neighbourhood_aliases

    @property
    def suburb(self):
        suburb = self.parse['components'].get('suburb')
        if suburb:
            return suburb
        else:
            return self.neighbourhood_aliases

    @property
    def city_district(self):
        city_district = self.parse['components'].get('city_district')
        if city_district:
            return city_district
        else:
            return self.neighbourhood_aliases

    @property
    def city_aliases(self):
        city = self.parse['components'].get('city')
        town = self.parse['components'].get('town')
        if city:  # Priority can be rearranged
            return city
        elif town:
            return town
        else:  # if nothing in city_aliases, then return village aliases
            return self.village_aliases

    @property
    def city(self):
        city = self.parse['components'].get('city')
        if city:
            return city
        else:
            return self.city_aliases

    @property
    def town(self):
        town = self.parse['components'].get('town')
        if town:
            return town
        else:
            return self.city_aliases

    @property
    def county(self):
        return self.parse['components'].get('county')

    @property
    def village_aliases(self):
        village = self.parse['components'].get('village')
        hamlet = self.parse['components'].get('hamlet')
        locality = self.parse['components'].get('locality')

        if village:  # Priority can be rearranged
            return village
        elif hamlet:
            return hamlet
        elif locality:
            return locality

    @property
    def village(self):
        village = self.parse['components'].get('village')
        if village:
            return village
        else:
            return self.village_aliases

    @property
    def hamlet(self):
        hamlet = self.parse['components'].get('hamlet')
        if hamlet:
            return hamlet
        else:
            return self.village_aliases

    @property
    def locality(self):
        locality = self.parse['components'].get('locality')
        if locality:
            return locality
        else:
            return self.village_aliases

    @property
    def state_aliases(self):
        state = self.parse['components'].get('state')
        province = self.parse['components'].get('province')
        state_code = self.parse['components'].get('state_code')

        if state:  # Priority can be rearranged
            return state
        elif province:
            return province
        elif state_code:
            return state_code

    @property
    def state(self):
        state = self.parse['components'].get('state')
        if state:
            return state
        else:
            return self.state_aliases

    @property
    def province(self):
        province = self.parse['components'].get('province')
        if province:
            return province
        else:
            return self.state_aliases

    @property
    def state_code(self):
        state_code = self.parse['components'].get('state_code')
        if state_code:
            return state_code
        else:
            return self.state_aliases

    @property
    def state_district(self):
        return self.parse['components'].get('state_district')

    @property
    def country(self):
        country = self.parse['components'].get('country')
        if country:
            return country
        else:
            return self.parse['components'].get('country_name')

    @property
    def country_code(self):
        return self.parse['components'].get('country_code')

    @property
    def postal(self):
        return self.parse['components'].get('postcode')

    @property
    def postcode(self):
        return self.parse['components'].get('postcode')

    @property
    def continent(self):
        return self.parse['components'].get('continent')

    @property
    def island(self):
        return self.parse['components'].get('island')

    @property
    def region(self):
        return self.parse['components'].get('region')

    @property
    def confidence(self):
        return self.parse.get('confidence')

    @property
    def w3w(self):
        return self.parse['what3words'].get('words')

    @property
    def mgrs(self):
        return self.parse['annotations'].get('MGRS')

    @property
    def geohash(self):
        return self.parse['annotations'].get('geohash')

    @property
    def callingcode(self):
        return self.parse['annotations'].get('callingcode')

    @property
    def Maidenhead(self):
        return self.parse['annotations'].get('Maidenhead')

    @property
    def DMS(self):
        return self.parse.get('DMS')

    @property
    def Mercator(self):
        return self.parse.get('Mercator')

    @property
    def license(self):
        return self.parse.get('licenses')

    @property
    def bbox(self):
        south = self.parse['southwest'].get('lat')
        north = self.parse['northeast'].get('lat')
        west = self.parse['southwest'].get('lng')
        east = self.parse['northeast'].get('lng')
        return self._get_bbox(south, west, north, east)


if __name__ == '__main__':
    g = OpenCage('1552 Payette dr., Ottawa')
    print(g.json['mgrs'])
