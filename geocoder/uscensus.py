#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import re
import logging

from geocoder.base import OneResult, MultipleResultsQuery


class USCensusResult(OneResult):

    @property
    def lat(self):
        if self.raw['coordinates']:
            return self.raw['coordinates'].get('y')

    @property
    def lng(self):
        if self.raw['coordinates']:
            return self.raw['coordinates'].get('x')

    @property
    def address(self):
        if self.raw['matchedAddress']:
            return self.raw.get('matchedAddress')

    @property
    def housenumber(self):
        if self.address:
            match = re.search('^\d+', self.address, re.UNICODE)
            if match:
                return match.group(0)

    @property
    def fromhousenumber(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('fromAddress')

    @property
    def tohousenumber(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('toAddress')

    @property
    def streetname(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('streetName')

    @property
    def prequalifier(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('preQualifier')

    @property
    def predirection(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('preDirection')

    @property
    def pretype(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('preType')

    @property
    def suffixtype(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('suffixType')

    @property
    def suffixdirection(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('suffixDirection')

    @property
    def suffixqualifier(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('suffixQualifier')

    @property
    def city(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('city')

    @property
    def state(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('state')

    @property
    def postal(self):
        if self.raw['addressComponents']:
            return self.raw['addressComponents'].get('zip')


class USCensusQuery(MultipleResultsQuery):
    """
    US Census Geocoder REST Services
    =======================
    The Census Geocoder is an address look-up tool that converts your address to an approximate coordinate (latitude/longitude) and returns information about the address range that includes the address and the census geography the address is within. The geocoder is available as a web interface and as an API (Representational State Transfer - REST - web-based service).

    API Reference
    -------------
    https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html

    """
    provider = 'uscensus'
    method = 'geocode'

    _URL = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress'
    _RESULT_CLASS = USCensusResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'address': location,
            'benchmark': kwargs.get('benchmark', '4'),
            'format': 'json'
        }

    def _adapt_results(self, json_response):
        return json_response['result']['addressMatches']


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = USCensusQuery('4600 Silver Hill Road, Suitland, MD 20746', benchmark=9)
    g.debug()
