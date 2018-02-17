#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.mapquest import MapquestResult, MapquestQuery
from geocoder.location import Location


class MapQuestReverseResult(MapquestResult):

    @property
    def ok(self):
        return bool(self.quality)


class MapquestReverse(MapquestQuery):
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

    _URL = 'http://www.mapquestapi.com/geocoding/v1/reverse'

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'key': provider_key,
            'location': str(Location(location)),
            'maxResults': 1,
            'outFormat': 'json',
        }


if __name__ == '__main__':
    g = MapquestReverse([45.50, -76.05])
    g.debug()
