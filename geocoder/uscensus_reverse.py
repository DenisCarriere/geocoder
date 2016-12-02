#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.location import Location
from geocoder.uscensus import USCensus


class USCensusReverse(USCensus, Base):
    """
    US Census Geocoder REST Services
    =======================
    The Census Geocoder is an address look-up tool that converts your address to an approximate coordinate (latitude/longitude) and returns information about the address range that includes the address and the census geography the address is within. The geocoder is available as a web interface and as an API (Representational State Transfer - REST - web-based service).

    API Reference
    -------------
    https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.pdf

    """
    provider = 'uscensus'
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates'
        self.location = location
        location = Location(location)
        self.params = {
            'x': location.longitude,
            'y': location.latitude,
            'benchmark': kwargs.get('benchmark', '4'),
            'vintage': kwargs.get('vintage', '4'),
            'format': 'json'
        }

        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        sets = self.parse['geographies']
        self._build_tree(sets)

    @property
    def ok(self):
        return bool(self.parse['States'])

    @property
    def state(self):
        if self.parse['States']:
            return self.parse['States'][0].get('NAME')

    @property
    def statenumber(self):
        if self.parse['States']:
            return self.parse['States'][0].get('STATE')

    @property
    def county(self):
        if self.parse['Counties']:
            return self.parse['Counties'][0].get('NAME')

    @property
    def countynumber(self):
        if self.parse['Counties']:
            return self.parse['Counties'][0].get('COUNTY')

    @property
    def tract(self):
        if self.parse['Census Tracts']:
            return self.parse['Census Tracts'][0].get('NAME')

    @property
    def tractnumber(self):
        if self.parse['Census Tracts']:
            return self.parse['Census Tracts'][0].get('TRACT')

    @property
    def block(self):
        if self.parse['2010 Census Blocks']:
            return self.parse['2010 Census Blocks'][0].get('NAME')
        elif self.parse['Census Blocks']:
            return self.parse['Census Blocks'][0].get('NAME')

    @property
    def blocknumber(self):
        if self.parse['2010 Census Blocks']:
            return self.parse['2010 Census Blocks'][0].get('BLOCK')
        elif self.parse['Census Blocks']:
            return self.parse['Census Blocks'][0].get('BLOCK')

    @property
    def geoid(self):
        if self.parse['2010 Census Blocks']:
            return self.parse['2010 Census Blocks'][0].get('GEOID')
        elif self.parse['Census Blocks']:
            return self.parse['Census Blocks'][0].get('GEOID')

if __name__ == '__main__':
    g = USCensusReverse([38.846542, -76.92691])
    g.debug()
