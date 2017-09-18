#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import google_key
from geocoder.location import Location


class ElevationResult(OneResult):

    @property
    def status(self):
        if self.elevation:
            return 'OK'
        else:
            return 'ERROR - No Elevation found'

    @property
    def ok(self):
        return bool(self.elevation)

    @property
    def meters(self):
        if self.elevation:
            return round(self.elevation, 1)

    @property
    def feet(self):
        if self.elevation:
            return round(self.elevation * 3.28084, 1)

    @property
    def elevation(self):
        return self.raw.get('elevation')

    @property
    def resolution(self):
        return self.raw.get('resolution')


class ElevationQuery(MultipleResultsQuery):
    """
    Google Elevation API
    ====================
    The Elevation API provides elevation data for all locations on the surface of the
    earth, including depth locations on the ocean floor (which return negative values).
    In those cases where Google does not possess exact elevation measurements at the
    precise location you request, the service will interpolate and return an averaged
    value using the four nearest locations.

    API Reference
    -------------
    https://developers.google.com/maps/documentation/elevation/
    """
    provider = 'google'
    method = 'elevation'

    _URL = 'https://maps.googleapis.com/maps/api/elevation/json'
    _RESULT_CLASS = ElevationResult
    _KEY = google_key

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'locations': str(Location(location)),
        }

    def _adapt_results(self, json_response):
        return json_response['results']


if __name__ == '__main__':
    g = ElevationQuery([45.123, -76.123])
    g.debug()
