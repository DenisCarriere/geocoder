#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

from geocoder.baidu import Baidu
from geocoder.keys import baidu_key
from geocoder.location import Location


class BaiduReverse(Baidu):
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

    def __init__(self, location, **kwargs):
        self.url = 'http://api.map.baidu.com/geocoder/v2/'
        self.location = location
        location = Location(location)
        coordtype = 'wgs84ll'
        if 'coordtype' in kwargs:
            coordtype = kwargs['coordtype']
        self.params = {
            'location': str(location),
            'coordtype': coordtype,
            'output': 'json',
            'ak': self._get_api_key(baidu_key, **kwargs),
        }
        if ('lang_code' in kwargs):
            self.params['accept-language'] = kwargs.get('lang_code')
        self._initialize(**kwargs)

    @property
    def country(self):
        return self.parse['addressComponent']['country']

    @property
    def province(self):
        return self.parse['addressComponent']['province']

    @property
    def state(self):
        return self.parse['addressComponent']['state']

    @property
    def city(self):
        return self.parse['addressComponent']['city']


    @property
    def district(self):
        return self.parse['addressComponent']['district']

    @property
    def street(self):
        return self.parse['addressComponent']['street']

    @property
    def housenumber(self):
        return self.parse['addressComponent']['street_number']

if __name__ == '__main__':
    g = BaiduReverse("39.983424,116.32298")
    g.debug()
