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
        self.params = {
            'input': location,
            'size': 1,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
         if self.parse['features']:
             if self.parse['features'][0]:
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
    g = Mapzen('ᐃᖃᓗᐃᑦ')
    g.debug()
    g = Mapzen('343 Booth Street')
    g.debug()
    g = Mapzen('Burj Khalifa')
    g.debug()
    g = Mapzen('Québec')
    g.debug()
