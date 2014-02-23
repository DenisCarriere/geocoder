# -*- coding: utf-8 -*-

from base import Base


class Osm(Base):
    name = 'OSM'
    url = 'http://nominatim.openstreetmap.org/search'

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['format'] = 'json'
        self.params['limit'] = 1
        self.params['addressdetails'] = 1
        self.params['q'] = location

    def lat(self):
        return self.safe_coord('lat')

    def lng(self):
        return self.safe_coord('lon')

    def address(self):
        return self.safe_format('display_name')

    def quality(self):
        return self.safe_format('type')

    def postal(self):
        # Using Regular Expression to find Postal Code
        return self.safe_postal(self.address())

    def bbox(self):
        south = self.json.get('boundingbox-0')
        west = self.json.get('boundingbox-2')
        north = self.json.get('boundingbox-1')
        east = self.json.get('boundingbox-3')
        return self.safe_bbox(south, west, north, east)

    def city(self):
        return self.safe_format('address-city')

    def country(self):
        return self.safe_format('address-country')
