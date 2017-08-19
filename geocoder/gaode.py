#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import requests

from geocoder.base import Base
from geocoder.keys import gaode_key


class Gaode(Base):
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

    def __init__(self, location, **kwargs):
        self.url = 'http://restapi.amap.com/v3/geocode/geo'
        self.location = location
        self.params = {
            'address': location,
            'output': 'JSON',
            'key': self._get_api_key(gaode_key, **kwargs),
        }
        self.headers = {'Referer': kwargs.get('referer', '')}
        self._initialize(**kwargs)

    def _initialize(self, **kwargs):
        # Remove extra URL from kwargs
        if 'url' in kwargs:
            kwargs.pop('url')
        self.json = {}
        self.parse = self.tree()
        self.content = None
        self.encoding = kwargs.get('encoding', 'utf-8')
        self.session = kwargs.get('session', requests.Session())
        self._connect(url=self.url, **kwargs)
        ###
        try:
            for result in self.content['geocodes']:  # Convert to iterator in each of the search tools
                self._build_tree(result)
                self._exceptions()
                self._catch_errors()
                self._json()
        except:
            self._build_tree(self.content)
            self._exceptions()
            self._catch_errors()
            self._json()

    @property
    def lat(self):
        return float(self.parse['location'].replace("'", '').split(',')[1])

    @property
    def lng(self):
        return float(self.parse['location'].replace("'", '').split(',')[0])

    @property
    def quality(self):
        return self.parse['level']

    @property
    def address(self):
        return self.parse['formatted_address']

    @property
    def country(self):
        return '中国'

    @property
    def province(self):
        return self.parse['province']

    @property
    def state(self):
        return self.parse['province']

    @property
    def city(self):
        return self.parse['city']

    @property
    def district(self):
        return self.parse['district']

    @property
    def street(self):
        return self.parse['street']

    @property
    def adcode(self):
        return self.parse['adcode']

    @property
    def housenumber(self):
        return self.parse['number']


if __name__ == '__main__':
    g = Gaode('纽约')
    g.debug()
