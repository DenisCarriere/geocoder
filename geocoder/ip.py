#!/usr/bin/python
# coding: utf8

from base import Base


class Ip(Base):
    name = 'IP'

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.headers = dict()
        self.params['demo'] = 1
        self.headers['Referer'] = 'https://www.maxmind.com/en/geoip_demo'
        self.headers['Host'] = 'www.maxmind.com'
        url = 'https://www.maxmind.com/geoip/v2.0/city_isp_org/{ip}'
        self.url = url.format(ip=self.location)

    @property
    def lat(self):
        return self.safe_coord('location-latitude')

    @property
    def lng(self):
        return self.safe_coord('location-longitude')

    @property
    def address(self):
        city = self.safe_format('city')
        province = self.safe_format('subdivisions')
        country = self.safe_format('country')

        if city:
            return '{0}, {1} {2}'.format(city, province, country)
        elif province:
            return '{0}, {1}'.format(province, country)
        elif country:
            return '{0}'.format(country)
        else:
            return None

    @property
    def quality(self):
        return self.safe_format('traits-domain')

    @property
    def isp(self):
        return self.safe_format('traits-isp')

    @property
    def postal(self):
        return self.safe_format('postal-code')

    @property
    def city(self):
        return self.safe_format('city')

    @property
    def state(self):
        return self.safe_format('subdivisions')

    @property
    def country(self):
        return self.safe_format('country')

    @property
    def ip(self):
        return self.safe_format('traits-ip_address')

if __name__ == '__main__':
    ip = '74.125.226.99'
    results = Ip(ip)
    print results.url