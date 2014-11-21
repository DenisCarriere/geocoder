#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import opencage_key


class OpenCage(Base):
    """
    OpenCage Geocoding Services
    ===========================
    OpenCage Geocoder simple, easy, and open geocoding for the entire world
    Our API combines multiple geocoding systems in the background.
    Each is optimized for different parts of the world and types of requests.
    We aggregate the best results from open data sources and algorithms so you don't have to.
    Each is optimized for different parts of the world and types of requests.

    API Reference
    -------------
    http://geocoder.opencagedata.com/api.html

    OSM Quality (5/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [ ] addr:postal
    """
    provider = 'opencage'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.opencagedata.com/geocode/v1/json'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'query': location,
            'key': kwargs.get('app_id', opencage_key),
            'pretty': 1,
        }
        self._initialize(**kwargs)
        self._opencage_catch_errors()

    def _opencage_catch_errors(self):
        status = self.content.get('status')
        if status:
            code = status.get('code')
            message = status.get('message')
            if code:
                self.error = message

    @property
    def lat(self):
        return self._get_json_float('geometry-lat')

    @property
    def lng(self):
        return self._get_json_float('geometry-lng')

    @property
    def address(self):
        return self._get_json_str('formatted')

    @property
    def housenumber(self):
        return self._get_json_str('components-house_number')

    @property
    def street(self):
        return self._get_json_str('components-road')

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
        country = self._get_json_str('components-country_code')
        if country:
            return country.upper()

    @property
    def postal(self):
        return self._get_json_str('postcode')

    @property
    def quality(self):
        return self._get_json_str('')

    @property
    def accuracy(self):
        return self._get_json_str('confidence')

    @property
    def w3w(self):
        return self._get_json_str('what3words-words')

    @property
    def mgrs(self):
        return self._get_json_str('annotations-MGRS')

    @property
    def geohash(self):
        return self._get_json_str('annotations-geohash')

    @property
    def license(self):
        return self._get_json_str('licenses-1-name')

    @property
    def bbox(self):
        south = self._get_json_float('southwest-lat')
        north = self._get_json_float('northeast-lat')
        west = self._get_json_float('southwest-lng')
        east = self._get_json_float('northeast-lng')
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = OpenCage('1552 Payette dr., Ottawa ON')
    g.debug()