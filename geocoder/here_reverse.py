#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

from geocoder.location import Location
from geocoder.here import HereResult, HereQuery


class HereReverseResult(HereResult):

    @property
    def ok(self):
        return bool(self.address)


class HereReverse(HereQuery):
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

    _RESULT_CLASS = HereReverseResult
    _URL = 'http://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json'

    def _build_params(self, location, provider_key, **kwargs):
        params = super(HereReverse, self)._build_params(location, provider_key, **kwargs)
        del params['searchtext']

        location = str(Location(location))
        params.update({
            'prox': location,
            'mode': 'retrieveAddresses',
            'gen': 8,
        })
        return params


if __name__ == '__main__':
    g = HereReverse([45.4049053, -75.7077965])
    g.debug()
