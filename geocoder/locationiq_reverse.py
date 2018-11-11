#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

from geocoder.location import Location
from geocoder.locationiq import LocationIQQuery


class LocationIQReverse(LocationIQQuery):
    provider = 'locationiq'
    method = 'reverse'

    _URL = 'https://locationiq.org/v1/reverse.php'

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            'format': 'json',
            'key': provider_key,
            'lat': location.latitude,
            'lon': location.longitude,
        }

    def _adapt_results(self, json_response):
        return [json_response]


if __name__ == '__main__':
    g = LocationIQReverse("45.421106, -75.690308")
    g.debug()
