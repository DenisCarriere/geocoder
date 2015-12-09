#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.mapzen import Mapzen
from geocoder.location import Location
from geocoder.keys import mapzen_key


class MapzenReverse(Mapzen):
    """
    Mapzen REST API
    =======================

    API Reference
    -------------
    https://mapzen.com/documentation/search/reverse/
    """
    provider = 'mapzen'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'https://search.mapzen.com/v1/reverse'
        self.location = location
        location = Location(location)
        key = kwargs.get('key', mapzen_key)
        if not key:
            raise ValueError('Mapzen requires a [key] as parameter.')

        self.params = {
            'point.lat': location.lat,
            'point.lon': location.lng,
            'size': kwargs.get('size', 1),
            'layers': kwargs.get('layers'),
            'source': kwargs.get('sources'),
            'boundary.country': kwargs.get('country'),
            'api_key': key
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.address)


if __name__ == '__main__':
    g = MapzenReverse("45.4049053 -75.7077965", key='search-un1M9Hk')
    g.debug()
