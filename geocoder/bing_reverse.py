#!/usr/bin/python
# coding: utf8

from .base import Base
from .bing import Bing
from .keys import bing_key
from .location import Location


class BingReverse(Bing, Base):
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
        location = Location(location)
        self.url = 'http://dev.virtualearth.net/REST/v1/Locations'
        self.url += '/{0},{1}'.format(location.lat, location.lng)
        self.location = location.latlng
        self.params = {
            'o': 'json',
            'key': kwargs.get('key', bing_key),
            'maxResults': 1,
        }
        self._initialize(**kwargs)
        self._bing_catch_errors()

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = BingReverse([45.4049053, -75.7077965])
    g.debug()
