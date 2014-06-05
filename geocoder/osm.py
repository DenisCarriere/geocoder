#!/usr/bin/python
# coding: utf8

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

    @property
    def lat(self):
        return self.safe_coord('lat')

    @property
    def lng(self):
        return self.safe_coord('lon')

    @property
    def quality(self):
        return self.safe_format('type')

    @property
    def postal(self):
        postal = self.safe_format('address-postcode')
        if postal:
            return postal
        elif self.address:
            # Using Regular Expressions to get Postal Code from Address
            return self.safe_postal(self.address)

    @property
    def bbox(self):
        south = self.json.get('boundingbox-0')
        west = self.json.get('boundingbox-2')
        north = self.json.get('boundingbox-1')
        east = self.json.get('boundingbox-3')
        return self.safe_bbox(south, west, north, east)

    @property
    def address(self):
        return self.safe_format('display_name')

    @property
    def street_number(self):
        return self.safe_format('address-house_number')

    @property
    def route(self):
        return self.safe_format('address-road')

    @property
    def neighborhood(self):
        return self.safe_format('address-suburb')

    @property
    def locality(self):
        return self.safe_format('address-city')

    @property
    def state(self):
        return self.safe_format('address-state')

    @property
    def country(self):
        return self.safe_format('address-country')
