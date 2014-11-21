#!/usr/bin/python
# coding: utf8

from .base import Base

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

    OSM Quality (6/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal
    """
    provider = 'yahoo'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://sgws2.maps.yahoo.com/FindLocation'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'q': location,
            'flags': 'J',
            'locale': kwargs.get('locale', 'en-CA'),
        }
        self._initialize(**kwargs)
        self._yahoo_catch_errors()

    def _yahoo_catch_errors(self):
        status = self._get_json_str('statusDescription')
        if not status == 'OK':
            self.error = status

    @property
    def lat(self):
        return self._get_json_float('latitude')

    @property
    def lng(self):
        return self._get_json_float('longitude')

    @property
    def address(self):
        line1 = self._get_json_str('line1')
        line2 = self._get_json_str('line2')
        if line1:
            return ', '.join([line1, line2])
        else:
            return line2

    @property
    def housenumber(self):
        return self._get_json_str('house')

    @property
    def street(self):
        return self._get_json_str('street')


    @property
    def neighborhood(self):
        return self._get_json_str('neighborhood')

    @property
    def city(self):
        return self._get_json_str('city')

    @property
    def county(self):
        return self._get_json_str('county')

    @property
    def state(self):
        return self._get_json_str('state')

    @property
    def country(self):
        return self._get_json_str('country')

    @property
    def hash(self):
        return self._get_json_str('hash')

    @property
    def quality(self):
        return self._get_json_str('addressMatchType')

    @property
    def postal(self):
        postal = self._get_json_str('postal')
        if postal:
            return self._get_json_str('postal')
        else:
            return self._get_json_str('uzip')

if __name__ == '__main__':
    g = Yahoo('1552 Payette dr., Ottawa, ON')
    g.debug()