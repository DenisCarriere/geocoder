# -*- coding: utf-8 -*-
from base import Base


class Nokia(Base):
    name = 'Nokia'
    url = 'http://geocoder.api.here.com/6.2/geocode.json'

    def __init__(self, location, app_id, app_code):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['searchtext'] = location
        self.params['app_id'] = app_id
        self.params['app_code'] = app_code
        self.params['gen'] = 4

        if not bool(app_id and app_code):
            self.help_key()

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

    def locality(self):
        return self.safe_format('Address-City')

    def state(self):
        return self.safe_format('StateName')

    def country(self):
        return self.safe_format('CountryName')

    def help_key(self):
        print '<ERROR> Please provide both (app_code & app_id) paramaters when using Nokia'
        print '>>> import geocoder'
        print '>>> app_code = "XXXX"'
        print '>>> app_id = "XXXX"'
        print '>>> g = geocoder.nokia(<location>, app_code=app_code, app_id=app_id)'
        print ''
        print 'How to get a Key?'
        print '-----------------'
        print 'http://developer.here.com/get-started'
