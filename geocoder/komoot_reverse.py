#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.komoot import Komoot
from geocoder.location import Location

class KomootReverse(Base):
    """
    Komoot REST API
    =======================

    API Reference
    -------------
    http://photon.komoot.de
    """
    provider = 'komoot'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        t = location.split()
        print t
        self.url = 'https://photon.komoot.de/reverse'
        self.params = {
            'lat': t[0],
            'lon': t[1],
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        if self.parse['features']:
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
    g = KomootReverse("45.4 -75.7")
    g.debug()
