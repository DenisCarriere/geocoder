#!/usr/bin/python
# coding: utf8

import time
from .base import Base
from .location import Location


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

    Attributes
    ----------
    [x] location
    [x] ok
    [x] provider
    [x] status
    [x] status_description
    [x] timestamp
    [x] timezone
    [x] timezone_id
    [x] utc
    """
    provider = 'google'
    method = 'timezone'

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/timezone/json'
        self.location = Location(location).latlng
        self.timestamp = kwargs.get('timestamp', time.time())
        self.params = {
            'location': self.location,
            'timestamp': self.timestamp,
        }
        self._initialize(**kwargs)

    def __repr__(self):
        return "<[{0}] {1} [{2}]>".format(self.status, self.provider, self.timeZoneName)

    def _exceptions(self):
        # Build intial Tree with results
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