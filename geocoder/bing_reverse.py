#!/usr/bin/python
# coding: utf8

from .base import Base
from .bing import Bing
from .keys import bing_key
from .location import Location


class BingReverse(Bing, Base):
    provider = 'bing'
    api = 'Bing Maps REST Services'
    url = 'http://dev.virtualearth.net/REST/v1/Locations'
    
    _description = 'The Bing™ Maps REST Services Application Programming Interface (API)\n'
    _description += 'provides a Representational State Transfer (REST) interface to\n'
    _description += 'perform tasks such as creating a static map with pushpins, geocoding\n'
    _description += 'an address, retrieving imagery metadata, or creating a route.'
    _api_reference = ['[{0}](http://msdn.microsoft.com/en-us/library/ff701714.aspx)'.format(api)]
    _api_parameter  = [':param ``key``: (optional) use your own API Key from Bing.']

    def __init__(self, location, key=bing_key):
        self.location = location
        g = Location(location)
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['key'] = key
        self.params['o'] = 'json'
        self.url = self.url + '/{0},{1}'.format(g.lat, g.lng)

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = Bing('453 Booth Street, Ottawa ON')
    g.help()
    g.debug()