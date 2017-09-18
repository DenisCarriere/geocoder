#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import baidu_key


class BaiduResult(OneResult):

    @property
    def lat(self):
        return self.raw.get('location', {}).get('lat')

    @property
    def lng(self):
        return self.raw.get('location', {}).get('lng')

    @property
    def quality(self):
        return self.raw.get('level')

    @property
    def confidence(self):
        return self.raw.get('confidence')


class BaiduQuery(MultipleResultsQuery):
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
    method = 'geocode'

    _URL = 'http://api.map.baidu.com/geocoder/v2/'
    _RESULT_CLASS = BaiduResult
    _KEY = baidu_key

    def _build_params(self, location, provider_key, **kwargs):
        coordtype = kwargs.get('coordtype', 'wgs84ll')
        return {
            'address': location,
            'output': 'json',
            'ret_coordtype': coordtype,
            'ak': provider_key,
        }

    def _build_headers(self, provider_key, **kwargs):
        return {'Referer': kwargs.get('referer', 'http://developer.baidu.com')}

    def _adapt_results(self, json_response):
        return [json_response['result']]

    def _catch_errors(self, json_response):
        status_code = json_response.get('status')
        if status_code != 200:
            self.status_code = status_code
            self.error = json_response.get('message')

        return self.error


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = BaiduQuery('将台路', key='')
    g.debug()
