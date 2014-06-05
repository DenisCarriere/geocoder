#!/usr/bin/python
# coding: utf8

from base import Base


class Mapquest(Base):
    name = 'MapQuest'
    url = 'http://www.mapquest.ca/_svc/searchio'

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['action'] = 'search'
        self.params['query0'] = location
        self.params['maxResults'] = 1
        self.params['page'] = 0
        self.params['thumbMaps'] = 'false'

    @property
    def lat(self):
        return self.safe_coord('latLng-lat')

    @property
    def lng(self):
        return self.safe_coord('latLng-lng')

    @property
    def address(self):
        return self.safe_format('address-singleLineAddress')

    @property
    def quality(self):
        return self.safe_format('address-quality')

    @property
    def postal(self):
        return self.safe_format('address-postalCode')

    @property
    def locality(self):
        return self.safe_format('address-locality')

    @property
    def state(self):
        return self.safe_format('address-regionLong')

    @property
    def country(self):
        return self.safe_format('address-countryLong')
