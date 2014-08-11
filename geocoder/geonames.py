#!/usr/bin/python
# coding: utf8

from .base import Base


class Geonames(Base):
    provider = 'geonames'
    api = 'GeoNames REST Web Services'
    url = 'http://api.geonames.org/searchJSON'
    _description = 'GeoNames is mainly using REST webservices. Find nearby postal codes / reverse geocoding\n'
    _description += 'This service comes in two flavors.You can either pass the lat/long or a postalcode/placename.\n'
    _api_reference = ['[{0}](http://www.geonames.org/export/web-services.html)'.format(api)]
    _api_parameter = [':param ``username``: (required) needs to be passed with each request.']

    def __init__(self, location, username='addxy'):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['q'] = location
        self.params['fuzzy'] = 0.8
        self.params['maxRows'] = 1
        self.params['username'] = username
        if not username:
            self.help_username()

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

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
    def status_description(self):
        return self._get_json_str('status-message')

    @property
    def quality(self):
        return self._get_json_str('fcodeName')

    @property
    def state(self):
        return self._get_json_str('adminName1')

    @property
    def country(self):
        return self._get_json_str('countryName')

    @property
    def population(self):
        return self._get_json_int('population')

if __name__ =='__main__':
    g = Geonames('Ottawa, Ontario')
    g.help()
    g.debug()
