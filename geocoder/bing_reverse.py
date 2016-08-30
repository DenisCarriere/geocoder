#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.bing import Bing
from geocoder.keys import bing_key
from geocoder.location import Location


class BingReverse(Bing):
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

    def __init__(self, location, **kwargs):
        self.location = str(Location(location))
        self.url = u'http://dev.virtualearth.net/' \
                   'REST/v1/Locations/{0}'.format(self.location)
        self.params = {
            'o': 'json',
            'key': self._get_api_key(bing_key, **kwargs),
            'maxResults': 1,
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = BingReverse([45.4049053, -75.7077965], key=None)
    g.debug()
