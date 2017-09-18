#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import gaode_key


class GaodeResult(OneResult):

    @property
    def lat(self):
        return float(self.raw.get('location', '0,0').replace("'", '').split(',')[1])

    @property
    def lng(self):
        return float(self.raw.get('location', '0,0').replace("'", '').split(',')[0])

    @property
    def quality(self):
        return self.raw.get('level')

    @property
    def address(self):
        return self.raw.get('formatted_address')

    @property
    def country(self):
        return '中国'

    @property
    def province(self):
        return self.raw.get('province')

    @property
    def state(self):
        return self.raw.get('province')

    @property
    def city(self):
        return self.raw.get('city')

    @property
    def district(self):
        return self.raw.get('district')

    @property
    def street(self):
        return self.raw.get('street')

    @property
    def adcode(self):
        return self.raw.get('adcode')

    @property
    def housenumber(self):
        return self.raw.get('number')


class GaodeQuery(MultipleResultsQuery):
    """
    Gaode AMap Geocoding API
    ===================
    Gaode Maps Geocoding API is a free open the API, the default quota
    2000 times / day.

    Params
    ------
    :param location: Your search location you want geocoded.
    :param key: Gaode API key.

    References
    ----------
    API Documentation: http://lbs.amap.com/api/webservice/guide/api/georegeo
    Get AMap Key: http://lbs.amap.com/dev/
    """
    provider = 'gaode'
    method = 'geocode'

    _URL = 'http://restapi.amap.com/v3/geocode/geo'
    _RESULT_CLASS = GaodeResult
    _KEY = gaode_key

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'address': location,
            'output': 'JSON',
            'key': provider_key,
        }

    def _build_headers(self, provider_key, **kwargs):
        return {'Referer': kwargs.get('referer', '')}

    def _adapt_results(self, json_response):
        return json_response['geocodes']


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = GaodeQuery('将台路')
    g.debug()
