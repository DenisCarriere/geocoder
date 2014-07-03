#!/usr/bin/python
# coding: utf8

from base import Base
from location import Location
import time


class Timezone(Base):
    name = 'Time Zone Google'
    url = 'https://maps.googleapis.com/maps/api/timezone/json'

    def __init__(self, latlng, timestamp=''):
        self.location = latlng
        self.timestamp = timestamp
        self.json = dict()
        self.params = dict()
        self.lat, self.lng = Location(latlng).latlng
        self.latlng = '{0},{1}'.format(self.lat, self.lng)

        # Parameters for URL request
        self.params['location'] = self.latlng
        self.params['timestamp'] = self.get_timestamp()

    def get_timestamp(self):
        if self.timestamp:
            return self.timestamp
        else:
            return time.time()

    @property
    def status(self):
        return self.safe_format('status')

    @property
    def address(self):
        return self.timezone

    @property
    def timezone_id(self):
        return self.safe_format('timeZoneId')

    @property
    def timezone(self):
        return self.safe_format('timeZoneName')

    @property
    def utc(self):
        return self.safe_format('rawOffset')

    @property
    def dst(self):
        return self.safe_format('dstOffset')

if __name__ == '__main__':
    pass