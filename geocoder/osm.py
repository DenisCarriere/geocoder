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
    """
    provider = 'osm'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://nominatim.openstreetmap.org/search'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'q': location,
            'format': 'json',
            'addressdetails': 1,
            'limit': 1,
        }
        self._initialize(**kwargs)

    @property
    def lat(self):
        return self._get_json_float('lat')

    @property
    def lng(self):
        return self._get_json_float('lon')

    @property
    def address(self):
        return self._get_json_str('display_name')

    @property
    def housenumber(self):
        return self._get_json_str('address-house_number')

    @property
    def street(self):
        return self._get_json_str('address-road')

    @property
    def neighborhood(self):
        return self._get_json_str('address-neighbourhood')

    @property
    def suburb(self):
        return self._get_json_str('address-suburb')

    @property
    def town(self):
        return self._get_json_str('address-town')

    @property
    def city(self):
        city = self._get_json_str('address-city')
        if city:
            return city
        elif self.town:
            return self.town

    @property
    def state(self):
        return self._get_json_str('address-state')

    @property
    def country(self):
        country_1 = self._get_json_str('address-country_code')
        country_2 = self._get_json_str('address-country')
        if country_1:
            return country_1.upper()

    @property
    def quality(self):
        return self._get_json_str('type')

    @property
    def osm_type(self):
        return self._get_json_str('osm_type')

    @property
    def osm_id(self):
        return self._get_json_str('osm_id')

    @property
    def postal(self):
        return self._get_json_str('address-postcode')

    @property
    def bbox(self):
        south = self._get_json_float('boundingbox-0')
        west = self._get_json_float('boundingbox-2')
        north = self._get_json_float('boundingbox-1')
        east = self._get_json_float('boundingbox-3')
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Osm('1552 Payette dr, Ottawa ON')
    g.debug()