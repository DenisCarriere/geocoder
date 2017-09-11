#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery


class YahooResult(OneResult):

    @property
    def lat(self):
        return self.raw.get('latitude')

    @property
    def lng(self):
        return self.raw.get('longitude')

    @property
    def address(self):
        line1 = self.raw.get('line1')
        line2 = self.raw.get('line2')
        if line1:
            return ', '.join([line1, line2])
        else:
            return line2

    @property
    def housenumber(self):
        return self.raw.get('house')

    @property
    def street(self):
        return self.raw.get('street')

    @property
    def neighborhood(self):
        return self.raw.get('neighborhood')

    @property
    def city(self):
        return self.raw.get('city')

    @property
    def county(self):
        return self.raw.get('county')

    @property
    def state(self):
        return self.raw.get('state')

    @property
    def country(self):
        return self.raw.get('country')

    @property
    def hash(self):
        return self.raw.get('hash')

    @property
    def quality(self):
        return self.raw.get('addressMatchType')

    @property
    def postal(self):
        postal = self.raw.get('postal')
        if postal:
            return postal
        else:
            return self.raw.get('uzip')


class YahooQuery(MultipleResultsQuery):
    """
    Yahoo BOSS Geo Services
    =======================
    Yahoo PlaceFinder is a geocoding Web service that helps developers make
    their applications location-aware by converting street addresses or
    place names into geographic coordinates (and vice versa).

    API Reference
    -------------
    https://developer.yahoo.com/boss/geo/
    """
    provider = 'yahoo'
    method = 'geocode'

    _URL = 'https://sgws2.maps.yahoo.com/FindLocation'
    _RESULT_CLASS = YahooResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        return{
            'q': location,
            'flags': 'J',
            'locale': kwargs.get('locale', 'en-CA'),
        }

    def _catch_errors(self, json_response):
        status = json_response['statusDescription']
        if status:
            if not status == 'OK':
                self.error = status

        return self.error

    def _adapt_results(self, json_response):
        return [json_response['Result']]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = YahooQuery('1552 Payette dr., Ottawa, ON')
    g.debug()
