#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import opencage_key


class OpenCage(Base):
    provider = 'opencage'
    api = 'OpenCage Geocoding Services'
    url = 'http://api.opencagedata.com/geocode/v1/json'
    _description = 'OpenCage Geocoder simple, easy, and open geocoding for the entire world\n'
    _description += 'Our API combines multiple geocoding systems in the background.\n'
    _description += 'Each is optimized for different parts of the world and types of requests.'
    _description += 'We aggregate the best results from open data sources and algorithms so you don\'t have to.\n'
    _description += 'Each is optimized for different parts of the world and types of requests.'
    _api_reference = ['[{0}](http://geocoder.opencagedata.com/api.html)'.format(api)]
    _api_parameter  = [':param ``key``: (optional) use your own API Key from OpenCage.']

    def __init__(self, location, key=opencage_key):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['query'] = location
        self.params['key'] = key
        self.params['pretty'] = 1

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()
        self.bbox

        # OpenCage catch errors
        status = self.content.get('status')
        if status:
            code = status.get('code')
            message = status.get('message')
            if code:
                self._error = message

    @property
    def lat(self):
        return self._get_json_float('geometry-lat')

    @property
    def lng(self):
        return self._get_json_float('geometry-lng')

    @property
    def housenumber(self):
        return self._get_json_str('components-house_number')

    @property
    def street(self):
        return self._get_json_str('components-road')

    @property
    def address(self):
        return self._get_json_str('formatted')

    @property
    def w3w(self):
        return self._get_json_str('what3words-words')

    @property
    def license(self):
        return self._get_json_str('licenses-1-name')

    """
    @property
    def quality(self):
        return self._get_json_str('')
    """

    @property
    def accuracy(self):
        return self._get_json_str('confidence')

    @property
    def postal(self):
        return self._get_json_str('postcode')

    @property
    def bbox(self):
        south = self._get_json_float('southwest-lat')
        north = self._get_json_float('northeast-lat')
        west = self._get_json_float('southwest-lng')
        east = self._get_json_float('northeast-lng')
        return self._get_bbox(south, west, north, east)

    @property
    def neighborhood(self):
        return self._get_json_str('components-neighbourhood')

    @property
    def district(self):
        return self._get_json_str('components-city_district')

    @property
    def city(self):
        return self._get_json_str('components-city')

    @property
    def state(self):
        return self._get_json_str('components-state')

    @property
    def country(self):
        return self._get_json_str('components-country')
