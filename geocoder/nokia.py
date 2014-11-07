#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import app_id, app_code


class Nokia(Base):
    provider = 'nokia'
    api = 'HERE Geocoding REST API'
    url = 'http://geocoder.api.here.com/6.2/geocode.json'
    _description = 'Send a request to the geocode endpoint to find an address using a combination of\n'
    _description += 'country, state, county, city, postal code, district, street and house number.'
    _api_reference = ['[{0}](https://developer.here.com/rest-apis/documentation/geocoder)'.format(api)]
    _api_parameter  = [':param app_id: (optional) use your own Application ID from Nokia.']
    _api_parameter  = [':param app_code: (optional) use your own Application Code from Nokia.']

    def __init__(self, location, app_id=app_id, app_code=app_code):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['searchtext'] = location
        self.params['app_id'] = app_id
        self.params['app_code'] = app_code
        self.params['gen'] = 4

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()
        self.bbox

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
    def housenumber(self):
        return self._get_json_str('Address-HouseNumber')

    @property
    def route(self):
        return self._get_json_str('Address-Street')

    @property
    def quality(self):
        return self._get_json_str('Result-MatchLevel')

    @property
    def accuracy(self):
        return self._get_json_str('Result-MatchType')

    @property
    def postal(self):
        return self._get_json_str('Address-PostalCode')

    @property
    def bbox(self):
        south = self._get_json_float('BottomRight-Latitude')
        north = self._get_json_float('TopLeft-Latitude')
        west = self._get_json_float('TopLeft-Longitude')
        east = self._get_json_float('BottomRight-Longitude')
        return self._get_bbox(south, west, north, east)

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
        return self._get_json_str('Address-StateName')

    @property
    def country(self):
        return self._get_json_str('CountryName')

if __name__ == '__main__':
    g = Nokia('Kingston Ontario')
    g.help()
    g.debug()