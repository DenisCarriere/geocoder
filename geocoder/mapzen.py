#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base


class Mapzen(Base):
    """
    Mapzen REST API
    =======================

    [FILL IN]

    API Reference
    -------------
    https://pelias.mapzen.com/
    """
    provider = 'mapzen'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://pelias.mapzen.com/search'
        self.location = location
        self.params = {
            'input': location,
            'size': 1,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['features'][0]:
            self._build_tree(self.parse['features'][0])
        if self.parse['properties']:
            self._build_tree(self.parse['properties'])

    # Need a check in here to make sure it fails nicely

    @property
    def lat(self):
        return self.parse['geometry'].get('coordinates')[1]

    @property
    def lng(self):
        return self.parse['geometry'].get('coordinates')[0]

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

#    @property
#    def bbox(self):
#        if self.parse['bbox']:
#            south = self.parse['bbox'].get('ymin')
#            west = self.parse['bbox'].get('xmin')
#            north = self.parse['bbox'].get('ymax')
#            east = self.parse['bbox'].get('xmax')
#            return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Mapzen('London')
    g.debug()
