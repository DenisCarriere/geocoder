#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.opencage import OpenCageResult, OpenCageQuery
from geocoder.location import Location


class OpenCageReverseResult(OpenCageResult):

    @property
    def ok(self):
        return bool(self.address)


class OpenCageReverse(OpenCageQuery):
    """
    OpenCage Geocoding Services
    ===========================
    OpenCage Geocoder simple, easy, and open geocoding for the entire world
    Our API combines multiple geocoding systems in the background.
    Each is optimized for different parts of the world and types of requests.
    We aggregate the best results from open data sources and algorithms so you don't have to.
    Each is optimized for different parts of the world and types of requests.

    API Reference
    -------------
    https://geocoder.opencagedata.com/api
    """
    provider = 'opencage'
    method = 'reverse'

    _URL = 'http://api.opencagedata.com/geocode/v1/json'
    _RESULT_CLASS = OpenCageReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            'query': location,
            'key': provider_key,
        }

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = OpenCageReverse([45.4049053, -75.7077965])
    g.debug()
