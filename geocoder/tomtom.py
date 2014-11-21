#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import tomtom_key

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

    OSM Quality (5/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [ ] addr:postal
    """
    provider = 'tomtom'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://api.tomtom.com/lbs/geocoding/geocode'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'query': location,
            'format': 'json',
            'key': kwargs.get('key', tomtom_key),
            'maxResults': 1,
        }
        self._initialize(**kwargs)

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
    def city(self):
        return self._get_json_str('geoResult-city')

    @property
    def state(self):
        return self._get_json_str('geoResult-state')

    @property
    def country(self):
        return self._get_json_str('geoResult-country')

    @property
    def geohash(self):
        return self._get_json_str('geoResult-geohash')

    @property
    def postal(self):
        return self._get_json_str('geoResult-postcode')

    @property
    def quality(self):
        return self._get_json_str('geoResult-type')

if __name__ == '__main__':
    g = Tomtom('1552 Payette dr., Ottawa')
    g.debug()