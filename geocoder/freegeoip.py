#!/usr/bin/python
# coding: utf8

import requests
from .base import Base
from .ratelim import rate_limited


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

    OSM Quality (4/6)
    -----------------
    [ ] addr:housenumber
    [ ] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal
    """
    provider = 'freegeoip'
    method = 'geocode'

    def __init__(self, location='me', **kwargs):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None

        if self._check_ip_address():
            self.url = 'http://freegeoip.net/json/{0}'.format(self.location)
            self._initialize(**kwargs)

    @staticmethod
    @rate_limited(10000, 60*60)
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)

    @property
    def lat(self):
        return self._get_json_float('latitude')

    @property
    def lng(self):
        return self._get_json_float('longitude')

    @property
    def address(self):
        if self.city:
            return '{0}, {1} {2}'.format(self.city, self.state, self.country)
        elif self.state:
            return '{0}, {1}'.format(self.state, self.country)
        else:
            return '{0}'.format(self.country)
    
    @property
    def housenumber(self):
        return ''

    @property
    def street(self):
        return ''

    @property
    def postal(self):
        return self._get_json_str('zip_code')

    @property
    def city(self):
        return self._get_json_str('city')

    @property
    def state(self):
        return self._get_json_str('region_name')

    @property
    def country(self):
        return self._get_json_str('country_name')

    @property
    def continent(self):
        return self._get_json_str('continent')

    @property
    def ip(self):
        return self._get_json_str('ip')

    @property
    def time_zone(self):
        return self._get_json_str('time_zone')


if __name__ == '__main__':
    g = FreeGeoIP('99.240.181.199')
    g.debug()
