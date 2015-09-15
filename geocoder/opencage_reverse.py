#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import opencage_key
from geocoder.opencage import OpenCage
from geocoder.location import Location


class OpenCageReverse(OpenCage, Base):
    """
    OpenCage Geocoding Services
    ===========================
    OpenCage Geocoder simple, easy, and open geocoding for the entire world
    Our API combines multiple geocoding systems in the background.
    Each is optimized for different parts of the world and types of requests.
    We aggregate the best results from open data sources and algorithms so you don't have to.
    Each is optimized for different parts of the world and types of requests.

    API Reference
    -------------
    http://geocoder.opencagedata.com/api.html
    """
    provider = 'opencage'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.opencagedata.com/geocode/v1/json'
        self.location = str(Location(location))
        self.params = {
            'query': self.location,
            'key': self._get_api_key(opencage_key, **kwargs),
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.address)

if __name__ == '__main__':
    g = OpenCageReverse([45.4049053, -75.7077965])
    g.debug()
