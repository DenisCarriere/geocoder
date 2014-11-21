#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import app_id, app_code


class Nokia(Base):
    """
    HERE Geocoding REST API
    =======================
    Send a request to the geocode endpoint to find an address 
    using a combination of country, state, county, city, 
    postal code, district, street and house number.

    API Reference
    -------------
    https://developer.here.com/rest-apis/documentation/geocoder

    OSM Quality (6/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal
    """
    provider = 'nokia'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocoder.api.here.com/6.2/geocode.json'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'searchtext': location,
            'app_id': kwargs.get('app_id', app_id),
            'app_code': kwargs.get('app_code', app_code),
            'gen': 4,
        }
        self._initialize(**kwargs)

    @property
    def lat(self):
        return self._get_json_float('NavigationPosition-Latitude')

    @property
    def lng(self):
        return self._get_json_float('NavigationPosition-Longitude')

    @property
    def address(self):
        return self._get_json_str('Address-Label')

    @property
    def postal(self):
        return self._get_json_str('Address-PostalCode')

    @property
    def housenumber(self):
        return self._get_json_str('Address-HouseNumber')

    @property
    def street(self):
        return self._get_json_str('Address-Street')

    @property
    def neighborhood(self):
        return self._get_json_str('Address-District')

    @property
    def city(self):
        return self._get_json_str('Address-City')

    @property
    def county(self):
        return self._get_json_str('Address-County')

    @property
    def state(self):
        state_1 = self._get_json_str('Address-StateName')
        state_2 = self._get_json_str('StateName')
        if state_1:
            return state_1
        elif state_2:
            return state_2 

    @property
    def country(self):
        return self._get_json_str('CountryName')

    @property
    def quality(self):
        return self._get_json_str('Result-MatchLevel')

    @property
    def accuracy(self):
        return self._get_json_str('Result-MatchType')

    @property
    def bbox(self):
        south = self._get_json_float('BottomRight-Latitude')
        north = self._get_json_float('TopLeft-Latitude')
        west = self._get_json_float('TopLeft-Longitude')
        east = self._get_json_float('BottomRight-Longitude')
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Nokia('1552 Payette dr., Ottawa ON')
    g.debug()