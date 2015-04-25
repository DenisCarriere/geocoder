#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import re
from geocoder.base import Base


class Ottawa(Base):
    """
    Ottawa ArcGIS REST Services
    ===========================
    Geocoding is the process of assigning a location, usually in the form of
    coordinate values (points), to an address by comparing the descriptive
    location elements in the address to those present in the reference
    material. Addresses come in many forms, ranging from the common address
    format of a house number followed by the street name and succeeding
    information to other location descriptions such as postal zone or census
    tract. An address includes any type of information that distinguishes
    a place.

    API Reference
    -------------
    http://maps.ottawa.ca/ArcGIS/rest/services/
           compositeLocator/GeocodeServer/findAddressCandidates
    """
    provider = 'ottawa'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://maps.ottawa.ca/ArcGIS/rest/services/'
        self.url += 'compositeLocator/GeocodeServer/findAddressCandidates'
        self.location = location
        self.params = {
            'SingleLine': location.replace(', Ottawa, ON', ''),
            'f': 'json',
            'outSR': 4326,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['candidates']:
            self._build_tree(self.parse['candidates'][0])

    @property
    def lat(self):
        return self.parse['location'].get('y')

    @property
    def lng(self):
        return self.parse['location'].get('x')

    @property
    def postal(self):
        if self.address:
            expression = r'([ABCEGHJKLMNPRSTVXY]{1}\d{1}[A-Z]{1}( *\d{1}[A-Z]{1}\d{1})?)'
            pattern = re.compile(expression)
            match = pattern.search(self.address.upper())
            if match:
                return match.group(0)

    @property
    def housenumber(self):
        if self.address:
            expression = r'\d+'
            pattern = re.compile(expression)
            match = pattern.search(self.address)
            if match:
                return int(match.group(0))

    @property
    def city(self):
        return 'Ottawa'

    @property
    def state(self):
        return 'Ontario'

    @property
    def country(self):
        return 'Canada'

    @property
    def address(self):
        return self.parse.get('address')

    @property
    def accuracy(self):
        return self.parse.get('score')

if __name__ == '__main__':
    g = Ottawa('1552 Payette dr.')
    g.debug()
