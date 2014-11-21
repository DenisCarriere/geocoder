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

    """
    provider = 'google'
    method = 'timezone'

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/timezone/json'
        self.location = Location(location).latlng
        self.timestamp = kwargs.get('timestamp', '')
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'location': self.location,
            'timestamp': self._get_timestamp(self.timestamp),
        }
        self._initialize(**kwargs)

    def __repr__(self):
        return "<[{0}] {1} [{2}]>".format(self.status, self.provider, self.timezone)

    def _get_timestamp(self, timestamp):
        if timestamp:
            return timestamp
        else:
            return time.time()

    @property
    def ok(self):
        return bool(self.timezone)

    @property
    def status_description(self):
        return self._get_json_str('status')

    @property
    def timezone_id(self):
        return self._get_json_str('timeZoneId')

    @property
    def timezone(self):
        return self._get_json_str('timeZoneName')

    @property
    def utc(self):
        return self._get_json_str('rawOffset')

    @property
    def dst(self):
        return self._get_json_str('dstOffset')

if __name__ == '__main__':
    g = Timezone([45.5375801, -75.2465979])
    g.debug()