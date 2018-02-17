#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import mapquest_key

from geocoder.location import BBox


class MapquestResult(OneResult):

    @property
    def lat(self):
        return self.raw.get('latLng', {}).get('lat')

    @property
    def lng(self):
        return self.raw.get('latLng', {}).get('lng')

    @property
    def street(self):
        return self.raw.get('street')

    @property
    def address(self):
        if self.street:
            return self.street
        elif self.city:
            return self.city
        elif self.country:
            return self.country

    @property
    def quality(self):
        return self.raw.get('geocodeQuality')

    @property
    def postal(self):
        return self.raw.get('postalCode')

    @property
    def neighborhood(self):
        return self.raw.get('adminArea6')

    @property
    def city(self):
        return self.raw.get('adminArea5')

    @property
    def county(self):
        return self.raw.get('adminArea4')

    @property
    def state(self):
        return self.raw.get('adminArea3')

    @property
    def country(self):
        return self.raw.get('adminArea1')


class MapquestQuery(MultipleResultsQuery):
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
    method = 'geocode'

    _URL = 'http://www.mapquestapi.com/geocoding/v1/address'
    _RESULT_CLASS = MapquestResult
    _KEY = mapquest_key

    def _build_headers(self, provider_key, **kwargs):
        return {
            'referer': 'http://www.mapquestapi.com/geocoding/',
            'host': 'www.mapquestapi.com',
        }

    def _build_params(self, location, provider_key, **kwargs):
        params = {
            'key': provider_key,
            'location': location,
            'maxResults': kwargs.get("maxRows", 1),
            'outFormat': 'json',
        }

        bbox = kwargs.get('bbox')
        if bbox:
            bbox = BBox(bbox=bbox)
            params['boundingBox'] = u'{north},{west},{south},{east}'.format(
                west=bbox.west,
                east=bbox.east,
                south=bbox.south,
                north=bbox.north
            )

        return params

    def _catch_errors(self, json_response):
        if b'The AppKey submitted with this request is invalid' in json_response:
            self.error = 'MapQuest API Key invalid'

        return self.error

    def _adapt_results(self, json_response):
        results = json_response.get('results', [])
        if results:
            return results[0]['locations']

        return []


if __name__ == '__main__':
    g = MapquestQuery('Ottawa', maxRows=3)
    g.debug()
