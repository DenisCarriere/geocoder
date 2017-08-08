#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.google import GoogleResult, GoogleQuery
from geocoder.location import Location


class GoogleReverseResult(GoogleResult):

    @property
    def ok(self):
        return bool(self.address)


class GoogleReverse(GoogleQuery):
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
        return {
            'latlng': str(Location(location)),
            'sensor': 'false',
        }


if __name__ == '__main__':
    g = GoogleReverse((45.4215296, -75.6971930))
    g.debug()
