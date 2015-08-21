#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base


class IpinfoIo(Base):
    """
    API Reference
    -------------
    https://www.ipinfo.io
    """
    provider = 'ipinfoio'
    method = 'geocode'
    def __init__(self, location='', **kwargs):
        self.location = location
        self.url = 'http://ipinfo.io/{0}/json'.format(self.location)
        self._initialize(**kwargs)
        self._ipinfoio_catch_errors()

    def _ipinfoio_catch_errors(self):
        error = self.content.get('error')
        if error:
            code = self.content.get('code')
            self.error = code

    def _exceptions(self):
        subdivisions = self.content.get('subdivisions')
        if subdivisions:
            self.content['subdivision'] = subdivisions[0]

        # Grab all names in [en] and place them in self.parse
        for key, value in self.content.items():
            if isinstance(value, dict):
                for minor_key, minor_value in value.items():
                    if minor_key == 'names':
                        self.parse[key] = minor_value['en']

    @property
    def lat(self):
        return self.parse.get('loc').split(',')[0]

    @property
    def lng(self):
         return self.parse.get('loc').split(',')[1]

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
    g = IpinfoIo('')
    g.debug()
