#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import six
from geocoder.base import Base
from geocoder.keys import here_app_id, here_app_code


class Here(Base):
    """
    HERE Geocoding REST API
    =======================
    Send a request to the geocode endpoint to find an address
    using a combination of country, state, county, city,
    postal code, district, street and house number.

    API Reference
    -------------
    https://developer.here.com/rest-apis/documentation/geocoder
    """
    provider = 'here'
    method = 'geocode'
    qualified_address = ['city', 'district', 'postal', 'state', 'country']

    def __init__(self, location, **kwargs):
        self.url = kwargs.get('url', 'http://geocoder.cit.api.here.com/6.2/geocode.json')
        self.location = location

        # HERE Credentials
        app_id = kwargs.get('app_id', here_app_id)
        app_code = kwargs.get('app_code', here_app_code)
        if not bool(app_id and app_code):
            raise ValueError("Provide app_id & app_code")

        # URL Params
        self.params = {
            'searchtext': location,
            'app_id': app_id,
            'app_code': app_code,
            'gen': 9,
            'language': kwargs.get('language', 'en')
        }
        for value in Here.qualified_address:
            if kwargs.get(value) is not None:
                self.params[value] = kwargs.get(value)
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        view = self.parse['Response']['View']
        if view:
            result = view[0]['Result']
            if result:
                self._build_tree(result[0])
        for item in self.parse['Location']['Address']['AdditionalData']:
            self.parse[item['key']] = item['value']

    def _catch_errors(self):
        status = self.parse.get('type')
        if not status == 'OK':
            self.error = status

    @property
    def lat(self):
        return self.parse['DisplayPosition'].get('Latitude')

    @property
    def lng(self):
        return self.parse['DisplayPosition'].get('Longitude')

    @property
    def address(self):
        return self.parse['Address'].get('Label')

    @property
    def postal(self):
        return self.parse['Address'].get('PostalCode')

    @property
    def housenumber(self):
        return self.parse['Address'].get('HouseNumber')

    @property
    def street(self):
        return self.parse['Address'].get('Street')

    @property
    def neighborhood(self):
        return self.district

    @property
    def district(self):
        return self.parse['Address'].get('District')

    @property
    def city(self):
        return self.parse['Address'].get('City')

    @property
    def county(self):
        return self.parse['Address'].get('County')

    @property
    def state(self):
        return self.parse['Address'].get('State')

    @property
    def country(self):
        return self.parse['Address'].get('Country')

    @property
    def quality(self):
        return self.parse.get('MatchLevel')

    @property
    def accuracy(self):
        return self.parse.get('MatchType')

    @property
    def bbox(self):
        south = self.parse['BottomRight'].get('Latitude')
        north = self.parse['TopLeft'].get('Latitude')
        west = self.parse['TopLeft'].get('Longitude')
        east = self.parse['BottomRight'].get('Longitude')
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Here("New York City")
    g.debug()
