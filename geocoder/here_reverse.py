#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import app_id, app_code
from .location import Location


class HereReverse(Base):
    """
    HERE Geocoding REST API
    =======================
    Send a request to the geocode endpoint to find an address
    using a combination of country, state, county, city,
    postal code, district, street and house number.

    API Reference
    -------------
    https://developer.here.com/rest-apis/documentation/geocoder

    OSM Quality (6/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal

    Attributes (19/19)
    ------------------
    [x] accuracy
    [x] address
    [x] bbox
    [x] city
    [x] confidence
    [x] country
    [x] county
    [x] housenumber
    [x] lat
    [x] lng
    [x] location
    [x] neighborhood
    [x] ok
    [x] postal
    [x] provider
    [x] quality
    [x] state
    [x] status
    [x] street
    """
    provider = 'here'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json'
        self.location = Location(location).latlng
        self.params = {
            'prox': self.location,
            'app_id': kwargs.get('app_id', app_id),
            'app_code': kwargs.get('app_code', app_code),
            'mode': 'retrieveAddresses',
            'gen': 8,
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = HereReverse([45.4049053, -75.7077965])
    g.debug()
