#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import bing_key


class Bing(Base):
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
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://dev.virtualearth.net/REST/v1/Locations'
        self.location = location
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
        
    def _initialize(self, **kwargs):
        self._connect(url=self.url, params=self.params, **kwargs)
        self._parse(self.content)
        self._json()
        self.bbox

        # Bing catch errors
        status = self._get_json_str('statusDescription')
        if not status == 'OK':
            self.error = status

    @property
    def lat(self):
        return self._get_json_float('coordinates-0')

    @property
    def lng(self):
        return self._get_json_float('coordinates-1')

    @property
    def housenumber(self):
        return ''

    @property
    def street(self):
        return self._get_json_str('address-addressLine')

    @property
    def address(self):
        return self._get_json_str('address-formattedAddress')

    @property
    def quality(self):
        return self._get_json_str('resources-entityType')

    @property
    def accuracy(self):
        return self._get_json_str('geocodePoints-calculationMethod')

    @property
    def postal(self):
        return self._get_json_str('address-postalCode')

    @property
    def bbox(self):
        south = self._get_json_float('bbox-0')
        north = self._get_json_float('bbox-2')
        west = self._get_json_float('bbox-1')
        east = self._get_json_float('bbox-3')
        return self._get_bbox(south, west, north, east)

    @property
    def city(self):
        return self._get_json_str('address-locality')

    @property
    def state(self):
        return self._get_json_str('address-adminDistrict')

    @property
    def country(self):
        return self._get_json_str('address-countryRegion')

if __name__ == '__main__':
    g = Bing('453 Booth Street, Ottawa ON')
    g.help()
    g.debug()