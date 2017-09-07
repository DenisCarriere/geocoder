#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.location import Location


class IpinfoResult(OneResult):

    @property
    def lat(self):
        loc = self.raw.get('loc')
        if loc:
            return Location(loc).lat

    @property
    def lng(self):
        loc = self.raw.get('loc')
        if loc:
            return Location(loc).lng

    @property
    def address(self):
        if self.city:
            return u'{0}, {1}, {2}'.format(self.city, self.state, self.country)
        elif self.state:
            return u'{0}, {1}'.format(self.state, self.country)
        elif self.country:
            return u'{0}'.format(self.country)
        else:
            return u''

    @property
    def postal(self):
        return self.raw.get('postal')

    @property
    def city(self):
        return self.raw.get('city')

    @property
    def state(self):
        return self.raw.get('region')

    @property
    def country(self):
        return self.raw.get('country')

    @property
    def hostname(self):
        return self.raw.get('hostname')

    @property
    def ip(self):
        return self.raw.get('ip')

    @property
    def org(self):
        return self.raw.get('org')


class IpinfoQuery(MultipleResultsQuery):
    """
    API Reference
    -------------
    https://ipinfo.io
    """
    provider = 'ipinfo'
    method = 'geocode'

    _URL = 'http://ipinfo.io/json'
    _RESULT_CLASS = IpinfoResult
    _KEY_MANDATORY = False

    def _before_initialize(self, location, **kwargs):
        if location.lower() == 'me' or location == '':
            self.url = 'http://ipinfo.io/json'
        else:
            self.url = 'http://ipinfo.io/{0}/json'.format(self.location)

    def _adapt_results(self, json_response):
        return [json_response]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = IpinfoQuery('8.8.8.8')
    g.debug()
