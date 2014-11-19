#!/usr/bin/python
# coding: utf8

from .base import Base

class Yahoo(Base):
    provider = 'yahoo'
    api = 'Yahoo BOSS Geo Services'
    url = 'https://sgws2.maps.yahoo.com/FindLocation'
    _description = 'Yahoo PlaceFinder is a geocoding Web service that helps developers make\n'
    _description += 'their applications location-aware by converting street addresses or\n'
    _description += 'place names into geographic coordinates (and vice versa).'
    _api_reference = ['[{0}](https://developer.yahoo.com/boss/geo/)'.format(api)]
    _api_parameter  = []

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['flags'] = 'J'
        self.params['q'] = location
        self.params['locale'] = 'en-CA'

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

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
    def status_description(self):
        return self._get_json_str('statusDescription')

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

if __name__ == '__main__':
    g = Yahoo('453 Booth street, Ottawa, ON')
    g.help()
    g.debug()