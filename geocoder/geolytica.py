#!/usr/bin/python
# coding: utf8

from base import Base
import xmltodict

class Geolytica(Base):
    provider = 'Geolytica'
    api = 'Geocoder.ca'
    url = 'http://geocoder.ca'
    api_references = ['[{0}](http://geocoder.ca/?api=1)'.format(api)]
    description = 'Geocoder.ca - A Canadian and US location geocoder.'

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['geoit'] = 'XML'
        self.params['locate'] = location

        # Initialize
        self._connect()
        self._parse(xmltodict.parse(self.content))
        self._test()
        self._json()

    @property
    def lat(self):
        return self._get_json_float('geodata-latt')

    @property
    def lng(self):
        return self._get_json_float('geodata-longt')

    @property
    def postal(self):
        return self._get_json_str('geodata-postal')

    @property
    def street_number(self):
        return self._get_json_str('standard-stnumber')

    @property
    def route(self):
        return self._get_json_str('standard-staddress')

    @property
    def locality(self):
        return self._get_json_str('standard-city')

    @property
    def state(self):
        return self._get_json_str('standard-prov')

    @property
    def address(self):
        if self.street_number:
            return '{0} {1}, {2}'.format(self.street_number, self.route, self.locality)
        elif bool(self.route and self.route != 'un-known'):
            return '{0}, {1}'.format(self.route, self.locality)
        else:
            return self.locality

if __name__ == '__main__':
    g = Geolytica('453 Booth street, Ottawa')
    g.help()
    g.debug()