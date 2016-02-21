#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import time
from geocoder.base import Base
from geocoder.location import Location


class Timezone(Base):
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

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/timezone/json'
        self.location = str(Location(location))
        self.timestamp = kwargs.get('timestamp', time.time())
        self.params = {
            'location': self.location,
            'timestamp': self.timestamp,
        }
        self._initialize(**kwargs)

    def __repr__(self):
        return "<[{0}] {1} [{2}]>".format(self.status, self.provider, self.timeZoneName)

    def _exceptions(self):
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])

    @property
    def ok(self):
        return bool(self.timeZoneName)

    @property
    def timeZoneId(self):
        return self.parse.get('timeZoneId')

    @property
    def timeZoneName(self):
        return self.parse.get('timeZoneName')

    @property
    def rawOffset(self):
        return self.parse.get('rawOffset')

    @property
    def dstOffset(self):
        return self.parse.get('dstOffset')

if __name__ == '__main__':
    g = Timezone([45.5375801, -75.2465979])
    g.debug()
