#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import geonames_username


class Geonames(Base):
    """
    GeoNames REST Web Services
    ==========================
    GeoNames is mainly using REST webservices. Find nearby postal codes / reverse geocoding
    This service comes in two flavors.You can either pass the lat/long or a postalcode/placename.

    API Reference
    -------------
    http://www.geonames.org/export/web-services.html

    OSM Quality (3/7)
    -----------------
    [ ] addr:housenumber
    [ ] addr:street
    [ ] addr:city
    [x] addr:state
    [x] addr:country
    [ ] addr:postal
    [x] population
    """
    provider = 'geonames'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.geonames.org/searchJSON'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'q': location,
            'fuzzy': 0.8,
            'username': kwargs.get('username', geonames_username),
            'maxRows': 1,
        }
        self._initialize(**kwargs)
        self._geonames_catch_errors()

    def _geonames_catch_errors(self):
        status = self._get_json_str('status-message')
        count = self._get_json_int('totalResultsCount')
        if status:
            self.error = status
        if count == 0:
            self.error = 'No Results Found'

    @property
    def lat(self):
        return self._get_json_float('lat')

    @property
    def lng(self):
        return self._get_json_float('lng')
    
    @property
    def address(self):
        return self._get_json_str('name')

    @property
    def housenumber(self):
        return ''

    @property
    def street(self):
        return ''

    @property
    def state(self):
        return self._get_json_str('adminName1')

    @property
    def country(self):
        return self._get_json_str('countryName')

    @property
    def quality(self):
        return self._get_json_str('fcodeName')

    @property
    def population(self):
        return self._get_json_int('population')

if __name__ =='__main__':
    g = Geonames('Ottawa, Ontario')
    g.debug()