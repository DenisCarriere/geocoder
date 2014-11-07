#!/usr/bin/python
# coding: utf8

from .base import Base
from .location import Location

class Elevation(Base):
    provider = 'elevation'
    api = 'Google Elevevation API'
    url = 'https://maps.googleapis.com/maps/api/elevation/json'

    _description = 'The Elevation API provides elevation data for all locations on the surface of the\n'
    _description += 'earth, including depth locations on the ocean floor (which return negative values).\n'
    _description += 'In those cases where Google does not possess exact elevation measurements at the\n'
    _description += 'precise location you request, the service will interpolate and return an averaged\n'
    _description += 'value using the four nearest locations.\n'
    _api_reference = ['[{0}](https://developers.google.com/maps/documentation/elevation/)'.format(api)]
    _api_parameter = [':param ``location``: (input) can be specified as [lat, lng].']
    _example = ['>>> g = geocoder.elevation(\'<address or [lat,lng]>\')',
                '>>> g.meters',
                '48.5']

    def __init__(self, location):
        self.location = location
        g = Location(location)
        self.lat, self.lng = g.lat, g.lng
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['locations'] = '{0},{1}'.format(self.lat, self.lng)

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

    def __repr__(self):
        return "<[{0}] {1} [{2}]>".format(self.status, self.provider, self.meters)

    @property
    def status(self):
        if self.elevation:
            return 'OK'
        else:
            return 'ERROR - No Elevation found'

    @property
    def ok(self):
        return bool(self.elevation)

    @property
    def meters(self):
        return round(self.elevation, 1)

    @property
    def feet(self):
        return round(self.elevation * 3.28084, 1)

    @property
    def elevation(self):
        return self._get_json_float('elevation')

    @property
    def resolution(self):
        return round(self._get_json_float('resolution'), 1)

if __name__ == '__main__':
    g = Elevation('Ottawa, ON')
    g.help()
    g.debug()