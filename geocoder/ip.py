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
