# -*- coding: utf-8 -*-

from base import Base
from location import Location


class Reverse(Base):
    name = 'Reverse Google'
    url = 'http://maps.googleapis.com/maps/api/geocode/json'

    def __init__(self, latlng):
        self.json = dict()
        self.params = dict()
        location = Location(latlng)
        self.latlng = '{0},{1}'.format(location.lat, location.lng)
        self.location = latlng

        # Parameters for URL request
        self.params['sensor'] = 'false'
        self.params['latlng'] = self.latlng

    def lat(self):
        return self.safe_coord('location-lat')

    def lng(self):
        return self.safe_coord('location-lng')

    def address(self):
        return self.safe_format('results-formatted_address')

    def status(self):
        return self.safe_format('status')

    def quality(self):
        return self.safe_format('geometry-location_type')

    def postal(self):
        return self.safe_format('postal_code')

    def bbox(self):
        south = self.json.get('southwest-lat')
        west = self.json.get('southwest-lng')
        north = self.json.get('northeast-lat')
        east = self.json.get('northeast-lng')
        return self.safe_bbox(south, west, north, east)

    def city(self):
        return self.safe_format('locality')

    def country(self):
        return self.safe_format('country')

if __name__ == '__main__':
    latlng = (45.4215296, -75.69719309999999)
    provider = Reverse(latlng)
    print provider.latlng
