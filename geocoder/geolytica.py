#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery


def _correct_empty_dict(obj, key, alt=''):
    try:
        k = obj.get(key, alt).strip()
    except AttributeError:
        k = alt
    return k


class GeolyticaResult(OneResult):

    def __init__(self, json_content):
        # create safe shortcuts
        self._standard = json_content.get('standard', {})

        # proceed with super.__init__
        super(GeolyticaResult, self).__init__(json_content)

    @property
    def lat(self):
        lat = _correct_empty_dict(self.raw, 'latt')
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = _correct_empty_dict(self.raw, 'longt')
        if lng:
            return float(lng)

    @property
    def postal(self):
        return _correct_empty_dict(self.raw, 'postal')

    @property
    def housenumber(self):
        return _correct_empty_dict(self._standard, 'stnumber')

    @property
    def street(self):
        return _correct_empty_dict(self._standard, 'staddress')

    @property
    def city(self):
        return _correct_empty_dict(self._standard, 'city')

    @property
    def state(self):
        return _correct_empty_dict(self._standard, 'prov')

    @property
    def address(self):
        if self.street_number:
            return u'{0} {1}, {2}'.format(self.street_number, self.route, self.locality)
        elif self.route and self.route != 'un-known':
            return u'{0}, {1}'.format(self.route, self.locality)
        else:
            return self.locality


class GeolyticaQuery(MultipleResultsQuery):
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

    _URL = 'http://geocoder.ca'
    _RESULT_CLASS = GeolyticaResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        params = {
            'json': 1,
            'locate': location,
            'geoit': 'xml'
        }
        if 'strictmode' in kwargs:
            params.update({'strictmode': kwargs.pop('strictmode')})
        if 'strict' in kwargs:
            params.update({'strict': kwargs.pop('strict')})
        if 'auth' in kwargs:
            params.update({'auth': kwargs.pop('auth')})
        return params

    def _adapt_results(self, json_response):
        return [json_response]

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = GeolyticaQuery('1552 Payette dr., Ottawa')
    g.debug()
