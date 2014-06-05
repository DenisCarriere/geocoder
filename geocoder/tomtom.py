#!/usr/bin/python
# coding: utf8

from base import Base


class Tomtom(Base):
    name = 'TomTom'
    url = 'https://api.tomtom.com/lbs/geocoding/geocode'

    def __init__(self, location, key):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['key'] = key
        self.params['query'] = location
        self.params['format'] = 'json'
        self.params['maxResults'] = 1
        if not key:
            self.help_key()

    @property
    def lat(self):
        return self.safe_coord('geoResult-latitude')

    @property
    def lng(self):
        return self.safe_coord('geoResult-longitude')

    @property
    def street_number(self):
        return self.safe_format('geoResult-houseNumber')

    @property
    def route(self):
        return self.safe_format('geoResult-street')

    @property
    def address(self):
        return self.safe_format('geoResult-formattedAddress')

    @property
    def quality(self):
        return self.safe_format('geoResult-type')

    @property
    def postal(self):
        return self.safe_format('geoResult-postcode')

    @property
    def locality(self):
        return self.safe_format('geoResult-city')

    @property
    def state(self):
        return self.safe_format('geoResult-state')

    @property
    def country(self):
        return self.safe_format('geoResult-country')

    def help_key(self):
        print '<ERROR> Please provide a Key paramater when using TomTom'
        print '>>> import geocoder'
        print '>>> key = "XXXX"'
        print '>>> g = geocoder.tomtom(<location>, key=key)'
        print ''
        print 'How to get a Key?'
        print '-----------------'
        print 'http://developer.tomtom.com/products/geocoding_api'
