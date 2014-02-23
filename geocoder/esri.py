# -*- coding: utf-8 -*-

from base import Base


class Esri(Base):
    name = 'ESRI'
    url = 'http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find'

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['text'] = location
        self.params['f'] = 'pjson'

    def lat(self):
        return self.safe_coord('geometry-y')

    def lng(self):
        return self.safe_coord('geometry-x')

    def address(self):
        return self.safe_format('locations-name')

    def quality(self):
        return self.safe_format('attributes-Addr_Type')

    def postal(self):
        return self.safe_postal(self.address())

    def bbox(self):
        south = self.json.get('extent-ymin')
        west = self.json.get('extent-xmin')
        north = self.json.get('extent-ymax')
        east = self.json.get('extent-xmax')
        
        return self.safe_bbox(south, west, north,east)

    def country(self):
        address = self.address()
        if ',' in address:
            return address.split(',')[-1].strip()
        else:
            return ''
