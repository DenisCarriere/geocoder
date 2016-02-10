#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import bing_key
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

    Get Bing key
    ------------
    https://www.bingmapsportal.com/
    """
    provider = 'bing'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://dev.virtualearth.net/REST/v1/Locations'
        self.location = location
        self.headers = {
            'Referer': "http://addxy.com/",
            'User-agent': 'Mozilla/5.0'
        }
        self.params = {
            'q': location,
            'o': 'json',
            'inclnb': 1,
            'key': self._get_api_key(bing_key, **kwargs),
            'maxResults': 1
        }

        self._initialize(**kwargs)

    def _catch_errors(self):
        status = self.parse['statusDescription']
        if not status == 'OK':
            self.error = status

    def _exceptions(self):
        # Build intial Tree with results
        sets = self.parse['resourceSets']
        if sets:
            resources = sets[0]['resources']
            if resources:
                self._build_tree(resources[0])

            for item in self.parse['geocodePoints']:
                self._build_tree(item)

    @property
    def lat(self):
        coord = self.parse['point']['coordinates']
        if coord:
            return coord[0]

    @property
    def lng(self):
        coord = self.parse['point']['coordinates']
        if coord:
            return coord[1]

    @property
    def address(self):
        return self.parse['address'].get('formattedAddress')

    @property
    def housenumber(self):
        if self.street:
            expression = r'\d+'
            pattern = re.compile(expression)
            match = pattern.search(self.street, re.UNICODE)
            if match:
                return match.group(0)

    @property
    def street(self):
        return self.parse['address'].get('addressLine')

    @property
    def neighborhood(self):
        return self.parse['address'].get('neighborhood')

    @property
    def city(self):
        return self.parse['address'].get('locality')

    @property
    def state(self):
        return self.parse['address'].get('adminDistrict')

    @property
    def country(self):
        return self.parse['address'].get('countryRegion')

    @property
    def quality(self):
        return self.parse.get('entityType')

    @property
    def accuracy(self):
        return self.parse.get('calculationMethod')

    @property
    def postal(self):
        return self.parse['address'].get('postalCode')

    @property
    def bbox(self):
        if self.parse['bbox']:
            south = self.parse['bbox'][0]
            north = self.parse['bbox'][2]
            west = self.parse['bbox'][1]
            east = self.parse['bbox'][3]
            return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Bing('453 Booth Street, Ottawa Ontario')
    g.debug()
