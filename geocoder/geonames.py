#!/usr/bin/python
# coding: utf8

from base import Base


class Geonames(Base):
    name = 'GeoNames'
    url = 'http://api.geonames.org/searchJSON'

    def __init__(self, location, username):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['q'] = location
        self.params['fuzzy'] = 0.8
        self.params['maxRows'] = 1
        self.params['username'] = username
        if not username:
            self.help_username()

    def lat(self):
        return self.safe_coord('geonames-lat')

    def lng(self):
        return self.safe_coord('geonames-lng')

    def address(self):
        return self.safe_format('geonames-name')

    def status(self):
        if self.lng():
            return 'OK'
        else:
            msg = self.safe_format('status-message')
            if msg:
                return msg
            else:
                return 'ERROR - No Geometry'

    def quality(self):
        return self.safe_format('geonames-fcodeName')

    def postal(self):
        return None

    def bbox(self):
        return None

    def city(self):
        return None

    def state(self):
        return self.safe_format('geonames-adminName1')

    def country(self):
        return self.safe_format('geonames-countryName')

    def population(self):
        return self.json.get('geonames-population')

    def help_username(self):
        print '<ERROR>'
        print 'Please provide a <username> paramater when using Geonames'
        print '    >>> import geocoder'
        print '    >>> username = "XXXX"'
        print '    >>> g = geocoder.geonames(<location>, username=username)'
        print ''
        print 'How to get a Username?'
        print '----------------------'
        print 'http://www.geonames.org/login'
