#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import json
import logging

from geocoder.base import MultipleResultsQuery, OneResult
from geocoder.keys import geonames_username
from geocoder.location import BBox

LOGGER = logging.getLogger(__name__)


class GeonamesResult(OneResult):

    @property
    def lat(self):
        return self.raw.get('lat')

    @property
    def lng(self):
        return self.raw.get('lng')

    @property
    def geonames_id(self):
        return self.raw.get('geonameId')

    @property
    def address(self):
        return self.raw.get('name')

    @property
    def feature_class(self):
        return self.raw.get('fcl')

    @property
    def class_description(self):
        return self.raw.get('fclName')

    @property
    def code(self):
        return self.raw.get('fcode')

    @property
    def description(self):
        return self.raw.get('fcodeName')

    @property
    def state(self):
        return self.raw.get('adminName1')

    @property
    def state_code(self):
        return self.raw.get('adminCode1')

    @property
    def country(self):
        return self.raw.get('countryName')

    @property
    def country_code(self):
        return self.raw.get('countryCode')

    @property
    def population(self):
        return self.raw.get('population')


class GeonamesQuery(MultipleResultsQuery):
    """
    GeoNames REST Web Services
    ==========================
    GeoNames is mainly using REST webservices. Find nearby postal codes / reverse geocoding
    This service comes in two flavors.You can either pass the lat/long or a postalcode/placename.

    API Reference
    -------------
    http://www.geonames.org/export/web-services.html
    """
    provider = 'geonames'
    method = 'geocode'

    _URL = 'http://api.geonames.org/searchJSON'
    _RESULT_CLASS = GeonamesResult
    _KEY = geonames_username

    def _build_params(self, location, provider_key, **kwargs):
        """Will be overridden according to the targetted web service"""
        base_kwargs = {
            'q': location,
            'fuzzy': kwargs.get('fuzzy', 1.0),
            'username': provider_key,
            'maxRows': kwargs.get('maxRows', 1),
        }
        # check out for bbox in kwargs
        bbox = kwargs.pop('proximity', None)
        if bbox is not None:
            bbox = BBox.factory(bbox)
            base_kwargs.update(
                {'east': bbox.east, 'west': bbox.west,
                 'north': bbox.north, 'south': bbox.south})

        # look out for valid extra kwargs
        supported_kwargs = set((
            'name', 'name_equals', 'name_startsWith', 'startRow',
            'country', 'countryBias', 'continentCode',
            'adminCode1', 'adminCode2', 'adminCode3', 'cities',
            'featureClass', 'featureCode',
            'lang', 'type', 'style',
            'isNameRequired', 'tag', 'operator', 'charset',
            'east', 'west', 'north', 'south',
            'orderby', 'inclBbox',
        ))
        found_kwargs = supported_kwargs & set(kwargs.keys())
        LOGGER.debug("Adding extra kwargs %s", found_kwargs)

        # update base kwargs with extra ones
        base_kwargs.update(dict(
            [(extra, kwargs[extra]) for extra in found_kwargs]
        ))
        return base_kwargs

    def _catch_errors(self, json_response):
        """ Changed: removed check on number of elements:
            - totalResultsCount not sytematically returned (e.g in hierarchy)
            - done in base.py
        """
        status = json_response.get('status')
        if status:
            message = status.get('message')
            value = status.get('value')
            custom_messages = {
                10: 'Invalid credentials',
                18: 'Do not use the demo account for your application',
            }
            self.error = custom_messages.get(value, message)
            LOGGER.error("Error %s from JSON %s", self.error, json_response)

        return self.error

    def _adapt_results(self, json_response):
        # extract the array of JSON objects
        return json_response['geonames']


if __name__ == '__main__':
    g = GeonamesQuery('Ottawa, Ontario', maxRows=1)
    print(json.dumps(g.geojson, indent=4))
    g.debug()
