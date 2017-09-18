#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.location import Location
from geocoder.base import OneResult
from geocoder.baidu import BaiduQuery


class BaiduReverseResult(OneResult):
    @property
    def ok(self):
        return bool(self.address)

    @property
    def address(self):
        return self.raw['formatted_address']

    @property
    def country(self):
        return self.raw['addressComponent']['country']

    @property
    def province(self):
        return self.raw['addressComponent']['province']

    @property
    def state(self):
        return self.raw['addressComponent']['province']

    @property
    def city(self):
        return self.raw['addressComponent']['city']

    @property
    def district(self):
        return self.raw['addressComponent']['district']

    @property
    def street(self):
        return self.raw['addressComponent']['street']

    @property
    def housenumber(self):
        return self.raw['addressComponent']['street_number']


class BaiduReverse(BaiduQuery):
    """
    Baidu Geocoding API
    ===================
    Baidu Maps Geocoding API is a free open the API, the default quota
    one million times / day.

    Params
    ------
    :param location: Your search location you want geocoded.
    :param key: Baidu API key.
    :param referer: Baidu API referer website.

    References
    ----------
    API Documentation: http://developer.baidu.com/map
    Get Baidu Key: http://lbsyun.baidu.com/apiconsole/key
    """
    provider = 'baidu'
    method = 'reverse'

    _URL = 'http://api.map.baidu.com/geocoder/v2/'
    _RESULT_CLASS = BaiduReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        params = {
            'location': str(location),
            'ret_coordtype': kwargs.get('coordtype', 'wgs84ll'),
            'output': 'json',
            'ak': provider_key
        }
        if ('lang_code' in kwargs):
            params['accept-language'] = kwargs['lang_code']

        return params


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = BaiduReverse("39.983424,116.32298", key='')
    g.debug()
