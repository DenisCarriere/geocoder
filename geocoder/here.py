#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import here_app_id, here_app_code

from geocoder.location import BBox


class HereResult(OneResult):

    def __init__(self, json_content):
        self._display_position = json_content.get('DisplayPosition', {})
        self._address = json_content.get('Address', {})
        self._mapview = json_content.get('MapView', {})

        for item in json_content['Address']['AdditionalData']:
            json_content[item['key']] = item['value']

        super(HereResult, self).__init__(json_content)

    @property
    def lat(self):
        return self._display_position.get('Latitude')

    @property
    def lng(self):
        return self._display_position.get('Longitude')

    @property
    def address(self):
        return self._address.get('Label')

    @property
    def postal(self):
        return self._address.get('PostalCode')

    @property
    def housenumber(self):
        return self._address.get('HouseNumber')

    @property
    def street(self):
        return self._address.get('Street')

    @property
    def neighborhood(self):
        return self.district

    @property
    def district(self):
        return self._address.get('District')

    @property
    def city(self):
        return self._address.get('City')

    @property
    def county(self):
        return self._address.get('County')

    @property
    def state(self):
        return self._address.get('State')

    @property
    def country(self):
        return self._address.get('Country')

    @property
    def quality(self):
        return self.raw.get('MatchLevel')

    @property
    def accuracy(self):
        return self.raw.get('MatchType')

    @property
    def bbox(self):
        south = self._mapview['BottomRight'].get('Latitude')
        north = self._mapview['TopLeft'].get('Latitude')
        west = self._mapview['TopLeft'].get('Longitude')
        east = self._mapview['BottomRight'].get('Longitude')
        return self._get_bbox(south, west, north, east)


class HereQuery(MultipleResultsQuery):
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

    _URL = 'http://geocoder.cit.api.here.com/6.2/geocode.json'
    _RESULT_CLASS = HereResult

    @classmethod
    def _get_api_key(cls, key=None):
        # API key is split between app_id and app_code -> managed in _build_params
        pass

    def _build_params(self, location, provider_key, **kwargs):
        # HERE Credentials
        app_id = kwargs.get('app_id', here_app_id)
        app_code = kwargs.get('app_code', here_app_code)
        if not bool(app_id and app_code):
            raise ValueError("Provide app_id & app_code")

        # URL Params
        params = {
            'searchtext': location,
            'app_id': app_id,
            'app_code': app_code,
            'gen': 9,
            'maxresults': kwargs.get('maxRows', 1),
            'language': kwargs.get('language', 'en'),
        }

        # bounding box if present
        bbox = kwargs.get('bbox')
        if bbox:
            bbox = BBox(bbox=bbox)
            # do not forget to convert bbox to mapbox expectations...
            params['bbox'] = u'{north},{west};{south},{east}'.format(
                west=bbox.west,
                east=bbox.east,
                south=bbox.south,
                north=bbox.north
            )

        for value in self.qualified_address:
            if kwargs.get(value) is not None:
                params[value] = kwargs.get(value)

        return params

    def _catch_errors(self, json_response):
        status = json_response.get('type')
        if not status == 'OK':
            self.error = status

        return self.error

    def _adapt_results(self, json_response):
        # Build intial Tree with results
        return [item['Location']
                for item in json_response['Response']['View'][0]['Result']]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = HereQuery("New York City")
    g.debug()
