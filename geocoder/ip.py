#!/usr/bin/python
# coding: utf8

from .base import Base


class Ip(Base):
    """
    MaxMind's GeoIP2
    =======================
    MaxMind's GeoIP2 products enable you to identify the location,
    organization, connection speed, and user type of your Internet
    visitors. The GeoIP2 databases are among the most popular and
    accurate IP geolocation databases available.

    API Reference
    -------------
    https://www.maxmind.com/en/geolocation_landing

    OSM Quality (4/6)
    -----------------
    [ ] addr:housenumber
    [ ] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal
    """
    provider = 'ip'
    method = 'geocode'

    def __init__(self, location='me', **kwargs):
        self.url = 'https://www.maxmind.com/geoip/v2.0/city_isp_org/{0}'.format(location)
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.headers = {
            'Referer': 'https://www.maxmind.com/en/geoip_demo',
            'Host': 'www.maxmind.com',
        }
        self.params = {'demo': 1,}
        self._initialize(**kwargs)

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
    def housenumber(self):
        return ''

    @property
    def street(self):
        return ''

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
    g = Ip('74.125.226.99')
    g.debug()