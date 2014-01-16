# -*- coding: utf-8 -*-

from base import Base


class Google(Base):
    name = 'Google'
    url = 'http://maps.googleapis.com/maps/api/geocode/json'

    def __init__(self, location, proxies=''):
        self.proxies = proxies
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['sensor'] = 'false'
        self.params['address'] = location

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
        southwest = self.json.get('southwest-lat'), self.json.get('southwest-lng')
        northeast = self.json.get('northeast-lat'), self.json.get('northeast-lng')
        return self.safe_bbox(southwest, northeast)

if __name__ == '__main__':
    provider = Google('Ottawa')
    print provider
