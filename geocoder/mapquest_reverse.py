#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.keys import mapquest_key
from geocoder.mapquest import Mapquest
from geocoder.location import Location


class MapquestReverse(Mapquest):
    """
    MapQuest
    ========
    The geocoding service enables you to take an address and get the
    associated latitude and longitude. You can also use any latitude
    and longitude pair and get the associated address. Three types of
    geocoding are offered: address, reverse, and batch.

    API Reference
    -------------
    http://www.mapquestapi.com/geocoding/

    """
    provider = 'mapquest'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://www.mapquestapi.com/geocoding/v1/address'
        self.location = str(Location(location))
        self.headers = {
            'referer': 'http://www.mapquestapi.com/geocoding/',
            'host': 'www.mapquestapi.com',
        }
        self.params = {
            'key': self._get_api_key(mapquest_key, **kwargs),
            'location': self.location,
            'maxResults': 1,
            'outFormat': 'json',
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.quality)

if __name__ == '__main__':
    g = MapquestReverse([45.50, -76.05])
    g.debug()
