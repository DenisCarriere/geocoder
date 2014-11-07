#!/usr/bin/python
# coding: utf8

from .base import Base


class Ip(Base):
    provider = 'ip'
    api = 'MaxMind\'s GeoIP2'
    _description = 'MaxMind\'s GeoIP2 products enable you to identify the location, \n'
    _description += 'organization, connection speed, and user type of your Internet \n'
    _description += 'visitors. The GeoIP2 databases are among the most popular and \n'
    _description += 'accurate IP geolocation databases available.'
    _api_reference = ['[{0}](https://www.maxmind.com/en/geolocation_landing)'.format(api)]
    _api_parameter = [':param location: (optional) if left blank will return your current IP address\'s location.']
    _example = ['>>> g = geocoder.ip(\'<IP Address>\')',
                '>>> g.lat, g.lng',
                '45.413140 -75.656703']

    def __init__(self, location='me'):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['demo'] = 1
        self.headers = dict()
        self.headers['Referer'] = 'https://www.maxmind.com/en/geoip_demo'
        self.headers['Host'] = 'www.maxmind.com'
        self.url = 'https://www.maxmind.com/geoip/v2.0/city_isp_org/{0}'.format(self.location)

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

    @property
    def lat(self):
        return self._get_json_float('location-latitude')

    @property
    def lng(self):
        return self._get_json_float('location-longitude')

    @property
    def address(self):
        if self.city:
            return '{0}, {1} {2}'.format(self.city, self.state, self.country)
        elif self.state:
            return '{0}, {1}'.format(self.state, self.country)
        else:
            return '{0}'.format(self.country)

    @property
    def domain(self):
        return self._get_json_str('traits-domain')

    @property
    def isp(self):
        return self._get_json_str('traits-isp')

    @property
    def postal(self):
        return self._get_json_str('postal-code')

    @property
    def city(self):
        return self._get_json_str('city')

    @property
    def state(self):
        return self._get_json_str('subdivisions')

    @property
    def country(self):
        return self._get_json_str('country')

    @property
    def continent(self):
        return self._get_json_str('continent')

    @property
    def ip(self):
        return self._get_json_str('traits-ip_address')

if __name__ == '__main__':
    ip = '74.125.226.99'
    g = Ip(ip)
    g.help()
    g.debug()