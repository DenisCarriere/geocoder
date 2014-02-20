# -*- coding: utf-8 -*-

from base import Base


class Bing(Base):
    #http://msdn.microsoft.com/en-us/library/ff701713.aspx
    name = 'Bing'
    url = 'http://dev.virtualearth.net/REST/v1/Locations'
    key = ''

    def __init__(self, location, key=''):
        self.location = location
        if not key:
            key = self.key
        self.params = dict()
        self.json = dict()
        self.params['key'] = key
        self.params['q'] = location

    def lat(self):
        return self.safe_coord('coordinates-0')

    def lng(self):
        return self.safe_coord('coordinates-1')

    def address(self):
        return self.safe_format('address-formattedAddress')

    def status(self):
        return self.safe_format('statusDescription')

    def quality(self):
        if self.json.get('matchCodes'):
            return self.safe_format('matchCodes')
        else:
            return self.safe_format('matchCodes-0')

    def postal(self):
        return self.safe_format('address-postalCode')

    def bbox(self):
        southwest = self.json.get('bbox-0'), self.json.get('bbox-1')
        northeast = self.json.get('bbox-2'), self.json.get('bbox-3')
        return self.safe_bbox(southwest, northeast)
