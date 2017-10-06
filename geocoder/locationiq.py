#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging
import json

from geocoder.osm import OsmResult, OsmQuery
from geocoder.keys import locationiq_key


class LocationIQResult(OsmResult):
    pass


class LocationIQQuery(OsmQuery):
    provider = 'locationiq'
    method = 'geocode'

    _URL = 'https://locationiq.org/v1/search.php'
    _RESULT_CLASS = LocationIQResult
    _KEY = locationiq_key
    _KEY_MANDATORY = True

    def _build_params(self, location, provider_key, **kwargs):
        if 'limit' in kwargs:
            kwargs['maxRows'] = kwargs['limit']
        return {
            'key': provider_key,
            'q': location,
            'format': 'json',
            'addressdetails': 1,
            'limit': kwargs.get('maxRows', 1),
        }


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = LocationIQQuery('Ottawa, Ontario')
    g.debug()
    g = LocationIQQuery('Ottawa, Ontario', maxRows=5)
    print(json.dumps(g.geojson, indent=4))
