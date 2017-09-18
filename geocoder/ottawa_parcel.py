#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery


class OttawaParcelIdResult(OneResult):

    @property
    def ok(self):
        return bool(self.address_id)

    @property
    def address_id(self):
        return self.raw.get('attributes', {}).get('PI Municipal Address ID')


class OttawaParcelIdQuery(MultipleResultsQuery):
    # XXX 8 sept 2017: Service still available ? not documented and returning 403

    _URL = 'http://maps.ottawa.ca/arcgis/rest/services/Property_Parcels/MapServer/find'
    _RESULT_CLASS = OttawaParcelIdResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'searchText': location,
            'layers': 0,
            'f': 'json',
            'sr': 4326,
        }

    def _adapt_results(self, json_response):
        return json_response.get('results', [])


class OttawaParcelResult(OneResult):

    @property
    def ok(self):
        return bool(self.geometry)

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
    def frontage(self):
        """Length in Feet (f)"""
        if self.length and self.area:
            return round(self.area / self.length)

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

    def _clean(self, item):
        if item:
            return item.strip()


class OttawaParcelQuery(MultipleResultsQuery):
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

    _URL = 'http://maps.ottawa.ca/arcgis/rest/services/Property_Parcels/MapServer/find'
    _RESULT_CLASS = OttawaParcelResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        ids = OttawaParcelIdQuery(location)
        if not ids.address_id:
            raise ValueError("Could not get any Id for given location")

        return {
            'searchText': ids.address_id,
            'layers': 2,
            'f': 'json',
            'sr': 4326,
        }

    def _adapt_results(self, json_response):
        return json_response.get('results', [])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    area = 2123
    length = 100
    frontage = 21
    location = '169 Carillon'
    g = OttawaParcelQuery(location, timeout=10.0)
    print('%s: %i x %i = %i' % (location, g.frontage, g.length, g.area))
    print('453 Booth: %i x %i = %i' % (frontage, length, area))
    print('%i x %i = %i' % (g.frontage - frontage, g.length - length, g.area - area))
