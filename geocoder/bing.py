#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import bing_key
import re


class BingResult(OneResult):

    @property
    def lat(self):
        coord = self.raw['point']['coordinates']
        if coord:
            return coord[0]

    @property
    def lng(self):
        coord = self.raw['point']['coordinates']
        if coord:
            return coord[1]

    @property
    def address(self):
        return self.raw['address'].get('formattedAddress')

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
        return self.raw['address'].get('addressLine')

    @property
    def neighborhood(self):
        return self.raw['address'].get('neighborhood')

    @property
    def city(self):
        return self.raw['address'].get('locality')

    @property
    def state(self):
        return self.raw['address'].get('adminDistrict')

    @property
    def country(self):
        return self.raw['address'].get('countryRegion')

    @property
    def quality(self):
        return self.raw.get('entityType')

    @property
    def accuracy(self):
        return self.raw.get('calculationMethod')

    @property
    def postal(self):
        return self.raw['address'].get('postalCode')

    @property
    def bbox(self):
        if self.raw['bbox']:
            south = self.raw['bbox'][0]
            north = self.raw['bbox'][2]
            west = self.raw['bbox'][1]
            east = self.raw['bbox'][3]
            return self._get_bbox(south, west, north, east)


class BingQuery(MultipleResultsQuery):
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

    _URL = 'http://dev.virtualearth.net/REST/v1/Locations'
    _RESULT_CLASS = BingResult
    _KEY = bing_key

    def _build_headers(self, provider_key, **kwargs):
        return {
            'Referer': "http://addxy.com/",
            'User-agent': 'Mozilla/5.0'
        }

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'q': location,
            'o': 'json',
            'inclnb': 1,
            'key': provider_key,
            'maxResults': kwargs.get('maxRows', 1)
        }

    def _catch_errors(self, json_response):
        status = json_response['statusDescription']
        if not status == 'OK':
            self.error = status

        return self.error

    def _adapt_results(self, json_response):
        # extract the array of JSON objects
        sets = json_response['resourceSets']
        if sets:
            return sets[0]['resources']
        return []


if __name__ == '__main__':
    g = BingQuery('453 Booth Street, Ottawa Ontario')
    g.debug()
