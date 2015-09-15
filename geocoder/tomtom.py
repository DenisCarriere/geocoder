#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import tomtom_key


class Tomtom(Base):
    """
    Geocoding API
    =============
    The Geocoding API gives developers access to TomTom’s first class geocoding service.
    Developers may call this service through either a single or batch geocoding request.
    This service supports global coverage, with house number level matching in over 50 countries,
    and address point matching where available.

    API Reference
    -------------
    http://developer.tomtom.com/products/geocoding_api
    """
    provider = 'tomtom'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://api.tomtom.com/lbs/geocoding/geocode'
        self.location = location
        self.params = {
            'query': location,
            'format': 'json',
            'key': self._get_api_key(tomtom_key, **kwargs),
            'maxResults': 1,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        result = self.parse['geoResponse']['geoResult']
        if result:
            self._build_tree(result[0])

    @property
    def lat(self):
        return self.parse.get('latitude')

    @property
    def lng(self):
        return self.parse.get('longitude')

    @property
    def address(self):
        return self.parse.get('formattedAddress')

    @property
    def housenumber(self):
        return self.parse.get('houseNumber')

    @property
    def street(self):
        return self.parse.get('street')

    @property
    def city(self):
        return self.parse.get('city')

    @property
    def state(self):
        return self.parse.get('state')

    @property
    def country(self):
        return self.parse.get('country')

    @property
    def geohash(self):
        return self.parse.get('geohash')

    @property
    def postal(self):
        return self.parse.get('postcode')

    @property
    def quality(self):
        return self.parse.get('type')

if __name__ == '__main__':
    g = Tomtom('1552 Payette dr., Ottawa')
    g.debug()
