#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import mapzen_key


class Mapzen(Base):
    """
    Mapzen REST API
    =======================

    API Reference
    -------------
    https://mapzen.com/documentation/search/search/
    """
    provider = 'mapzen'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://search.mapzen.com/v1/search'
        self.location = location
        key = kwargs.get('key', mapzen_key)
        if not key:
            raise ValueError('Mapzen requires a [key] as parameter.')

        self.params = {
            'text': location,
            'api_key': key,
            'size': kwargs.get('size', 1)
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Only retrieve the first feature
        features = self.parse['features']
        if features:
            self._build_tree(self.parse['features'][0])

    def __iter__(self):
        for item in self.content['features']:
            yield item

    @property
    def lat(self):
        return self.parse['geometry']['coordinates'][1]

    @property
    def lng(self):
        return self.parse['geometry']['coordinates'][0]

    @property
    def bbox(self):
        extent = self.parse['bbox']
        if extent:
            west = extent[0]
            north = extent[1]
            east = extent[2]
            south = extent[3]
            return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self.parse['properties'].get('label')

    @property
    def housenumber(self):
        return self.parse['properties'].get('housenumber')

    @property
    def street(self):
        return self.parse['properties'].get('street')

    @property
    def neighbourhood(self):
        return self.parse['properties'].get('neighbourhood')

    @property
    def city(self):
        return self.parse['properties'].get('locality')

    @property
    def state(self):
        return self.parse['properties'].get('region')

    @property
    def country(self):
        return self.parse['properties'].get('country')

    @property
    def postal(self):
        return self.parse['properties'].get('postalcode')

    @property
    def gid(self):
        return self.parse['properties'].get('gid')

    @property
    def id(self):
        return self.parse['properties'].get('id')


if __name__ == '__main__':
    g = Mapzen('1552 Payette dr., Ottawa, ON', key='search-un1M9Hk')
    g.debug()
