#!/usr/bin/python
# coding: utf8

from base import Base
from google import Google
from location import Location

class Elevation(Google, Base):
    name = 'Elevation Google'
    url = 'http://maps.googleapis.com/maps/api/elevation/json'

    def __init__(self, latlng):
        self.location = latlng
        self.json = dict()
        self.params = dict()
        lat, lng = Location(latlng).latlng
        self.latlng = '{0},{1}'.format(lat, lng)

        # Parameters for URL request
        self.params['locations'] = self.latlng

    @property
    def meters(self):
        return round(self.elevation, 1)

    @property
    def feet(self):
        return round(self.elevation * 3.28084, 1)

    @property
    def elevation(self):
        return self.safe_format('results-elevation')

    @property
    def resolution(self):
        return round(self.safe_format('results-resolution'), 1)

if __name__ == '__main__':
    from api import Geocoder
    latlng = (45.4215296, -75.69719309999999)
    provider = Elevation(latlng)
    g = Geocoder(provider)
    print g.resolution
    print g.elevation
    print g.json