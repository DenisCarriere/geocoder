#!/usr/bin/python
# coding: utf8

from base import Base


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

    Attributes (17/20)
    ------------------
    [ ] accuracy
    [x] address
    [ ] bbox
    [x] city
    [ ] confidence
    [x] country
    [x] county
    [x] hash
    [x] housenumber
    [x] lat
    [x] lng
    [x] location
    [x] neighborhood
    [x] ok
    [x] postal
    [x] provider
    [x] quality
    [x] state
    [x] status
    [x] street
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
        self._yahoo_catch_errors()

    def _yahoo_catch_errors(self):
        status = self.parse['statusDescription']
        if not status == 'OK':
            self.error = status

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['Result']:
            self._build_tree(self.parse['Result'])

    @property
    def lat(self):
        return self.parse['latitude']

    @property
    def lng(self):
        return self.parse['longitude']

    @property
    def address(self):
        line1 = self.parse['line1']
        line2 = self.parse['line2']
        if line1:
            return ', '.join([line1, line2])
        else:
            return line2

    @property
    def housenumber(self):
        return self.parse['house']

    @property
    def street(self):
        return self.parse['street']


    @property
    def neighborhood(self):
        return self.parse['neighborhood']

    @property
    def city(self):
        return self.parse['city']

    @property
    def county(self):
        return self.parse['county']

    @property
    def state(self):
        return self.parse['state']

    @property
    def country(self):
        return self.parse['country']

    @property
    def hash(self):
        return self.parse['hash']

    @property
    def quality(self):
        return self.parse['addressMatchType']

    @property
    def postal(self):
        postal = self.parse['postal']
        if postal:
            return postal
        else:
            return self.parse['uzip']

if __name__ == '__main__':
    g = Yahoo('1552 Payette dr., Ottawa, ON')
    g.debug()