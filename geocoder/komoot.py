#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.location import BBox
from geocoder.base import OneResult, MultipleResultsQuery


class KomootResult(OneResult):

    def __init__(self, json_content):
        # create safe shortcuts
        self._geometry = json_content.get('geometry', {})
        self._properties = json_content.get('properties', {})

        # proceed with super.__init__
        super(KomootResult, self).__init__(json_content)

    @property
    def lat(self):
        return self._geometry['coordinates'][1]

    @property
    def lng(self):
        return self._geometry['coordinates'][0]

    @property
    def bbox(self):
        extent = self._properties.get('extent')
        if extent and all(extent):
            west = extent[0]
            north = extent[1]
            east = extent[2]
            south = extent[3]
            return BBox.factory([south, west, north, east]).as_dict

    @property
    def address(self):
        # Ontario, Canada
        address = ', '.join([self.state, self.country])

        # 453 Booth street, Ottawa ON, Canada
        if self.housenumber:
            middle = ', '.join([self.street, self.city])
            address = ' '.join([self.housenumber, middle, address])

        # 453 Booth street, Ottawa ON, Canada
        elif self.street:
            middle = ', '.join([self.street, self.city])
            address = ' '.join([middle, address])

        # Ottawa ON, Canada
        elif self.city:
            address = ' '.join([self.city, address])

        return address

    @property
    def country(self):
        return self._properties.get('country', '')

    @property
    def state(self):
        if self.osm_value == 'state':
            return self._properties.get('name', '')
        return self._properties.get('state', '')

    @property
    def city(self):
        if self.osm_value == 'city':
            return self._properties.get('name', '')
        return self._properties.get('city', '')

    @property
    def street(self):
        return self._properties.get('street', '')

    @property
    def housenumber(self):
        return self._properties.get('housenumber', '')

    @property
    def postal(self):
        return self._properties.get('postcode', '')

    @property
    def osm_id(self):
        return self._properties.get('osm_id', '')

    @property
    def osm_value(self):
        return self._properties.get('osm_value', '')

    @property
    def osm_key(self):
        return self._properties.get('osm_key', '')

    @property
    def osm_type(self):
        return self._properties.get('osm_type', '')


class KomootQuery(MultipleResultsQuery):
    """
    Komoot REST API
    =======================

    API Reference
    -------------
    http://photon.komoot.de
    """
    provider = 'komoot'
    method = 'geocode'

    _URL = 'http://photon.komoot.de/api'
    _RESULT_CLASS = KomootResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'q': location,
            'limit': kwargs.get('maxRows', 1),
            'lang': 'en',
        }

    def _adapt_results(self, json_response):
        return json_response['features']


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = KomootQuery('Ottawa Ontario', maxRows=3)
    g.debug()
