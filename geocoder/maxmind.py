#!/usr/bin/python
# coding: utf8

from base import Base


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

    OSM Quality (4/6)
    -----------------
    [ ] addr:housenumber
    [ ] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal

    Attributes (17/23)
    ------------------
    [ ] accuracy
    [x] address
    [ ] bbox
    [x] city
    [ ] confidence
    [x] continent
    [x] country
    [x] domain
    [ ] housenumber
    [x] ip
    [x] isp
    [x] lat
    [x] lng
    [x] location
    [x] metro_code
    [x] ok
    [x] postal
    [x] provider
    [ ] quality
    [x] state
    [x] status
    [ ] street
    [x] timezone
    """
    provider = 'maxmind'
    method = 'geocode'

    def __init__(self, location='me', **kwargs):
        self.location = location
        self.headers = {
            'Referer': 'https://www.maxmind.com/en/geoip_demo',
            'Host': 'www.maxmind.com',
        }
        self.params = {'demo': 1,}
        self.url = 'https://www.maxmind.com/geoip/v2.0/city_isp_org/{0}'.format(self.location)
        self._initialize(**kwargs)
        self._maxmind_catch_errors()

    def _maxmind_catch_errors(self):
        error = self.content.get('error')
        if error:
            code = self.content.get('code')
            self.error = code

    def _exceptions(self):
        subdivisions = self.content.get('subdivisions')
        if subdivisions:
            self.content['subdivision'] = subdivisions[0]

        #Grab all names in [en] and place them in self.parse
        for key, value in self.content.items():
            if isinstance(value, dict):
                for minor_key, minor_value in value.items():
                    if minor_key == 'names':
                        self.parse[key] = minor_value['en']

    def __repr__(self):
        return "hey"

    @property
    def status(self):
        return 'OK'

    @property
    def lat(self):
        return self.parse['location']['latitude']

    @property
    def lng(self):
        return self.parse['location']['longitude']

    @property
    def address(self):
        if self.city:
            return '{0}, {1}, {2}'.format(self.city, self.state, self.country)
        elif self.state:
            return '{0}, {1}'.format(self.state, self.country)
        else:
            return '{0}'.format(self.country)

    @property
    def domain(self):
        return self.parse['traits']['domain']

    @property
    def isp(self):
        return self.parse['traits']['isp']

    @property
    def postal(self):
        return self.parse['postal']['code']

    @property
    def city(self):
        return self.parse['city']

    @property
    def state(self):
        return self.parse['subdivision']

    @property
    def country(self):
        return self.parse['country']

    @property
    def continent(self):
        return self.parse['continent']

    @property
    def ip(self):
        return self.parse['traits']['ip_address']

    @property
    def timezone(self):
        return self.parse['location']['time_zone']

    @property
    def metro_code(self):
        return self.parse['location']['metro_code']

if __name__ == '__main__':
    g = Maxmind('74.125.226.99')
    print g.debug()