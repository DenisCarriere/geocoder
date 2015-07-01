#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import requests
from geocoder.base import Base


class OttawaParcel(Base):
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
    method = 'parcel'

    def __init__(self, location, **kwargs):
        self.url = 'http://maps.ottawa.ca/arcgis/rest/services/Property_Parcels/MapServer/find'
        self.location = location
        self.address_id = self._get_address_id(location)
        if self.address_id:
            self.params = {
                'searchText': self.address_id,
                'layers': 2,
                'f': 'json',
                'sr': 4326,
            }
            self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])

    def _get_address_id(self, location):
        url = 'http://maps.ottawa.ca/arcgis/rest/services/Property_Parcels/MapServer/find'
        params = {
            'searchText': location,
            'layers': 0,
            'f': 'json',
            'sr': 4326,
        }
        r = requests.get(url, params=params)
        content = r.json()
        if content:
            results = content['results']
            if results:
                return results[0]['attributes']['PI Municipal Address ID']

    def _clean(self, item):
        if item:
            return item.strip()

    @property
    def ok(self):
        return bool(self.geometry)

    @property
    def frontage(self):
        """Length in Feet (f)"""
        if self.length and self.area:
            return round(self.area / self.length)

    @property
    def length(self):
        """Length in Feet (f)"""
        length = self.parse['attributes'].get('Shape_Length')
        if length:
            return round(float(length))

    @property
    def area(self):
        """Square Foot Area (sqft)"""
        area = self.parse['attributes'].get('Shape_Area')
        if area:
            return round(float(area) * 10.76391)

    @property
    def municipality(self):
        return self._clean(self.parse['attributes'].get('MUNICIPALITY_NAME'))

    @property
    def housenumber(self):
        return self._clean(self.parse['attributes'].get('ADDRESS_NUMBER'))

    @property
    def suffix(self):
        return self._clean(self.parse['attributes'].get('SUFFIX'))

    @property
    def public_land(self):
        return self._clean(self.parse['attributes'].get('PUBLICLAND'))

    @property
    def street(self):
        return self._clean(self.parse['attributes'].get('ROAD_NAME'))

    @property
    def legal_unit(self):
        return self._clean(self.parse['attributes'].get('LEGAL_UNIT'))

    @property
    def pin(self):
        return self._clean(self.parse['attributes'].get('PIN_NUMBER'))

    @property
    def geometry(self):
        return self.parse['geometry']

    @property
    def postal(self):
        return self._clean(self.parse['attributes'].get('POSTAL_CODE'))


if __name__ == '__main__':
    area = 2123
    length = 100
    frontage = 21
    location = '169 Carillon'
    g = OttawaParcel(location, timeout=10.0)
    print('%s: %i x %i = %i' % (location, g.frontage, g.length, g.area))
    print('453 Booth: %i x %i = %i' % (frontage, length, area))
    print('%i x %i = %i' % (g.frontage - frontage, g.length - length, g.area - area))
