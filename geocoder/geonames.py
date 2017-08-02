#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import json

from geocoder.base import MultipleResultsQuery, OneResult
from geocoder.keys import geonames_username


class GeonamesResult(OneResult):

    @property
    def lat(self):
        return self.raw.get('lat')

    @property
    def lng(self):
        return self.raw.get('lng')

    @property
    def geonames_id(self):
        return self.raw.get('geonameId')

    @property
    def address(self):
        return self.raw.get('name')

    @property
    def feature_class(self):
        return self.raw.get('fcl')

    @property
    def class_description(self):
        return self.raw.get('fclName')

    @property
    def code(self):
        return self.raw.get('fcode')

    @property
    def description(self):
        return self.raw.get('fcodeName')

    @property
    def state(self):
        return self.raw.get('adminName1')

    @property
    def state_code(self):
        return self.raw.get('adminCode1')

    @property
    def country(self):
        return self.raw.get('countryName')

    @property
    def country_code(self):
        return self.raw.get('countryCode')

    @property
    def population(self):
        return self.raw.get('population')


class GeonamesQuery(MultipleResultsQuery):
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

    _URL = 'http://api.geonames.org/searchJSON'
    _RESULT_CLASS = GeonamesResult

    def __init__(self, location, **kwargs):
        super(GeonamesQuery, self).__init__(location, **kwargs)

        # check username (key)
        username = kwargs.pop('username', geonames_username)
        if not username:
            raise ValueError('Provide username')

        # prepare params for query
        self.params = self._build_params(location, username, **kwargs)

        # query and parse results
        self._initialize()

    def _build_params(self, location, username, **kwargs):
        """Will be overridden according to the targetted web service"""
        return {
            'q': location,
            'fuzzy': kwargs.get('fuzzy', 0.8),
            'username': username,
            'maxRows': kwargs.get('maxRows', 1),
        }

    def _catch_errors(self, json_response):
        """ Changed: removed check on number of elements:
            - totalResultsCount not sytem^atically returned (e.g in hierarchy)
            - done in base.py
        """
        status = json_response.get('status')
        if status:
            message = status.get('message')
            value = status.get('value')
            custom_messages = {
                10: 'Invalid credentials',
                18: 'Do not use the demo account for your application',
            }
            self.error = custom_messages.get(value, message)

        return self.error

    def _adapt_results(self, json_content):
        # extract the array of JSON objects
        return json_content['geonames']


if __name__ == '__main__':
    g = GeonamesQuery('Ottawa, Ontario', maxRows=1)
    print(json.dumps(g.geojson, indent=4))
    # g.debug()
