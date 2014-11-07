#!/usr/bin/python
# coding: utf8

from .base import Base
from .location import Location
import time

class Timezone(Base):
    provider = 'timezone'
    api = 'Google Time Zone API'
    url = 'https://maps.googleapis.com/maps/api/timezone/json'

    _description = 'The Time Zone API provides time offset data for locations on the surface of the earth.\n'
    _description += 'Requesting the time zone information for a specific Latitude/Longitude pair will\n'
    _description += 'return the name of that time zone, the time offset from UTC, and the Daylight Savings offset.'
    _api_reference = ['[{0}](https://developers.google.com/maps/documentation/timezone/)'.format(api)]
    _api_parameter = [':param ``location``: (input) can be specified as [lat, lng].']
    _api_parameter = [':param ``timestamp``: (optional) specifies the desired time as seconds']
    _example = ['>>> g = geocoder.timezone(\'<address or [lat,lng]>\')',
                '>>> g.timezone',
                '\'Eastern Daylight Time\'']

    def __init__(self, location, timestamp=''):
        self.location = location
        self.timestamp = timestamp
        g = Location(location)
        self.lat, self.lng = g.lat, g.lng
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['location'] = '{0},{1}'.format(self.lat, self.lng)
        self.params['timestamp'] = self._get_timestamp()

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

    def __repr__(self):
        return "<[{0}] {1} [{2}]>".format(self.status, self.provider, self.timezone)

    def _get_timestamp(self):
        if self.timestamp:
            return self.timestamp
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
    g.help()
    g.debug()