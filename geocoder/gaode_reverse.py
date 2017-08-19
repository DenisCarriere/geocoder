#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import requests

from geocoder.gaode import Gaode
from geocoder.keys import gaode_key
from geocoder.location import Location


class GaodeReverse(Gaode):
    """
    Gaode GeoReverse API
    ===================
    Gaode Maps GeoReverse API is a free open the API, the default quota
    2000 times / day.

    Params
    ------
    :param location: Your search location you want geocoded.
    :param key: Gaode API key.
    :param referer: Gaode API referer website.

    References
    ----------
    API Documentation: http://lbs.amap.com/api/webservice/guide/api/georegeo
    Get Gaode AMap Key: http://lbs.amap.com/dev/
    """
    provider = 'gaode'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://restapi.amap.com/v3/geocode/regeo'
        location = Location(location)
        self._lat = location.lat
        self._lng = location.lng
        location = str(location.lng) + ',' + str(location.lat)
        self.params = {
            'location': location,
            'output': 'json',
            'key': self._get_api_key(gaode_key, **kwargs),
        }
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
            result = self.content['regeocode']
            self._build_tree(result)
            self._exceptions()
            self._catch_errors()
            self._json()
        except Exception as ex:
            pass

    @property
    def lat(self):
        return self._lat

    @property
    def lng(self):
        return self._lng

    @property
    def address(self):
        return self.parse['formatted_address']

    @property
    def country(self):
        return self.parse['addressComponent']['country']

    @property
    def province(self):
        return self.parse['addressComponent']['province']

    @property
    def state(self):
        return self.parse['addressComponent']['province']

    @property
    def city(self):
        if len(self.parse['addressComponent']['city']) == 0:
            return self.parse['addressComponent']['province']
        else:
            return self.parse['addressComponent']['city']

    @property
    def district(self):
        return self.parse['addressComponent']['district']

    @property
    def street(self):
        return self.content['regeocode']['addressComponent']['streetNumber']['street']

    @property
    def adcode(self):
        return self.parse['addressComponent']['adcode']

    @property
    def township(self):
        return self.parse['addressComponent']['township']

    @property
    def towncode(self):
        return self.parse['addressComponent']['towncode']

    @property
    def housenumber(self):
        return self.content['regeocode']['addressComponent']['streetNumber']['number']


if __name__ == '__main__':
    g = GaodeReverse("39.7916548353,116.3671875000")
    g.debug()
