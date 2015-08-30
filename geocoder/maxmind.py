#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base


class Maxmind(Base):
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
    """
    provider = 'maxmind'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        if location:
            self.location = location
        else:
            self.location = 'me'
        self.headers = {
            'Referer': 'https://www.maxmind.com/en/geoip_demo',
            'Host': 'www.maxmind.com',
        }
        self.params = {'demo': 1}
        self.url = 'https://www.maxmind.com/geoip/v2.0/city_isp_org/{0}'.format(self.location)
        self._initialize(**kwargs)

    def _catch_errors(self):
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
        return self.parse['location'].get('latitude')

    @property
    def lng(self):
        return self.parse['location'].get('longitude')

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
    def domain(self):
        return self.parse['traits'].get('domain')

    @property
    def isp(self):
        return self.parse['traits'].get('isp')

    @property
    def postal(self):
        return self.parse['postal'].get('code')

    @property
    def city(self):
        return self.parse.get('city')

    @property
    def state(self):
        return self.parse.get('subdivision')

    @property
    def country(self):
        return self.parse.get('country')

    @property
    def continent(self):
        return self.parse.get('continent')

    @property
    def ip(self):
        return self.parse['traits'].get('ip_address')

    @property
    def timezone(self):
        return self.parse['location'].get('time_zone')

    @property
    def metro_code(self):
        return self.parse['location'].get('metro_code')

if __name__ == '__main__':
    g = Maxmind('8.8.8.8')
    g.debug()
