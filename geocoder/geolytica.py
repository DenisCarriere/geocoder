#!/usr/bin/python
# coding: utf8

from .base import Base

class Geolytica(Base):
    """
    Geocoder.ca
    ===========
    A Canadian and US location geocoder.

    API Reference
    -------------
    http://geocoder.ca/?api=1

    OSM Quality (4/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [ ] addr:country
    [ ] addr:postal
    """
    provider = 'geolytica'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocoder.ca'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'json': 1,
            'locate': location,
            'geoit': 'xml',
        }
        self._initialize(**kwargs)

    @property
    def lat(self):
        return self._get_json_float('latt')

    @property
    def lng(self):
        return self._get_json_float('longt')

    @property
    def postal(self):
        return self._get_json_str('postal')

    @property
    def housenumber(self):
        return self._get_json_str('standard-stnumber')

    @property
    def street(self):
        street = self._get_json_str('standard-staddress')
        return street.strip()

    @property
    def city(self):
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
    g = Geolytica('1552 Payette dr., Ottawa')
    g.debug()