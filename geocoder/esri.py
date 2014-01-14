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
        southwest = self.json.get('extent-ymin'), self.json.get('extent-xmin')
        northeast = self.json.get('extent-ymax'), self.json.get('extent-xmax')
        return self.safe_bbox(southwest, northeast)
