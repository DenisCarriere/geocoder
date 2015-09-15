#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import baidu_key


class Baidu(Base):
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

    def __init__(self, location, **kwargs):
        self.url = 'http://api.map.baidu.com/geocoder/v2/'
        self.location = location
        self.params = {
            'address': location,
            'output': 'json',
            'ak': self._get_api_key(baidu_key, **kwargs),
        }
        self.headers = {'Referer': kwargs.get('referer', 'http://developer.baidu.com')}
        self._initialize(**kwargs)

    @property
    def lat(self):
        return self.parse['location'].get('lat')

    @property
    def lng(self):
        return self.parse['location'].get('lng')

    @property
    def quality(self):
        return self.parse['result'].get('level')

    @property
    def accuracy(self):
        return self.parse['result'].get('confidence')

if __name__ == '__main__':
    g = Baidu('中国')
    g.debug()
