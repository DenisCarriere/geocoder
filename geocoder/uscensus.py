#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
import re


class USCensus(Base):
    """
    US Census Geocoder REST Services
    =======================
    The Census Geocoder is an address look-up tool that converts your address to an approximate coordinate (latitude/longitude) and returns information about the address range that includes the address and the census geography the address is within. The geocoder is available as a web interface and as an API (Representational State Transfer - REST - web-based service).

    API Reference
    -------------
    https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.pdf

    """
    provider = 'uscensus'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress'
        self.location = location
        self.params = {
            'address': location,
            'benchmark': kwargs.get('benchmark', '4'),
            'format': 'json'
        }

        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        sets = self.parse['result']['addressMatches']
        if sets:
            resources = sets[0]
            if resources:
                self._build_tree(resources)

    @property
    def lat(self):
        if self.parse['coordinates']:
            return self.parse['coordinates'].get('y')

    @property
    def lng(self):
        if self.parse['coordinates']:
            return self.parse['coordinates'].get('x')

    @property
    def address(self):
        if self.parse['matchedAddress']:
            return self.parse.get('matchedAddress')

    @property
    def housenumber(self):
        if self.address:
            match = re.search('^\d+', self.address, re.UNICODE)
            if match:
                return match.group(0)

    @property
    def fromhousenumber(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('fromAddress')

    @property
    def tohousenumber(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('toAddress')

    @property
    def streetname(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('streetName')

    @property
    def prequalifier(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('preQualifier')

    @property
    def predirection(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('preDirection')

    @property
    def pretype(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('preType')

    @property
    def suffixtype(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('suffixType')

    @property
    def suffixdirection(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('suffixDirection')

    @property
    def suffixqualifier(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('suffixQualifier')

    @property
    def city(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('city')

    @property
    def state(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('state')

    @property
    def postal(self):
        if self.parse['addressComponents']:
            return self.parse['addressComponents'].get('zip')

if __name__ == '__main__':
    g = USCensus('4600 Silver Hill Road, Suitland, MD 20746', benchmark=9)
    g.debug()
