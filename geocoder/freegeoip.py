#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging
import requests
import ratelim

from geocoder.base import OneResult, MultipleResultsQuery


class FreeGeoIPResult(OneResult):

    @property
    def lat(self):
        return self.raw.get('latitude')

    @property
    def lng(self):
        return self.raw.get('longitude')

    @property
    def address(self):
        if self.city:
            return u'{0}, {1} {2}'.format(self.city, self.state, self.country)
        elif self.state:
            return u'{0}, {1}'.format(self.state, self.country)
        elif self.country:
            return u'{0}'.format(self.country)
        return u''

    @property
    def postal(self):
        zip_code = self.raw.get('zip_code')
        postal_code = self.raw.get('postal_code')
        if zip_code:
            return zip_code
        if postal_code:
            return postal_code

    @property
    def city(self):
        return self.raw.get('city')

    @property
    def state(self):
        return self.raw.get('region')

    @property
    def region_code(self):
        return self.raw.get('region_code')

    @property
    def country(self):
        return self.raw.get('country_name')

    @property
    def country_code3(self):
        return self.raw.get('country_code3')

    @property
    def continent(self):
        return self.raw.get('continent')

    @property
    def timezone(self):
        return self.raw.get('timezone')

    @property
    def area_code(self):
        return self.raw.get('area_code')

    @property
    def dma_code(self):
        return self.raw.get('dma_code')

    @property
    def offset(self):
        return self.raw.get('offset')

    @property
    def organization(self):
        return self.raw.get('organization')

    @property
    def ip(self):
        return self.raw.get('ip')

    @property
    def time_zone(self):
        return self.raw.get('time_zone')


class FreeGeoIPQuery(MultipleResultsQuery):
    """
    FreeGeoIP.net
    =============
    freegeoip.net provides a public HTTP API for software developers to
    search the geolocation of IP addresses. It uses a database of IP addresses
    that are associated to cities along with other relevant information like
    time zone, latitude and longitude.

    You're allowed up to 10,000 queries per hour by default. Once this
    limit is reached, all of your requests will result in HTTP 403,
    forbidden, until your quota is cleared.

    API Reference
    -------------
    http://freegeoip.net/
    """
    provider = 'freegeoip'
    method = 'geocode'

    _URL = 'https://freegeoip.net/json/'
    _RESULT_CLASS = FreeGeoIPResult
    _KEY_MANDATORY = False

    def _before_initialize(self, location, **kwargs):
        self.url += location

    @staticmethod
    @ratelim.greedy(10000, 60 * 60)
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)

    def _adapt_results(self, json_response):
        return [json_response]

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = FreeGeoIPQuery('99.240.181.199')
    g.debug()
