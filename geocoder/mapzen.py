#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.location import BBox
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import mapzen_key


class MapzenResult(OneResult):

    def __init__(self, json_content):
        # create safe shortcuts
        self._geometry = json_content.get('geometry', {})
        self._properties = json_content.get('properties', {})

        # proceed with super.__init__
        super(MapzenResult, self).__init__(json_content)

    @property
    def lat(self):
        return self._geometry['coordinates'][1]

    @property
    def lng(self):
        return self._geometry['coordinates'][0]

    @property
    def bbox(self):
        return BBox.factory(self.latlng).as_dict

    @property
    def address(self):
        return self._properties.get('label')

    @property
    def housenumber(self):
        return self._properties.get('housenumber')

    @property
    def street(self):
        return self._properties.get('street')

    @property
    def neighbourhood(self):
        return self._properties.get('neighbourhood')

    @property
    def city(self):
        return self._properties.get('locality')

    @property
    def state(self):
        return self._properties.get('region')

    @property
    def country(self):
        return self._properties.get('country')

    @property
    def postal(self):
        return self._properties.get('postalcode')

    @property
    def gid(self):
        return self._properties.get('gid')

    @property
    def id(self):
        return self._properties.get('id')


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

    def __init__(self, *args, **kwargs):
        raise DeprecationWarning('MapZen shut down as of January 2018: https://mapzen.com/blog/shutdown')

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
