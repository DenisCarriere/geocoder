#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.location import Location


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
        self.location = str(Location(location))
        self.params = {
            'locations': self.location,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])

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
        if self.elevation:
            return round(self.elevation, 1)

    @property
    def feet(self):
        if self.elevation:
            return round(self.elevation * 3.28084, 1)

    @property
    def elevation(self):
        return self.parse.get('elevation')

    @property
    def resolution(self):
        return self.parse.get('resolution')

if __name__ == '__main__':
    g = Elevation([45.123, -76.123])
    g.debug()
