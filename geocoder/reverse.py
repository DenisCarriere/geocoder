#!/usr/bin/python
# coding: utf8

from .base import Base
from .google import Google
from .location import Location


class Reverse(Google, Base):
    provider = 'reverse'
    api = 'Google Geocoding API'
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    _description = 'The term geocoding generally refers to translating a human-readable address into\n'
    _description += 'a location on a map. The process of doing the opposite, translating a location\n'
    _description += 'on the map into a human-readable address, is known as reverse geocoding.'
    _api_reference = ['[{0}](https://developers.google.com/maps/documentation/geocoding/)'.format(api)]
    _api_parameter = [':param ``location``: (required) must be specified as [lat, lng].']
    _api_parameter = [':param ``short_name``: (optional) if ``False`` will retrieve the results with Long names.']
    _example = ['>>> g = geocoder.reverse([\'lat\',\'lng\'])',
                '>>> g.address',
                '\'453 Booth Street, Ottawa\'']

    def __init__(self, location, short_name=True):
        self.location = location
        self.short_name = short_name
        g = Location(location)
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['sensor'] = 'false'
        self.params['latlng'] = '{0},{1}'.format(g.lat, g.lng)

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = Reverse([45.4049053, -75.7077965], short_name=False)
    g.help()
    g.debug()