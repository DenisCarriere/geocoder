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
        self.url = 'http://dev.virtualearth.net/REST/v1/Locations'
        self.url += '/{0},{1}'.format(Location(location).lat, Location(location).lng)
        self.location = Location(location).latlng
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'q': location,
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
    g = Bing('453 Booth Street, Ottawa ON')
    g.help()
    g.debug()