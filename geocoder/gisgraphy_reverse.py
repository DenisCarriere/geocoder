#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.location import Location
from geocoder.gisgraphy import GisgraphyResult, GisgraphyQuery


class GisgraphyReverseResult(GisgraphyResult):

    @property
    def ok(self):
        return bool(self.address)


class GisgraphyReverse(GisgraphyQuery):
    """
    Gisgraphy REST API
    =======================

    API Reference
    -------------
    http://www.gisgraphy.com/documentation/user-guide.php
    """
    provider = 'gisgraphy'
    method = 'reverse'

    _URL = 'https://services.gisgraphy.com/reversegeocoding/'
    _RESULT_CLASS = GisgraphyReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            'lat': location.lat,
            'lng': location.lng,
            'format': 'json',
        }


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = GisgraphyReverse("45.4 -75.7")
    g.debug()
