#!/usr/bin/python
# coding: utf8

from base import Base
from keys import bing_key
import json
import re


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

    OSM Quality (4/6)
    -----------------
    [ ] addr:housenumber
    [ ] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal
    """
    provider = 'bing'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://dev.virtualearth.net/REST/v1/Locations'
        self.location = location
        self.params = {
            'q': location,
            'o': 'json',
            'key': kwargs.get('key', bing_key),
            'maxResults': 1,
        }
        self._initialize(**kwargs)
        self._bing_catch_errors()

    def _bing_catch_errors(self):
        status = self.parse['statusDescription']
        if not status == 'OK':
            self.error = status

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['resourceSets']:
            self._build_tree(self.parse['resourceSets'][0])

            if self.parse['resources']:
                self._build_tree(self.parse['resources'][0])

                for item in self.parse['geocodePoints']:
                    self._build_tree(item)

    @property
    def lat(self):
        return self.parse['point']['coordinates'][0]

    @property
    def lng(self):
        return self.parse['point']['coordinates'][1]

    @property
    def address(self):
        return self.parse['address']['formattedAddress']

    @property
    def housenumber(self):
        return ''
        if self.street:
            expression = r'\d+'
            pattern = re.compile(expression)
            match = pattern.search(self.street)
            if match:
                return int(match.group(0))

    @property
    def street(self):
        return self.parse['address']['addressLine']

    @property
    def city(self):
        return self.parse['address']['locality']

    @property
    def state(self):
        return self.parse['address']['adminDistrict']

    @property
    def country(self):
        return self.parse['address']['countryRegion']

    @property
    def quality(self):
        return self.parse['entityType']

    @property
    def accuracy(self):
        return self.parse['calculationMethod']

    @property
    def postal(self):
        return self.parse['address']['postalCode']

    @property
    def bbox(self):
        south = self.parse['bbox'][0]
        north = self.parse['bbox'][2]
        west = self.parse['bbox'][1]
        east = self.parse['bbox'][3]
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    #g = Bing('1552 Payette dr, Ottawa ON')
    g = Bing('1552 Payette dr., Ottawa ON')
    g.debug()