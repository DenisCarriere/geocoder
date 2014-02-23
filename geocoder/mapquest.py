# -*- coding: utf-8 -*-

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

    def lat(self):
        return self.safe_coord('latLng-lat')

    def lng(self):
        return self.safe_coord('latLng-lng')

    def address(self):
        return self.safe_format('address-singleLineAddress')

    def quality(self):
        return self.safe_format('address-quality')

    def postal(self):
        return self.safe_format('address-postalCode')

    def city(self):
        return self.safe_format('address-locality')

    def country(self):
        return self.safe_format('address-countryLong')
