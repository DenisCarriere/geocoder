#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import requests
import ratelim
from geocoder.base import Base


class FreeGeoIP(Base):
    """
    FreeGeoIP.net
    =============
    freegeoip.net provides a public HTTP API for software developers to
    search the geolocation of IP addresses. It uses a database of IP addresses
    that are associated to cities along with other relevant information like
    time zone, latitude and longitude.

    You're allowed up to 10,000 queries per hour by default. Once this
    limit is reached, all of your requests will result in HTTP 403,
    forbidden, until your quota is cleared.

    API Reference
    -------------
    http://freegeoip.net/
    """
    provider = 'freegeoip'
    method = 'geocode'

    def __init__(self, location='me', **kwargs):
        self.location = location
        self.url = kwargs.get('url', 'https://telize.j3ss.co/geoip/') + self.location
        self._initialize(**kwargs)

    @staticmethod
    @ratelim.greedy(10000, 60 * 60)
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)

    @property
    def lat(self):
        return self.parse.get('latitude')

    @property
    def lng(self):
        return self.parse.get('longitude')

    @property
    def address(self):
        if self.city:
            return '{0}, {1} {2}'.format(self.city, self.state, self.country)
        elif self.state:
            return '{0}, {1}'.format(self.state, self.country)
        else:
            return '{0}'.format(self.country)

    @property
    def postal(self):
        zip_code = self.parse.get('zip_code')
        postal_code = self.parse.get('postal_code')
        if zip_code:
            return zip_code
        if postal_code:
            return postal_code

    @property
    def city(self):
        return self.parse.get('city')

    @property
    def state(self):
        return self.parse.get('region')

    @property
    def region_code(self):
        return self.parse.get('region_code')

    @property
    def country(self):
        return self.parse.get('country_name')

    @property
    def country_code3(self):
        return self.parse.get('country_code3')

    @property
    def continent(self):
        return self.parse.get('continent')

    @property
    def timezone(self):
        return self.parse.get('timezone')

    @property
    def area_code(self):
        return self.parse.get('area_code')

    @property
    def dma_code(self):
        return self.parse.get('dma_code')

    @property
    def offset(self):
        return self.parse.get('offset')

    @property
    def organization(self):
        return self.parse.get('organization')

    @property
    def offset(self):
        return self.parse.get('offset')

    @property
    def ip(self):
        return self.parse.get('ip')

    @property
    def time_zone(self):
        return self.parse.get('time_zone')


if __name__ == '__main__':
    g = FreeGeoIP('99.240.181.199')
    g.debug()
