#!/usr/bin/python
# coding: utf8

import requests
from .base import Base
from .ratelim import rate_limited


class Google(Base):
    """
    Google Geocoding API
    ====================
    Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway,
    Mountain View, CA") into geographic coordinates (like latitude 37.423021 and
    longitude -122.083739), which you can use to place markers or position the map.

    API Reference
    -------------
    https://developers.google.com/maps/documentation/geocoding/

    OSM Quality (6/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal
    """
    provider = 'google'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.location = location
        self.short_name = kwargs.get('short_name', True)
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'sensor': 'false',
            'address': location,
        }
        self._initialize(**kwargs)
        self._google_catch_errors()

    def _google_catch_errors(self):
        status = self._get_json_str('status')
        if not status == 'OK':
            self.error = status

    @staticmethod
    @rate_limited(2500, 60*60*24)
    @rate_limited(5, 1)
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)

    @property
    def lat(self):
        return self._get_json_float('location-lat')

    @property
    def lng(self):
        return self._get_json_float('location-lng')

    @property
    def quality(self):
        return self._get_json_str('types')

    @property
    def accuracy(self):
        return self._get_json_str('geometry-location_type')

    @property
    def bbox(self):
        south = self._get_json_float('southwest-lat')
        west = self._get_json_float('southwest-lng')
        north = self._get_json_float('northeast-lat')
        east = self._get_json_float('northeast-lng')
        return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self._get_json_str('formatted_address')

    @property
    def postal(self):
        if self.short_name:
            return self._get_json_str('postal_code')
        else:
            return self._get_json_str('postal_code-long_name')

    @property
    def subpremise(self):
        if self.short_name:
            return self._get_json_str('subpremise')
        else:
            return self._get_json_str('subpremise-long_name')

    @property
    def housenumber(self):
        if self.short_name:
            return self._get_json_str('street_number')
        else:
            return self._get_json_str('street_number-long_name')

    @property
    def street(self):
        if self.short_name:
            return self._get_json_str('route')
        else:
            return self._get_json_str('route-long_name')

    @property
    def neighborhood(self):
        if self.short_name:
            return self._get_json_str('neighborhood')
        else:
            return self._get_json_str('neighborhood-long_name')

    @property
    def sublocality(self):
        if self.short_name:
            return self._get_json_str('sublocality')
        else:
            return self._get_json_str('sublocality-long_name')

    @property
    def city(self):
        if self.short_name:
            return self._get_json_str('locality')
        else:
            return self._get_json_str('locality-long_name')

    @property
    def county(self):
        if self.short_name:
            return self._get_json_str('administrative_area_level_2')
        else:
            return self._get_json_str('administrative_area_level_2-long_name')

    @property
    def state(self):
        if self.short_name:
            return self._get_json_str('administrative_area_level_1')
        else:
            return self._get_json_str('administrative_area_level_1-long_name')

    @property
    def country(self):
        if self.short_name:
            return self._get_json_str('country')
        else:
            return self._get_json_str('country-long_name')

if __name__ == '__main__':
    g = Google('1552 Payette dr, Orleans, Ottawa ON')
    g.debug()
