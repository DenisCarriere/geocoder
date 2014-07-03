#!/usr/bin/python
# coding: utf8

from base import Base
import requests
import xmltodict

class Geolytica(Base):
    name = 'Geolytica'
    url = 'http://geocoder.ca'

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['geoit'] = 'XML'
        self.params['callback'] = 'results'
        self.params['locate'] = location

        # Geolytica only has a valid XML response
        self.parse_xml()

    def parse_xml(self):
        # Connect
        r = requests.get(self.url, params=self.params)

        # Parse XML
        results = xmltodict.parse(r.content)
        if 'geodata' in results:
            for key, value in results['geodata'].items():
                self.json[key] = value
            for key, value in results['geodata']['standard'].items():
                self.json[key] = value

    @property
    def lat(self):
        return self.safe_coord('latt')

    @property
    def lng(self):
        return self.safe_coord('longt')

    @property
    def street_number(self):
        return self.safe_format('stnumber')

    @property
    def route(self):
        return self.safe_format('staddress')

    @property
    def postal(self):
        return self.safe_format('postal')

    @property
    def locality(self):
        return self.safe_format('city')

    @property
    def state(self):
        return self.safe_format('prov')

    @property
    def address(self):
        return '{0} {1}, {2}'.format(self.street_number, self.route, self.locality)

if __name__ == '__main__':
    g = Geolytica('Ottawa, ON')
    print g