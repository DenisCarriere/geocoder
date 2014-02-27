# -*- coding: utf-8 -*-

from base import Base


class Bing(Base):
    #http://msdn.microsoft.com/en-us/library/ff701713.aspx
    name = 'Bing'
    url = 'http://dev.virtualearth.net/REST/v1/Locations'
    key = 'AtnSnX1rEHr3yTUGC3EHkD6Qi3NNB-PABa_F9F8zvLxxvt8A7aYdiG3bGM_PorOq'

    def __init__(self, location, key=''):
        self.location = location
        if not key:
            key = self.key
        self.params = dict()
        self.json = dict()
        self.params['key'] = key
        self.params['q'] = location
        self.params['maxResults'] = 1

    def lat(self):
        return self.safe_coord('coordinates-0')

    def lng(self):
        return self.safe_coord('coordinates-1')

    def address(self):
        return self.safe_format('address-formattedAddress')

    def status(self):
        return self.safe_format('statusDescription')

    def quality(self):
        return self.safe_format('resources-entityType')

    def postal(self):
        return self.safe_format('address-postalCode')

    def bbox(self):
        south = self.json.get('bbox-0')
        west = self.json.get('bbox-1')
        north = self.json.get('bbox-2')
        east = self.json.get('bbox-3')

        return self.safe_bbox(south, west, north, east)

    def city(self):
        return self.safe_format('address-locality')

    def country(self):
        return self.safe_format('address-countryRegion')
