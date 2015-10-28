#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.mapzen import Mapzen
from geocoder.location import Location

class MapzenReverse(Base):
    """
    Mapzen REST API
    =======================

    API Reference
    -------------
    https://pelias.mapzen.com/
    """
    provider = 'mapzen'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        t = str(Location(location)).split(",")
        self.url = 'https://pelias.mapzen.com/reverse'
        self.params = {
            'lat': t[0],
            'lon': t[1],
            'size': 1,
        }
        self._initialize(**kwargs)

    def _exceptions(self):							# Seems to always return results, ie: Location: Earth
        self._build_tree(self.parse['features'][0]['geometry'])
        self._build_tree(self.parse['features'][0]['properties'])
        self._build_tree(self.parse['features'][0])

    @property
    def lat(self):
        return self.parse['coordinates'][1]

    @property
    def lng(self):
        return self.parse['coordinates'][0]

    @property
    def address(self):
        return self.parse['properties'].get('text')

    @property
    def country(self):
        return self.parse['properties'].get('alpha3')

    @property
    def state(self):
         return self.parse['properties'].get('admin1')

    @property
    def city(self):
         return self.parse['properties'].get('admin2')

    @property
    def street(self):
         return self.parse['address'].get('street')

    @property
    def housenumber(self):
         return self.parse['address'].get('number')

if __name__ == '__main__':
    g = MapzenReverse([45.4049053, -75.7077965])
    g.debug()
    g = MapzenReverse([45.4049053, -150.7077965])
    g.debug()
    g = MapzenReverse([-1000,1000])
    g.debug()
