#!/usr/bin/python
# coding: utf8

from .base import Base


class Arcgis(Base):
    """
    ArcGIS REST API
    =======================
    The World Geocoding Service finds addresses and places in all supported countries
    from a single endpoint. The service can find point locations of addresses,
    business names, and so on.  The output points can be visualized on a map,
    inserted as stops for a route, or loaded as input for a spatial analysis.
    an address, retrieving imagery metadata, or creating a route.

    API Reference
    -------------
    https://developers.arcgis.com/rest/geocode/api-reference/geocoding-find.htm

    OSM Quality (0/6)
    -----------------
    [ ] addr:housenumber
    [ ] addr:street
    [ ] addr:city
    [ ] addr:state
    [ ] addr:country
    [ ] addr:postal
    """
    provider = 'arcgis'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/find'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'f': 'json',
            'text': location,
            'maxLocations': 1,
        }
        self._initialize(**kwargs)

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
    def housenumber(self):
        return ''

    @property
    def street(self):
        return ''

    @property
    def city(self):
        return ''

    @property
    def state(self):
        return ''

    @property
    def country(self):
        return ''

    @property
    def quality(self):
        return self._get_json_str('attributes-Addr_Type')

    @property
    def postal(self):
        return ''

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
    g.debug()