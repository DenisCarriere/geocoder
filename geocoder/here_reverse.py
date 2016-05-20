#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import here_app_id, here_app_code
from geocoder.location import Location
from geocoder.here import Here


class HereReverse(Here, Base):
    """
    HERE Geocoding REST API
    =======================
    Send a request to the geocode endpoint to find an address
    using a combination of country, state, county, city,
    postal code, district, street and house number.

    API Reference
    -------------
    https://developer.here.com/rest-apis/documentation/geocoder
    """
    provider = 'here'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json'
        self.location = str(Location(location))

        # HERE Credentials
        app_id = kwargs.get('app_id', here_app_id)
        app_code = kwargs.get('app_code', here_app_code)
        if not bool(app_id and app_code):
            raise ValueError("Provide app_id & app_code")

        # URL Params
        self.params = {
            'prox': self.location,
            'app_id': app_id,
            'app_code': app_code,
            'mode': 'retrieveAddresses',
            'language': kwargs.get('language ', ''),
            'gen': 8,
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = HereReverse([45.4049053, -75.7077965])
    g.debug()
