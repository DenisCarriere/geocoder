#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.google import Google
from geocoder.location import Location


class GoogleReverse(Google):
    """
    Google Geocoding API
    ====================
    Geocoding is the process of converting addresses (like "1600 Amphitheatre
    Parkway, Mountain View, CA") into geographic coordinates (like latitude
    37.423021 and longitude -122.083739), which you can use to place markers or
    position the map.

    API Reference
    -------------
    https://developers.google.com/maps/documentation/geocoding/
    """
    provider = 'google'
    method = 'reverse'

    def _location_init(self, location, **kwargs):
        self.location = str(Location(location))
        self.params['latlng'] = self.location
        self.params['sensor'] = 'false'

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = GoogleReverse([45.4049053, -75.7077965])
    g.debug()
