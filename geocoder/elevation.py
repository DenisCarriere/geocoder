#!/usr/bin/python
# coding: utf8

from .base import Base
from .location import Location


class Elevation(Base):
    """
    Google Elevation API
    ====================
    The Elevation API provides elevation data for all locations on the surface of the
    earth, including depth locations on the ocean floor (which return negative values).
    In those cases where Google does not possess exact elevation measurements at the
    precise location you request, the service will interpolate and return an averaged
    value using the four nearest locations.

    API Reference
    -------------
    https://developers.google.com/maps/documentation/elevation/

    """
    provider = 'google'
    method = 'elevation'

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/elevation/json'
        self.location = Location(location).latlng
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'locations': self.location,
        }
        self._initialize(**kwargs)

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
    g = Elevation([45.123, -76.123])
    g.debug()