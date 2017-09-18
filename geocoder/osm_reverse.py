#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.osm import OsmQuery
from geocoder.location import Location


class OsmReverse(OsmQuery):
    """
    Nominatim
    =========
    Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
    and address and to generate synthetic addresses of OSM points (reverse geocoding).

    API Reference
    -------------
    http://wiki.openstreetmap.org/wiki/Nominatim
    """
    provider = 'osm'
    method = 'reverse'

    def _build_params(self, location, provider_key, **kwargs):
        params = {
            'q': str(Location(location)),
            'format': 'jsonv2',
            'addressdetails': 1,
            'limit': kwargs.get('limit', 1)
        }
        if('lang_code' in kwargs):
            params['accept-language'] = kwargs.get('lang_code')
        return params


if __name__ == '__main__':
    g = OsmReverse("45.3, -75.4")
    g.debug()
