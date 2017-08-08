#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.bing import BingResult, BingQuery
from geocoder.location import Location


class BingReverseResult(BingResult):

    @property
    def ok(self):
        return bool(self.address)


class BingReverse(BingQuery):
    """
    Bing Maps REST Services
    =======================
    The Bing™ Maps REST Services Application Programming Interface (API)
    provides a Representational State Transfer (REST) interface to
    perform tasks such as creating a static map with pushpins, geocoding
    an address, retrieving imagery metadata, or creating a route.

    API Reference
    -------------
    http://msdn.microsoft.com/en-us/library/ff701714.aspx

    """
    provider = 'bing'
    method = 'reverse'

    _URL = u'http://dev.virtualearth.net/REST/v1/Locations/{0}'

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'o': 'json',
            'key': provider_key,
            'maxResults': 1,
        }

    def _before_initialize(self, location, **kwargs):
        self.url = self.url.format(str(Location(location)))


if __name__ == '__main__':
    g = BingReverse([45.4049053, -75.7077965], key=None)
    g.debug()
