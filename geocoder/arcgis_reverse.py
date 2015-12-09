#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.arcgis import Arcgis
from geocoder.location import Location


class ArcgisReverse(Arcgis):
    """
    ArcGIS REST API
    =======================
    The World Geocoding Service finds addresses and places in all supported countries
    from a single endpoint. The service can find point locations of addresses,
    business names, and so on.  The output points can be visualized on a map,
    inserted as stops for a route, or loaded as input for a spatial analysis.
    an address, retrieving imagery metadata, or creating a route.

    API Reference
    -------------
    https://developers.arcgis.com/rest/geocode/api-reference/geocoding-reverse-geocode.htm
    """
    provider = 'arcgis'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode'
        self.location = location
        location = Location(location)
        self.params = {
            'location': '{},{}'.format(location.lng, location.lat),
            'f': 'json'
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        if self.parse['locations']:
            self._build_tree(self.parse['locations'][0])


if __name__ == '__main__':
    g = ArcgisReverse("48.8583, -75.2945")
    g.debug()
