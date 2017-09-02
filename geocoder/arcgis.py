#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging
import json

from geocoder.base import OneResult, MultipleResultsQuery


class ArcgisResult(OneResult):

    @property
    def address(self):
        return self.raw.get('name', '')

    @property
    def lat(self):
        return self.raw['feature']['geometry'].get('y')

    @property
    def lng(self):
        return self.raw['feature']['geometry'].get('x')

    @property
    def score(self):
        return self.raw['feature']['attributes'].get('Score', '')

    @property
    def quality(self):
        return self.raw['feature']['attributes'].get('Addr_Type', '')

    @property
    def bbox(self):
        if self.raw['extent']:
            south = self.raw['extent'].get('ymin')
            west = self.raw['extent'].get('xmin')
            north = self.raw['extent'].get('ymax')
            east = self.raw['extent'].get('xmax')
            return self._get_bbox(south, west, north, east)


class ArcgisQuery(MultipleResultsQuery):
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
    method = 'geocode'

    _URL = 'https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find'
    _RESULT_CLASS = ArcgisResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        # backward compatitibility for 'limit' (now maxRows)
        if 'limit' in kwargs:
            logging.warning(
                "argument 'limit' in OSM is deprecated and should be replaced with maxRows")
            kwargs['maxRows'] = kwargs['limit']
        # build params
        return {
            'f': 'json',
            'text': location,
            'maxLocations': kwargs.get('maxRows', 1),
        }

    def _adapt_results(self, json_response):
        return json_response['locations']


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = ArcgisQuery('Toronto')
    g.debug()
    g = ArcgisQuery('Ottawa, Ontario', maxRows=5)
    print(json.dumps(g.geojson, indent=4))
    print([result.address for result in g][:3])
