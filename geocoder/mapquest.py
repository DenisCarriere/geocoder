# -*- coding: utf-8 -*-

from base import Base


class Mapquest(Base):
    name = 'MapQuest'
    url = 'http://www.mapquest.ca/_svc/searchio'

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['query0'] = location
        self.params['action'] = 'search'

    def lat(self):
        return self.safe_coord('latLng-lat')

    def lng(self):
        return self.safe_coord('latLng-lng')

    def address(self):
        return self.safe_format('address-singleLineAddress')

    def quality(self):
        return self.safe_format('address-geocodeQualityCode')

    def postal(self):
        return self.safe_format('address-postalCode')
