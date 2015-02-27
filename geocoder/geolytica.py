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

    OSM Quality (5/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [ ] addr:country
    [x] addr:postal

    Attributes (12/17)
    ------------------
    [ ] accuracy
    [x] address
    [ ] bbox
    [x] city
    [ ] confidence
    [ ] country
    [x] housenumber
    [x] lat
    [x] lng
    [x] location
    [x] ok
    [x] postal
    [x] provider
    [ ] quality
    [x] state
    [x] status
    [x] street
    """
    provider = 'geolytica'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocoder.ca'
        self.location = location
        self.params = {
            'json': 1,
            'locate': location,
            'geoit': 'xml',
        }
        self._initialize(**kwargs)

    @property
    def lat(self):
        return self.parse.get('latt')

    @property
    def lng(self):
        return self.parse.get('longt')

    @property
    def postal(self):
        return self.parse.get('postal')

    @property
    def housenumber(self):
        return self.parse['standard'].get('stnumber')

    @property
    def street(self):
        return self.parse['standard'].get('staddress')

    @property
    def city(self):
        return self.parse['standard'].get('city')

    @property
    def state(self):
        return self.parse['standard'].get('prov')

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
