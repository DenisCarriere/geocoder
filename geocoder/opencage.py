#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.location import BBox
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import opencage_key


class OpenCageResult(OneResult):

    @property
    def lat(self):
        return self.raw['geometry'].get('lat')

    @property
    def lng(self):
        return self.raw['geometry'].get('lng')

    @property
    def address(self):
        return self.raw.get('formatted')

    @property
    def housenumber(self):
        return self.raw['components'].get('house_number')

    @property
    def house_aliases(self):
        house = self.raw['components'].get('house')
        building = self.raw['components'].get('building')
        public_building = self.raw['components'].get('public_building')
        if house:  # Priority can be rearranged
            return house
        elif building:
            return building
        elif public_building:
            return public_building

    @property
    def house(self):
        house = self.raw['components'].get('house')
        if house:
            return house
        else:
            return self.house_aliases

    @property
    def building(self):
        building = self.raw['components'].get('building')
        if building:
            return building
        else:
            return self.house_aliases

    @property
    def public_building(self):
        public_building = self.raw['components'].get('public_building')
        if public_building:
            return public_building
        else:
            return self.house_aliases

    @property
    def street_aliases(self):
        street = self.raw['components'].get('street')
        road = self.raw['components'].get('road')
        footway = self.raw['components'].get('footway')
        street_name = self.raw['components'].get('street_name')
        residential = self.raw['components'].get('residential')
        path = self.raw['components'].get('path')
        pedestrian = self.raw['components'].get('pedestrian')
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
        street = self.raw['components'].get('street')
        if street:
            return street
        else:
            return self.street_aliases

    @property
    def footway(self):
        footway = self.raw['components'].get('footway')
        if footway:
            return footway
        else:
            return self.street_aliases

    @property
    def road(self):
        road = self.raw['components'].get('road')
        if road:
            return road
        else:
            return self.street_aliases

    @property
    def street_name(self):
        street_name = self.raw['components'].get('street_name')
        if street_name:
            return street_name
        else:
            return self.street_aliases

    @property
    def residential(self):
        residential = self.raw['components'].get('residential')
        if residential:
            return residential
        else:
            return self.street_aliases

    @property
    def path(self):
        path = self.raw['components'].get('path')
        if path:
            return path
        else:
            return self.street_aliases

    @property
    def pedestrian(self):
        pedestrian = self.raw['components'].get('pedestrian')
        if pedestrian:
            return pedestrian
        else:
            return self.street_aliases

    @property
    def neighbourhood_aliases(self):
        neighbourhood = self.raw['components'].get('neighbourhood')
        suburb = self.raw['components'].get('suburb')
        city_district = self.raw['components'].get('city_district')
        if neighbourhood:  # Priority can be rearranged
            return neighbourhood
        elif suburb:
            return suburb
        elif city_district:
            return city_district

    @property
    def neighbourhood(self):
        neighbourhood = self.raw['components'].get('neighbourhood')
        if neighbourhood:
            return neighbourhood
        else:
            return self.neighbourhood_aliases

    @property
    def suburb(self):
        suburb = self.raw['components'].get('suburb')
        if suburb:
            return suburb
        else:
            return self.neighbourhood_aliases

    @property
    def city_district(self):
        city_district = self.raw['components'].get('city_district')
        if city_district:
            return city_district
        else:
            return self.neighbourhood_aliases

    @property
    def city_aliases(self):
        city = self.raw['components'].get('city')
        town = self.raw['components'].get('town')
        if city:  # Priority can be rearranged
            return city
        elif town:
            return town
        else:  # if nothing in city_aliases, then return village aliases
            return self.village_aliases

    @property
    def city(self):
        city = self.raw['components'].get('city')
        if city:
            return city
        else:
            return self.city_aliases

    @property
    def town(self):
        town = self.raw['components'].get('town')
        if town:
            return town
        else:
            return self.city_aliases

    @property
    def county(self):
        return self.raw['components'].get('county')

    @property
    def village_aliases(self):
        village = self.raw['components'].get('village')
        hamlet = self.raw['components'].get('hamlet')
        locality = self.raw['components'].get('locality')

        if village:  # Priority can be rearranged
            return village
        elif hamlet:
            return hamlet
        elif locality:
            return locality

    @property
    def village(self):
        village = self.raw['components'].get('village')
        if village:
            return village
        else:
            return self.village_aliases

    @property
    def hamlet(self):
        hamlet = self.raw['components'].get('hamlet')
        if hamlet:
            return hamlet
        else:
            return self.village_aliases

    @property
    def locality(self):
        locality = self.raw['components'].get('locality')
        if locality:
            return locality
        else:
            return self.village_aliases

    @property
    def state_aliases(self):
        state = self.raw['components'].get('state')
        province = self.raw['components'].get('province')
        state_code = self.raw['components'].get('state_code')

        if state:  # Priority can be rearranged
            return state
        elif province:
            return province
        elif state_code:
            return state_code

    @property
    def state(self):
        state = self.raw['components'].get('state')
        if state:
            return state
        else:
            return self.state_aliases

    @property
    def province(self):
        province = self.raw['components'].get('province')
        if province:
            return province
        else:
            return self.state_aliases

    @property
    def state_code(self):
        state_code = self.raw['components'].get('state_code')
        if state_code:
            return state_code
        else:
            return self.state_aliases

    @property
    def state_district(self):
        return self.raw['components'].get('state_district')

    @property
    def country(self):
        country = self.raw['components'].get('country')
        if country:
            return country
        else:
            return self.raw['components'].get('country_name')

    @property
    def country_code(self):
        return self.raw['components'].get('country_code')

    @property
    def postal(self):
        return self.raw['components'].get('postcode')

    @property
    def postcode(self):
        return self.raw['components'].get('postcode')

    @property
    def continent(self):
        return self.raw['components'].get('continent')

    @property
    def island(self):
        return self.raw['components'].get('island')

    @property
    def region(self):
        return self.raw['components'].get('region')

    @property
    def confidence(self):
        return self.raw.get('confidence')

    @property
    def w3w(self):
        return self.raw['annotations'].get('what3words', {}).get('words')

    @property
    def mgrs(self):
        return self.raw['annotations'].get('MGRS')

    @property
    def geohash(self):
        return self.raw['annotations'].get('geohash')

    @property
    def callingcode(self):
        return self.raw['annotations'].get('callingcode')

    @property
    def Maidenhead(self):
        return self.raw['annotations'].get('Maidenhead')

    @property
    def DMS(self):
        return self.raw['annotations'].get('DMS')

    @property
    def Mercator(self):
        return self.raw['annotations'].get('Mercator')

    @property
    def bbox(self):
        south = self.raw['bounds']['southwest'].get('lat')
        north = self.raw['bounds']['northeast'].get('lat')
        west = self.raw['bounds']['southwest'].get('lng')
        east = self.raw['bounds']['northeast'].get('lng')
        return BBox.factory([south, west, north, east]).as_dict


class OpenCageQuery(MultipleResultsQuery):
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

    _URL = 'http://api.opencagedata.com/geocode/v1/json'
    _RESULT_CLASS = OpenCageResult
    _KEY = opencage_key

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'query': location,
            'key': provider_key,
            'limit': kwargs.get('maxRows', 1)
        }

    def _catch_errors(self, json_response):
        status = json_response.get('status')
        if status and status.get('code') != 200:
            self.status_code = status.get('code')
            self.error = status.get('message')

        return self.error

    def _adapt_results(self, json_response):
        # special license attribute
        self.license = json_response['licenses']
        # return geo results
        return json_response['results']


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = OpenCageQuery('1552 Payette dr., Ottawa')
    g.debug()
