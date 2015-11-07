#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.arcgis import Arcgis
from geocoder.location import Location

class ArcgisReverse(Base):
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
    https://developers.arcgis.com/rest/geocode/api-reference/geocoding-find.htm
    """
    provider = 'arcgis'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        t = location.split()
        print t[0] + " " + t[1]
        self.location = str(Location(location))
        self.url = 'http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode'
        self.params = {
            'location': t[1]+","+t[0],		# ArcGIS needs it reversed from the norm
            'f': 'json'
        }

        self._initialize(**kwargs)

    def _exceptions(self):
        if self.parse['locations']:
            self._build_tree(self.parse['locations'][0])

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
    def country(self):
        return self.parse['address'].get('CountryCode')

    @property
    def postal(self):
        return self.parse['address'].get('Postal')

    @property
    def state(self):
        return self.parse['address'].get('Region')

if __name__ == '__main__':
    g = ArcgisReverse("48.8583 2.2945")
    print g
