# -*- coding: utf-8 -*-

from base import Base


class Bing(Base):
    #http://msdn.microsoft.com/en-us/library/ff701713.aspx
    name = 'Bing'
    url = 'http://dev.virtualearth.net/REST/v1/Locations'

    def __init__(self, location, key='AtnSnX1rEHr3yTUGC3EHkD6Qi3NNB-PABa_F9F8zvLxxvt8A7aYdiG3bGM_PorOq'):
        self.location = location
        self.params = dict()
        self.json = dict()
        self.params['maxResults'] = 1
        self.params['key'] = key
        self.params['q'] = location
        if not key:
            self.help_key()

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

    def state(self):
        return self.safe_format('address-adminDistrict')

    def country(self):
        return self.safe_format('address-countryRegion')

    def help_key(self):
        print '<ERROR>'
        print 'Please provide a <key> paramater when using Bing'
        print '    >>> import geocoder'
        print '    >>> key = "XXXX"'
        print '    >>> g = geocoder.bing(<location>, key=key)'
        print ''
        print 'How to get a Key?'
        print '-----------------'
        print 'http://msdn.microsoft.com/en-us/library/ff428642.aspx'
