#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

from collections import OrderedDict
import logging
import re
import six

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import baidu_key, baidu_security_key


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
        params = {
            'address': re.sub('[ ,]', '%', location),
            'output': 'json',
            'ret_coordtype': coordtype,
            'ak': provider_key,
        }

        # adapt params to authentication method
        self.security_key = kwargs.get('sk', baidu_security_key)
        if self.security_key:
            return self._encode_params(params)
        else:
            return params

    def _encode_params(self, params):
        # maintain the order of the parameters during signature creation when returning the results
        # signature is added to the end of the parameters
        ordered_params = sorted([(k, v)
                                 for (k, v) in params.items() if v])

        params = OrderedDict(ordered_params)

        # urlencode with Chinese symbols sabotage the query
        params['sn'] = self._sign_url(
            '/geocoder/v2/',
            params,
            self.security_key
        )

        return params

    def _sign_url(self, base_url, params, security_key):
        """
        Signs a request url with a security key.
        """
        import hashlib

        if six.PY3:
            from urllib.parse import urlencode, quote, quote_plus
        else:
            from urllib import urlencode, quote, quote_plus

        if not base_url or not self.security_key:
            return None

        params = params.copy()
        address = params.pop('address')

        url = base_url + '?address=' + address + '&' + urlencode(params)
        encoded_url = quote(url, safe="/:=&?#+!$,;'@()*[]")

        signature = quote_plus(encoded_url + self.security_key).encode('utf-8')
        encoded_signature = hashlib.md5(signature).hexdigest()

        return encoded_signature

    def _build_headers(self, provider_key, **kwargs):
        return {'Referer': kwargs.get('referer', 'http://developer.baidu.com')}

    def _adapt_results(self, json_response):
        return [json_response['result']]

    def _catch_errors(self, json_response):
        status_code = json_response.get('status')
        if status_code != 0:
            self.status_code = status_code
            self.error = json_response.get('message')

        return self.error


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = BaiduQuery('将台路', key='')
    g.debug()
