import requests

params = dict()
ip  = '68.69.18.130'
params['showDetails'] = 'true'
params['showARIN'] = 'true'
#url = 'http://whois.arin.net/rest/nets;q={0}'.format(ip)
url = 'http://whois.arin.net/rest/ip/{0}'.format(ip)

headers = dict()
headers['Accept'] = 'application/json'

r = requests.get(url, params=params, headers=headers)

print r.json()


# -*- coding: utf-8 -*-

from base import Base


class Ip(Base):
    name = 'IP'

    def __init__(self, location):
        self.location = location
        url = 'https://geoip.maxmind.com/geoip/v2.0/city_isp_org/{ip}'
        self.url = url.format(ip=location)
        self.json = dict()
        self.params = dict()
        self.params['geolocation_status'] = 'UNSUPPORTED'
        self.headers = dict()
        self.headers['Referer'] = 'http://www.maxmind.com/en/javascript_demo'

    def lat(self):
        return self.safe_coord('location-latitude')

    def lng(self):
        return self.safe_coord('location-longitude')

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

    def quality(self):
        return self.safe_format('traits-isp')

    def postal(self):
        return self.safe_format('postal-code')

    def city(self):
        return self.safe_format('city')

    def state(self):
        return self.safe_format('subdivisions')

    def country(self):
        return self.safe_format('country')

    def ip(self):
        return self.safe_format('traits-ip_address')
