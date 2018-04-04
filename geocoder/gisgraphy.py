#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery


class GisgraphyResult(OneResult):

    @property
    def lat(self):
        return self.raw.get('lat')

    @property
    def lng(self):
        return self.raw.get('lng')

    @property
    def address(self):
        return self.raw.get('formatedFull', '')

    @property
    def country(self):
        return self.raw.get('countryCode', '')

    @property
    def state(self):
        return self.raw.get('state', '')

    @property
    def city(self):
        return self.raw.get('city', '')

    @property
    def street(self):
        return self.raw.get('streetName', '')

    @property
    def housenumber(self):
        return self.raw.get('houseNumber', '')

    @property
    def postal(self):
        return self.raw.get('zipCode', '')


class GisgraphyQuery(MultipleResultsQuery):
    """
    Gisgraphy REST API
    =======================

    API Reference
    -------------
    http://www.gisgraphy.com/documentation/user-guide.php
    """
    provider = 'gisgraphy'
    method = 'geocode'

    _URL = 'https://services.gisgraphy.com/geocoding/'
    _RESULT_CLASS = GisgraphyResult
    _KEY_MANDATORY = False
    
    def _build_headers(self, provider_key, **kwargs):
        return {
            'Referer': "https://services.gisgraphy.com",
            'User-agent': 'geocoder-converter'
        }

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'address': location,
            'limitnbresult': kwargs.get('maxRows', 1),
            'format': 'json',
        }

    def _adapt_results(self, json_response):
        return json_response['result']

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = GisgraphyQuery('Ottawa Ontario', maxRows=3)
    g.debug()
