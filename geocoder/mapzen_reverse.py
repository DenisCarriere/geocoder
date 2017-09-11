#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.mapzen import MapzenResult, MapzenQuery
from geocoder.location import Location


class MapzenReverseResult(MapzenResult):

    @property
    def ok(self):
        return bool(self.address)


class MapzenReverse(MapzenQuery):
    """
    Mapzen REST API
    =======================

    API Reference
    -------------
    https://mapzen.com/documentation/search/reverse/
    """
    provider = 'mapzen'
    method = 'reverse'

    _URL = 'https://search.mapzen.com/v1/reverse'
    _RESULT_CLASS = MapzenReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            'point.lat': location.lat,
            'point.lon': location.lng,
            'size': kwargs.get('size', 1),
            'layers': kwargs.get('layers'),
            'source': kwargs.get('sources'),
            'boundary.country': kwargs.get('country'),
            'api_key': provider_key
        }


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = MapzenReverse("45.4049053 -75.7077965", key='search-un1M9Hk')
    g.debug()
