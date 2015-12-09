#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.google import Google
from geocoder.location import Location
from geocoder.keys import google_key, google_client


class GoogleReverse(Google, Base):
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

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.location = str(Location(location))
        self.short_name = kwargs.get('short_name', True)
        self.params = {
            'sensor': 'false',
            'latlng': self.location,
            'key': kwargs.get('key', google_key),
            'language': kwargs.get('language', ''),
            'client': kwargs.get('client', google_client)
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = GoogleReverse([45.4049053, -75.7077965])
    g.debug()
