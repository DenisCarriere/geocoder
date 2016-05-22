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
        self.url = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode'
        self.location = location
        location = Location(location)
        self.params = {
            'location': '{}, {}'.format(location.lng, location.lat),
            'f': 'pjson',
            'distance': kwargs.get('distance', 50000),
            'outSR': kwargs.get('outSR', ''),
            'maxLocations': kwargs.get('limit', 1),
        }
        self._initialize(**kwargs)

    def _catch_errors(self):
        error = self.parse['error']
        if error:
            self.error = error['message']

    @property
    def ok(self):
        return bool(self.address)

    @property
    def lat(self):
        return self.parse['location'].get('y')

    @property
    def lng(self):
        return self.parse['location'].get('x')

    @property
    def address(self):
        return self.parse['address'].get('Match_addr')

    @property
    def city(self):
        return self.parse['address'].get('City')

    @property
    def neighborhood(self):
        return self.parse['address'].get('Neighbourhood')

    @property
    def region(self):
        return self.parse['address'].get('Region')

    @property
    def country(self):
        return self.parse['address'].get('CountryCode')

    @property
    def postal(self):
        return self.parse['address'].get('Postal')

    @property
    def state(self):
        return self.parse['address'].get('Region')

    def _exceptions(self):
        self._build_tree(self.content)


if __name__ == '__main__':
    g = ArcgisReverse("45.404702, -75.704150")
    g.debug()
