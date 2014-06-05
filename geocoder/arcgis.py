#!/usr/bin/python
# coding: utf8

from base import Base


class Arcgis(Base):
    name = 'ArcGIS'
    url = 'http://geocode.arcgis.com/arcgis/rest/'
    url += 'services/World/GeocodeServer/find'

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['text'] = location
        self.params['maxLocations'] = 1
        self.params['f'] = 'pjson'

    @property
    def lat(self):
        return self.safe_coord('geometry-y')

    @property
    def lng(self):
        return self.safe_coord('geometry-x')

    @property
    def address(self):
        return self.safe_format('locations-name')

    @property
    def quality(self):
        return self.safe_format('attributes-Addr_Type')

    @property
    def postal(self):
        # Using Regular Expression to find Postal Code
        if self.address:
            return self.safe_postal(self.address)

    @property
    def bbox(self):
        south = self.json.get('extent-ymin')
        west = self.json.get('extent-xmin')
        north = self.json.get('extent-ymax')
        east = self.json.get('extent-xmax')
        return self.safe_bbox(south, west, north, east)
