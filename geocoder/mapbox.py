#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import mapbox_access_token
from geocoder.location import Location


class MapboxResult(OneResult):

    def __init__(self, json_content):
        super(MapboxResult, self).__init__(json_content)

        for item in json_content.get('context', []):
            if '.' in item['id']:
                # attribute=country & text=Canada
                attribute = item['id'].split('.')[0]
                self.raw[attribute] = item['text']

    @property
    def lat(self):
        coord = self.raw['geometry']['coordinates']
        if coord:
            return coord[1]

    @property
    def lng(self):
        coord = self.raw['geometry']['coordinates']
        if coord:
            return coord[0]

    @property
    def address(self):
        return self.raw.get('place_name')

    @property
    def housenumber(self):
        return self.raw.get('address')

    @property
    def street(self):
        return ''

    @property
    def city(self):
        return self.raw.get('place')

    @property
    def state(self):
        return self.raw.get('region')

    @property
    def country(self):
        return self.raw.get('country')

    @property
    def postal(self):
        return self.raw.get('postcode')

    @property
    def accuracy(self):
        if self.interpolated:
            return "interpolated"

    @property
    def quality(self):
        return self.raw.get('relevance')

    @property
    def interpolated(self):
        return self.raw['geometry'].get('interpolated')

    @property
    def bbox(self):
        if self.raw.get('bbox'):
            west = self.raw['bbox'][0]
            south = self.raw['bbox'][1]
            east = self.raw['bbox'][2]
            north = self.raw['bbox'][3]
            return self._get_bbox(south, west, north, east)


class MapboxQuery(MultipleResultsQuery):
    """
    Mapbox Geocoding
    ================
    The Mapbox Geocoding API lets you convert location text into
    geographic coordinates (1600 Pennsylvania Ave NW → -77.0366,38.8971).

    API Reference
    -------------
    https://www.mapbox.com/developers/api/geocoding/

    Get Mapbox Access Token
    -----------------------
    https://www.mapbox.com/account
    """
    provider = 'mapbox'
    method = 'geocode'

    _URL = u'https://api.mapbox.com/geocoding/v5/mapbox.places/{0}.json'
    _RESULT_CLASS = MapboxResult
    _KEY = mapbox_access_token

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'access_token': provider_key,
            'country': kwargs.get('country'),
            'proximity': self._get_proximity(**kwargs),
            'types': kwargs.get('types'),
        }

    def _before_initialize(self, location, **kwargs):
        self.url = self.url.format(location)
        self._get_proximity(**kwargs)

    def _get_proximity(self, **kwargs):
        if 'proximity' in kwargs:
            lat, lng = Location(kwargs['proximity']).latlng
            return u'{0},{1}'.format(lng, lat)

    def _adapt_results(self, json_content):
        # extract the array of JSON objects
        return json_content.get('features', [])


if __name__ == '__main__':
    g = MapboxQuery("200 Queen Street", proximity=[45.3, -66.1])
    print(g.address)
    g = MapboxQuery("200 Queen Street")
    print(g.address)
    g.debug()
