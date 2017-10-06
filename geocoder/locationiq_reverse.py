#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.locationiq import LocationIQQuery
from geocoder.location import Location


class LocationIQReverse(LocationIQQuery):
    """
    Nominatim
    =========
    Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
    and address and to generate synthetic addresses of OSM points (reverse geocoding).

    API Reference
    -------------
    http://wiki.openstreetmap.org/wiki/Nominatim
    """
    provider = 'locationiq'
    method = 'reverse'

    def _build_params(self, location, provider_key, **kwargs):
        params = {
            'key': provider_key,
            'q': str(Location(location)),
            'format': 'json',
            'addressdetails': 1,
            'limit': kwargs.get('limit', 1)
        }
        if('lang_code' in kwargs):
            params['accept-language'] = kwargs.get('lang_code')
        return params


if __name__ == '__main__':
    g = LocationIQReverse("45.3, -75.4")
    g.debug()
