# -*- coding: utf-8 -*-

from base import Base


class Nokia(Base):
    name = 'Nokia'
    url = 'http://geocoder.api.here.com/6.2/geocode.json'
    app_id = '6QqTvc3kUWsMjYi7iGRb'
    app_code = 'q7R__C774SunvWJDEiWbcA'

    def __init__(self, location, app_id='', app_code=''):
        self.location = location
        if not app_id or not app_code:
            app_id = self.app_id
            app_code = self.app_code
        self.json = dict()
        self.params = dict()
        self.params['searchtext'] = location
        self.params['app_id'] = app_id
        self.params['app_code'] = app_code
        self.params['gen'] = 4

    def lat(self):
        return self.safe_coord('NavigationPosition-Latitude')

    def lng(self):
        return self.safe_coord('NavigationPosition-Longitude')

    def address(self):
        return self.safe_format('Address-Label')

    def quality(self):
        return self.safe_format('Result-MatchLevel')

    def postal(self):
        return self.safe_format('Address-PostalCode')

    def bbox(self):
        south = self.json.get('BottomRight-Latitude')
        west = self.json.get('TopLeft-Longitude')
        north = self.json.get('TopLeft-Latitude')
        east = self.json.get('BottomRight-Longitude')
        return self.safe_bbox(south, west, north, east)

    def city(self):
        return self.safe_format('Address-City')

    def country(self):
        return self.safe_format('Address-Country')
