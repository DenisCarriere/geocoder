#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base

class Mapzen(Base):
    """
    Mapzen REST API
    =======================

    API Reference
    -------------
    https://pelias.mapzen.com/
    """
    provider = 'mapzen'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://pelias.mapzen.com/search'
        self.location = location
        if 'result' in kwargs:
            if kwargs['result']:
                size = kwargs['result']
        else:
            size = 1
        self.params = {
            'input': location,
            'size': size,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        self._build_tree(self.parse['geometry'])
        self._build_tree(self.parse['properties'])

    def next(self):
        for item in self.content['features']:
            yield item

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
    g = Mapzen('Toronto',result=1)
    print " "
    print g.json
    g = Mapzen('Toronto',result=2)
    print " "
    print g.json
    g = Mapzen('Toronto',result=3)
    print " "
    print g.json
    g = Mapzen('Toronto',result=4)
    print " "
    print g.json
