#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.location import BBox
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import tomtom_key


class TomtomResult(OneResult):

    def __init__(self, json_content):
        self._address = json_content['address']
        super(TomtomResult, self).__init__(json_content)

    @property
    def lat(self):
        return self.raw.get('position', {}).get('lat')

    @property
    def lng(self):
        return self.raw.get('position', {}).get('lon')

    @property
    def geohash(self):
        return self.raw.get('id')

    @property
    def quality(self):
        return self.raw.get('type')

    @property
    def bbox(self):
        viewport = self.raw.get('viewport', {})
        if viewport:
            bbox = {
                'south': viewport.get('btmRightPoint')['lon'],
                'west': viewport.get('btmRightPoint')['lat'],
                'north': viewport.get('topLeftPoint')['lon'],
                'east': viewport.get('topLeftPoint')['lat'],
            }
            return BBox.factory(bbox).as_dict

    @property
    def address(self):
        return self._address.get('freeformAddress')

    @property
    def housenumber(self):
        return self._address.get('streetNumber')

    @property
    def street(self):
        return self._address.get('streetName')

    @property
    def road(self):
        return self.street

    @property
    def city(self):
        return self._address.get('municipality')

    @property
    def state(self):
        return self._address.get('countrySubdivisionName', self._address.get('countrySubdivision'))

    @property
    def country(self):
        return self._address.get('countryCode')

    @property
    def postal(self):
        return self._address.get('postalCode')


class TomtomQuery(MultipleResultsQuery):
    """
    Geocoding API
    =============
    The Geocoding API gives developers access to TomTom’s first class geocoding service.
    Developers may call this service through either a single or batch geocoding request.
    This service supports global coverage, with house number level matching in over 50 countries,
    and address point matching where available.

    API Reference
    -------------
    https://developer.tomtom.com/tomtom-maps-apis-developers
    """
    provider = 'tomtom'
    method = 'geocode'

    _URL = 'https://api.tomtom.com/search/2/geocode/{0}.json'
    _RESULT_CLASS = TomtomResult
    _KEY = tomtom_key

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'key': provider_key,
            'limit': kwargs.get('maxRows', 1),
            'countrySet': kwargs.get('countrySet'),
            'lon': kwargs.get('lon'),
            'lat': kwargs.get('lat'),
            'radius': kwargs.get('radius')
        }

    def _before_initialize(self, location, **kwargs):
        self.url = self.url.format(location)

    def _adapt_results(self, json_response):
        return json_response['results']

    def _catch_errors(self, json_response):
        if 'Developer Inactive' in str(json_response):
            self.error = 'API Key not valid'
            self.status_code = 401

        return self.error


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = TomtomQuery('1552 Payette dr., Ottawa')
    g.debug()
