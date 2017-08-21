#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import time
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import google_key
from geocoder.location import Location


class TimezoneResult(OneResult):

    def __repr__(self):
        return u'<[{}] [{}]>'.format(self.status, self.timeZoneName)

    @property
    def ok(self):
        return bool(self.timeZoneName)

    @property
    def timeZoneId(self):
        return self.raw.get('timeZoneId')

    @property
    def timeZoneName(self):
        return self.raw.get('timeZoneName')

    @property
    def rawOffset(self):
        return self.raw.get('rawOffset')

    @property
    def dstOffset(self):
        return self.raw.get('dstOffset')


class TimezoneQuery(MultipleResultsQuery):
    """
    Google Time Zone API
    ====================
    The Time Zone API provides time offset data for locations on the surface of the earth.
    Requesting the time zone information for a specific Latitude/Longitude pair will
    return the name of that time zone, the time offset from UTC, and the Daylight Savings offset.

    API Reference
    -------------
    https://developers.google.com/maps/documentation/timezone/
    """
    provider = 'google'
    method = 'timezone'

    _URL = 'https://maps.googleapis.com/maps/api/timezone/json'
    _RESULT_CLASS = TimezoneResult
    _KEY = google_key

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'location': str(Location(location)),
            'timestamp': kwargs.get('timestamp', time.time()),
        }

    def _adapt_results(self, json_response):
        return [json_response]


if __name__ == '__main__':
    g = TimezoneQuery([45.5375801, -75.2465979])
    g.debug()
