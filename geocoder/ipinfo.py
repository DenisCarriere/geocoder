#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.location import Location


class Ipinfo(Base):
    """
    API Reference
    -------------
    https://ipinfo.io
    """
    provider = 'ipinfo'
    method = 'geocode'

    def __init__(self, location='', **kwargs):
        self.location = location
        if location.lower() == 'me':
            self.location = ''
        self.url = 'http://ipinfo.io/{0}/json'.format(self.location)
        self._initialize(**kwargs)

    def _catch_errors(self):
        content = self.content
        if content and self.status_code == 400:
            self.error = content

    @property
    def lat(self):
        loc = self.parse.get('loc')
        if loc:
            return Location(loc).lat

    @property
    def lng(self):
        loc = self.parse.get('loc')
        if loc:
            return Location(loc).lng

    @property
    def address(self):
        if self.city:
            return '{0}, {1}, {2}'.format(self.city, self.state, self.country)
        elif self.state:
            return '{0}, {1}'.format(self.state, self.country)
        elif self.country:
            return '{0}'.format(self.country)
        else:
            return ''

    @property
    def postal(self):
        return self.parse.get('postal')

    @property
    def city(self):
        return self.parse.get('city')

    @property
    def state(self):
        return self.parse.get('region')

    @property
    def country(self):
        return self.parse.get('country')

    @property
    def hostname(self):
        return self.parse.get('hostname')

    @property
    def ip(self):
        return self.parse.get('ip')

    @property
    def org(self):
        return self.parse.get('org')

if __name__ == '__main__':
    g = Ipinfo('8.8.8.8')
    g.debug()
