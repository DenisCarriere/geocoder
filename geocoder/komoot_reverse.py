#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.komoot import Komoot
from geocoder.location import Location


class KomootReverse(Komoot):
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
        self.url = 'https://photon.komoot.de/reverse'
        self.location = location
        location = Location(location)
        self.params = {
            'lat': location.lat,
            'lon': location.lng,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        if self.parse['features']:
            self._build_tree(self.parse['features'][0])

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = KomootReverse("45.4 -75.7")
    g.debug()
