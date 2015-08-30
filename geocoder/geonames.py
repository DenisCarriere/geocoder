#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import geonames_username


class Geonames(Base):
    """
    GeoNames REST Web Services
    ==========================
    GeoNames is mainly using REST webservices. Find nearby postal codes / reverse geocoding
    This service comes in two flavors.You can either pass the lat/long or a postalcode/placename.

    API Reference
    -------------
    http://www.geonames.org/export/web-services.html
    """
    provider = 'geonames'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.geonames.org/searchJSON'
        self.location = location
        username = kwargs.get('username', geonames_username)
        if not username:
            raise ValueError('Provide username')
        self.params = {
            'q': location,
            'fuzzy': 0.8,
            'username': username,
            'maxRows': 1,
        }
        self._initialize(**kwargs)

    def _catch_errors(self):
        status = self.parse['status'].get('message')
        value = self.parse['status'].get('value')
        count = self.parse['totalResultsCount']
        if status:
            value_lookup = {10: 'Invalid credentials'}
            self.error = value_lookup[value]
        if count == 0:
            self.error = 'No Results Found'

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['geonames']:
            self._build_tree(self.parse['geonames'][0])

    @property
    def lat(self):
        return self.parse.get('lat')

    @property
    def lng(self):
        return self.parse.get('lng')

    @property
    def address(self):
        return self.parse.get('name')

    @property
    def state(self):
        return self.parse.get('adminName1')

    @property
    def country(self):
        return self.parse.get('countryName')

    @property
    def description(self):
        return self.parse.get('fcodeName')

    @property
    def code(self):
        return self.parse.get('fcode')

    @property
    def geonames_id(self):
        return self.parse.get('geonameId')

    @property
    def population(self):
        return self.parse.get('population')

if __name__ == '__main__':
    g = Geonames('Ottawa, Ontario')
    g.debug()
