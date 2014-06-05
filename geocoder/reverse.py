#!/usr/bin/python
# coding: utf8

from base import Base
from google import Google
from location import Location


class Reverse(Google, Base):
    name = 'Reverse Google'
    url = 'http://maps.googleapis.com/maps/api/geocode/json'

    def __init__(self, latlng, short_name=True):
        self.location = latlng
        self.short_name = short_name
        self.json = dict()
        self.params = dict()
        lat, lng = Location(latlng).latlng
        self.latlng = '{0},{1}'.format(lat, lng)

        # Parameters for URL request
        self.params['sensor'] = 'false'
        self.params['latlng'] = self.latlng

if __name__ == '__main__':
    latlng = (45.4215296, -75.69719309999999)
    provider = Reverse(latlng)
    print provider.latlng
