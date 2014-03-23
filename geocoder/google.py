# -*- coding: utf-8 -*-

from base import Base

class Google(Base):
    name = 'Google'
    url = 'http://maps.googleapis.com/maps/api/geocode/json'

    def __init__(self, location='', client='', signature='', proxies=''):
        self.proxies = proxies
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['sensor'] = 'false'
        self.params['address'] = location
        if bool(client and signature):
            self.params['client'] = client
            self.params['signature'] = signature
        
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

    def state(self):
        return self.safe_format('administrative_area_level_1')

    def country(self):
        return self.safe_format('country')

if __name__ == '__main__':
    provider = Google('Ottawa')
    print provider
