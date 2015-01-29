#!/usr/bin/python
# coding: utf8

from .base import Base


class Osm(Base):
    """
    Nominatim
    =========
    Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
    and address and to generate synthetic addresses of OSM points (reverse geocoding).

    API Reference
    -------------
    http://wiki.openstreetmap.org/wiki/Nominatim

    OSM Quality (6/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal

    Attributes (20/24)
    ------------------
    [ ] accuracy
    [x] address
    [x] bbox
    [x] city
    [ ] city_district
    [x] confidence
    [x] country
    [ ] county
    [x] housenumber
    [x] lat
    [x] lng
    [x] location
    [x] neighborhood
    [x] ok
    [x] osm_id
    [x] osm_type
    [x] postal
    [x] provider
    [x] quality
    [x] state
    [x] status
    [x] street
    [x] suburb
    [ ] town
    """
    provider = 'osm'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://nominatim.openstreetmap.org/search'
        self.location = location
        self.params = {
            'q': location,
            'format': 'json',
            'addressdetails': 1,
            'limit': 1,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        if self.content:
            self._build_tree(self.content[0])

    @property
    def lat(self):
        return self.parse.get('lat')

    @property
    def lng(self):
        return self.parse.get('lon')

    @property
    def address(self):
        return self.parse.get('display_name')

    @property
    def housenumber(self):
        return self.parse['address'].get('house_number')

    @property
    def street(self):
        return self.parse['address'].get('road')

    @property
    def neighborhood(self):
        neighborhood = self.parse['address'].get('neighbourhood')
        if neighborhood:
            return neighborhood
        elif self.suburb:
            return self.suburb
        elif self.city_district:
            return self.city_district

    @property
    def city_district(self):
        return self.parse['address'].get('city_district')

    @property
    def suburb(self):
        return self.parse['address'].get('suburb')

    @property
    def town(self):
        return self.parse['address'].get('town')

    @property
    def city(self):
        city = self.parse['address'].get('city')
        if city:
            return city
        elif self.town:
            return self.town
        elif self.county:
            return self.county

    @property
    def county(self):
        return self.parse['address'].get('county')

    @property
    def state(self):
        return self.parse['address'].get('state')

    @property
    def country(self):
        return self.parse['address'].get('country')

    @property
    def quality(self):
        return self.parse.get('type')

    @property
    def osm_type(self):
        return self.parse.get('osm_type')

    @property
    def osm_id(self):
        return self.parse.get('osm_id')

    @property
    def postal(self):
        return self.parse['address'].get('postcode')

    @property
    def bbox(self):
        if self.parse['boundingbox']:
            south = float(self.parse['boundingbox'][0])
            west = float(self.parse['boundingbox'][2])
            north = float(self.parse['boundingbox'][1])
            east = float(self.parse['boundingbox'][3])
            return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Osm('1552 Payette dr, Ottawa ON')
    g.debug()