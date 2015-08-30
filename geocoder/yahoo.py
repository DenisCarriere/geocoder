#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base


class Yahoo(Base):
    """
    Yahoo BOSS Geo Services
    =======================
    Yahoo PlaceFinder is a geocoding Web service that helps developers make
    their applications location-aware by converting street addresses or
    place names into geographic coordinates (and vice versa).

    API Reference
    -------------
    https://developer.yahoo.com/boss/geo/
    """
    provider = 'yahoo'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://sgws2.maps.yahoo.com/FindLocation'
        self.location = location
        self.params = {
            'q': location,
            'flags': 'J',
            'locale': kwargs.get('locale', 'en-CA'),
        }
        self._initialize(**kwargs)

    def _catch_errors(self):
        status = self.parse['statusDescription']
        if status:
            if not status == 'OK':
                self.error = status

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['Result']:
            self._build_tree(self.parse['Result'])

    @property
    def lat(self):
        return self.parse.get('latitude')

    @property
    def lng(self):
        return self.parse.get('longitude')

    @property
    def address(self):
        line1 = self.parse.get('line1')
        line2 = self.parse.get('line2')
        if line1:
            return ', '.join([line1, line2])
        else:
            return line2

    @property
    def housenumber(self):
        return self.parse.get('house')

    @property
    def street(self):
        return self.parse.get('street')

    @property
    def neighborhood(self):
        return self.parse.get('neighborhood')

    @property
    def city(self):
        return self.parse.get('city')

    @property
    def county(self):
        return self.parse.get('county')

    @property
    def state(self):
        return self.parse.get('state')

    @property
    def country(self):
        return self.parse.get('country')

    @property
    def hash(self):
        return self.parse.get('hash')

    @property
    def quality(self):
        return self.parse.get('addressMatchType')

    @property
    def postal(self):
        postal = self.parse.get('postal')
        if postal:
            return postal
        else:
            return self.parse.get('uzip')

if __name__ == '__main__':
    g = Yahoo('1552 Payette dr., Ottawa, ON')
    g.debug()
