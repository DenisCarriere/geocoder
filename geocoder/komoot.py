#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base

class Komoot(Base):
    """
    Komoot REST API
    =======================

    API Reference
    -------------
    http://photon.komoot.de
    """
    provider = 'komoot'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://photon.komoot.de/api'
        self.location = location
        if 'result' in kwargs:
            if kwargs['result']:
                limit = kwargs['result']
        else:
            size = 1
        self.params = {
            'q': location,
            'limit': limit,
            'lang': 'en',
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
        def xstr(s):
            if s is None:
                return ''
            return unicode(s) + " "
        return xstr((self.parse['properties'].get('housenumber'))) + xstr((self.parse['properties'].get('street'))) + xstr((self.parse['properties'].get('city'))) + xstr((self.parse['properties'].get('state'))) + xstr((self.parse['properties'].get('country'))) + xstr((self.parse['properties'].get('postcode')))

    @property
    def country(self):
         return self.parse['properties'].get('country')

    @property
    def state(self):
         return self.parse['properties'].get('state')

    @property
    def city(self):
         return self.parse['properties'].get('city')

    @property
    def street(self):
         return self.parse['properties'].get('street')

    @property
    def housenumber(self):
         return self.parse['properties'].get('housenumber')

    @property
    def postal(self):
         return self.parse['properties'].get('postcode')    

if __name__ == '__main__':
    g = Komoot('Toronto',result=1)
    print " "
    print g.json
    g = Komoot('Toronto',result=2)
    print " "
    print g.json
    g = Komoot('Toronto',result=3)
    print " "
    print g.json
    g = Komoot('Toronto',result=4)
    print " "
    print g.json
    g = Komoot('Burj Khalifa',result=1)
    print " "
    print g.json
    g = Komoot('52 Northview Road',result=1)
    print " "
    print g.json
