#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.osm import Osm
from geocoder.location import Location


class OsmReverse(Osm):
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

    def __init__(self, location, **kwargs):
        self.url = self._get_osm_url(kwargs.get('url', ''))
        self.location = location
        location = Location(location)
        self.params = {
            'q': str(location),
            'format': 'jsonv2',
            'addressdetails': 1,
            'limit': kwargs.get('limit', 1)
        }
        if('lang_code' in kwargs):
            self.params['accept-language'] = kwargs.get('lang_code')
        self._initialize(**kwargs)


if __name__ == '__main__':
    g = OsmReverse("45.3, -75.4")
    g.debug()
