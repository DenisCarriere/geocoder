#!/usr/bin/python
# coding: utf8

from .base import Base


class Arcgis(Base):
    provider = 'arcgis'
    api = 'ArcGIS REST API'
    url = 'http://geocode.arcgis.com/arcgis/rest/'
    url += 'services/World/GeocodeServer/find'
    _api_reference = ['[{0}](https://developers.arcgis.com/rest/geocode/api-reference/geocoding-find.htm)'.format(api)]
    _description = 'The World Geocoding Service finds addresses and places in all supported countries\n'
    _description += 'from a single endpoint. The service can find point locations of addresses,\n'
    _description += 'business names, and so on.  The output points can be visualized on a map,\n'
    _description += 'inserted as stops for a route, or loaded as input for a spatial analysis.\n'
    _description += 'an address, retrieving imagery metadata, or creating a route.'
    _api_parameter = []

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['text'] = location
        self.params['maxLocations'] = 1
        self.params['f'] = 'json'

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()
        self.bbox

    @property
    def lat(self):
        return self._get_json_float('geometry-y')

    @property
    def lng(self):
        return self._get_json_float('geometry-x')

    @property
    def address(self):
        return self._get_json_str('locations-name')

    @property
    def quality(self):
        return self._get_json_str('attributes-Addr_Type')

    """
    >>>>>>>>>>>>>>>>>>>>>>>>>>>
    TO-DO
    Regex on Postal Code

    @property
    def postal(self):
        # Using Regular Expression to find Postal Code
        if self.address:
            return self.safe_postal(self.address)

    >>>>>>>>>>>>>>>>>>>>>>>>>>>
    """

    @property
    def bbox(self):
        south = self._get_json_float('extent-ymin')
        west = self._get_json_float('extent-xmin')
        north = self._get_json_float('extent-ymax')
        east = self._get_json_float('extent-xmax')
        return self._get_bbox(south, west, north, east)


if __name__ == '__main__':
    g = Arcgis('453 Booth, Ottawa, ON')
    g.help()
    g.debug()