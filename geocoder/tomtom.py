#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import tomtom_key

class Tomtom(Base):

    provider = 'tomtom'
    api = 'Geocoding API'
    url = 'https://api.tomtom.com/lbs/geocoding/geocode'
    _description = 'The Geocoding API gives developers access to TomTom’s first class geocoding service. \n'
    _description += 'Developers may call this service through either a single or batch geocoding request.\n'
    _description += 'This service supports global coverage, with house number level matching in over 50 countries,\n'
    _description += 'and address point matching where available.'
    _api_reference = ['[{0}](http://developer.tomtom.com/products/geocoding_api)'.format(api)]
    _api_parameter  = [':param ``key``: (optional) use your own API Key from TomTom.']

    def __init__(self, location, key=tomtom_key):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['key'] = key
        self.params['query'] = location
        self.params['format'] = 'json'
        self.params['maxResults'] = 1

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

    @property
    def lat(self):
        return self._get_json_float('geoResult-latitude')

    @property
    def lng(self):
        return self._get_json_float('geoResult-longitude')

    @property
    def address(self):
        return self._get_json_str('geoResult-formattedAddress')

    @property
    def housenumber(self):
        return self._get_json_str('geoResult-houseNumber')

    @property
    def street(self):
        return self._get_json_str('geoResult-street')

    @property
    def quality(self):
        return self._get_json_str('geoResult-type')

    @property
    def postal(self):
        return self._get_json_str('geoResult-postcode')

    @property
    def city(self):
        return self._get_json_str('geoResult-city')

    @property
    def state(self):
        return self._get_json_str('geoResult-state')

    @property
    def country(self):
        return self._get_json_str('geoResult-country')

if __name__ == '__main__':
    g = Tomtom('453 Booth Street, Ottawa')
    g.help()
    g.debug()