#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.location import BBox
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import mapzen_key


class MapzenResult(OneResult):

    @property
    def lat(self):
        return self.raw['geometry']['coordinates'][1]

    @property
    def lng(self):
        return self.raw['geometry']['coordinates'][0]

    @property
    def bbox(self):
        return BBox.factory(self.latlng).as_dict

    @property
    def address(self):
        return self.raw['properties'].get('label')

    @property
    def housenumber(self):
        return self.raw['properties'].get('housenumber')

    @property
    def street(self):
        return self.raw['properties'].get('street')

    @property
    def neighbourhood(self):
        return self.raw['properties'].get('neighbourhood')

    @property
    def city(self):
        return self.raw['properties'].get('locality')

    @property
    def state(self):
        return self.raw['properties'].get('region')

    @property
    def country(self):
        return self.raw['properties'].get('country')

    @property
    def postal(self):
        return self.raw['properties'].get('postalcode')

    @property
    def gid(self):
        return self.raw['properties'].get('gid')

    @property
    def id(self):
        return self.raw['properties'].get('id')


class MapzenQuery(MultipleResultsQuery):
    """
    Mapzen REST API
    =======================

    API Reference
    -------------
    https://mapzen.com/documentation/search/search/
    """
    provider = 'mapzen'
    method = 'geocode'

    _URL = 'https://search.mapzen.com/v1/search'
    _RESULT_CLASS = MapzenResult
    _KEY = mapzen_key

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'text': location,
            'api_key': provider_key,
            'size': kwargs.get('maxRows', 1)
        }

    def _adapt_results(self, json_response):
        return json_response['features']


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = MapzenQuery('201 Spear Street, San Francisco')
    g.debug()
