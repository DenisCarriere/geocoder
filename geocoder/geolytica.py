#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base


class Geolytica(Base):
    """
    Geocoder.ca
    ===========
    A Canadian and US location geocoder.

    API Reference
    -------------
    http://geocoder.ca/?api=1
    """
    provider = 'geolytica'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocoder.ca'
        self.location = location
        self.params = {
            'json': 1,
            'locate': location,
            'geoit': 'xml'
        }
        if 'strictmode' in kwargs:
            self.params.update({'strictmode': kwargs.pop('strictmode')})
        if 'strict' in kwargs:
            self.params.update({'strict': kwargs.pop('strict')})
        if 'auth' in kwargs:
            self.params.update({'auth': kwargs.pop('auth')})
        self._initialize(**kwargs)

    @property
    def lat(self):
        lat = self.parse.get('latt', '').strip()
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = self.parse.get('longt', '').strip()
        if lng:
            return float(lng)

    @property
    def postal(self):
        return self.parse.get('postal', '').strip()

    @property
    def housenumber(self):
        return self.parse['standard'].get('stnumber', '').strip()

    @property
    def street(self):
        return self.parse['standard'].get('staddress', '').strip()

    @property
    def city(self):
        return self.parse['standard'].get('city', '').strip()

    @property
    def state(self):
        return self.parse['standard'].get('prov', '').strip()

    @property
    def address(self):
        if self.street_number:
            return u'{0} {1}, {2}'.format(self.street_number, self.route, self.locality)
        elif self.route and self.route != 'un-known':
            return u'{0}, {1}'.format(self.route, self.locality)
        else:
            return self.locality

if __name__ == '__main__':
    g = Geolytica('1552 Payette dr., Ottawa')
    g.debug()
