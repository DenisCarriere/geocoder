#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.location import Location
from geocoder.komoot import KomootResult, KomootQuery


class KomootReverseResult(KomootResult):

    @property
    def ok(self):
        return bool(self.address)


class KomootReverse(KomootQuery):
    """
    Komoot REST API
    =======================

    API Reference
    -------------
    http://photon.komoot.de
    """
    provider = 'komoot'
    method = 'reverse'

    _URL = 'https://photon.komoot.de/reverse'
    _RESULT_CLASS = KomootReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            'lat': location.lat,
            'lon': location.lng,
        }


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = KomootReverse("45.4 -75.7")
    g.debug()
