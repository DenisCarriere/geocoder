#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.location import Location
from geocoder.base import OneResult
from geocoder.gaode import GaodeQuery


class GaodeReverseResult(OneResult):

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
        if len(self.raw['addressComponent']['city']) == 0:
            return self.raw['addressComponent']['province']
        else:
            return self.raw['addressComponent']['city']

    @property
    def district(self):
        return self.raw['addressComponent']['district']

    @property
    def street(self):
        return self.raw['addressComponent']['streetNumber']['street']

    @property
    def adcode(self):
        return self.raw['addressComponent']['adcode']

    @property
    def township(self):
        return self.raw['addressComponent']['township']

    @property
    def towncode(self):
        return self.raw['addressComponent']['towncode']

    @property
    def housenumber(self):
        return self.raw['addressComponent']['streetNumber']['number']


class GaodeReverse(GaodeQuery):
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

    _URL = 'http://restapi.amap.com/v3/geocode/regeo'
    _RESULT_CLASS = GaodeReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            'location': str(location.lng) + ',' + str(location.lat),
            'output': 'json',
            'key': provider_key,
        }

    def _adapt_results(self, json_response):
        return [json_response['regeocode']]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = GaodeReverse("39.971577, 116.506142")
    g.debug()
