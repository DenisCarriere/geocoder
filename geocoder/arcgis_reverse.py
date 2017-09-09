#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult
from geocoder.arcgis import ArcgisQuery
from geocoder.location import Location


class ArcgisReverseResult(OneResult):

    @property
    def ok(self):
        return bool(self.address)

    @property
    def lat(self):
        return self.raw['location'].get('y')

    @property
    def lng(self):
        return self.raw['location'].get('x')

    @property
    def address(self):
        return self.raw['address'].get('Match_addr')

    @property
    def city(self):
        return self.raw['address'].get('City')

    @property
    def neighborhood(self):
        return self.raw['address'].get('Neighbourhood')

    @property
    def region(self):
        return self.raw['address'].get('Region')

    @property
    def country(self):
        return self.raw['address'].get('CountryCode')

    @property
    def postal(self):
        return self.raw['address'].get('Postal')

    @property
    def state(self):
        return self.raw['address'].get('Region')


class ArcgisReverse(ArcgisQuery):
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

    _URL = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode'
    _RESULT_CLASS = ArcgisReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            'location': u'{}, {}'.format(location.lng, location.lat),
            'f': 'pjson',
            'distance': kwargs.get('distance', 50000),
            'outSR': kwargs.get('outSR', '')
        }

    def _adapt_results(self, json_response):
        return [json_response]

    def _catch_errors(self, json_response):
        error = json_response.get('error', None)
        if error:
            self.error = error['message']

        return self.error


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = ArcgisReverse("45.404702, -75.704150")
    g.debug()
