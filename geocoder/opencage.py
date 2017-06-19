#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import opencage_key


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
    """
    provider = 'opencage'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.opencagedata.com/geocode/v1/json'
        self.location = location
        self.params = {
            'query': location,
            'key': self._get_api_key(opencage_key, **kwargs),
        }
        self._initialize(**kwargs)

    def _catch_errors(self):
        if self.content:
            status = self.content.get('status')
            if status:
                self.status_code = status.get('code')
                message = status.get('message')
                if self.status_code:
                    self.error = message

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])
        licenses = self.parse['licenses']
        if licenses:
            self.parse['licenses'] = licenses[0]

    @property
    def lat(self):
        return self.parse['geometry'].get('lat')

    @property
    def lng(self):
        return self.parse['geometry'].get('lng')

    @property
    def address(self):
        return self.parse.get('formatted')

    @property
    def housenumber(self):
        return self.parse['components'].get('house_number')

    @property
    def street(self):
        return self.parse['components'].get('road')

    @property
    def neighborhood(self):
        neighbourhood = self.parse['components'].get('neighbourhood')
        if neighbourhood:
            return neighbourhood
        elif self.suburb:
            return self.suburb
        elif self.city_district:
            return self.city_district

    @property
    def suburb(self):
        return self.parse['components'].get('suburb')

    @property
    def city_district(self):
        return self.parse['components'].get('city_district')

    @property
    def city(self):
        city = self.parse['components'].get('city')
        if city:
            return city
        elif self.town:
            return self.town
        elif self.village:
            return self.village
        elif self.county:
            return self.county

    @property
    def town(self):
        return self.parse['components'].get('town')

    @property
    def village(self):
        return self.parse['components'].get('village')

    @property
    def county(self):
        return self.parse['components'].get('county')

    @property
    def state(self):
        return self.parse['components'].get('state')

    @property
    def country(self):
        return self.parse['components'].get('country_code')

    @property
    def postal(self):
        return self.parse['components'].get('postcode')

    @property
    def confidence(self):
        return self.parse.get('confidence')

    @property
    def w3w(self):
        return self.parse['what3words'].get('words')

    @property
    def mgrs(self):
        return self.parse['annotations'].get('MGRS')

    @property
    def geohash(self):
        return self.parse['annotations'].get('geohash')

    @property
    def callingcode(self):
        return self.parse['annotations'].get('callingcode')

    @property
    def Maidenhead(self):
        return self.parse['annotations'].get('Maidenhead')

    @property
    def DMS(self):
        return self.parse.get('DMS')

    @property
    def Mercator(self):
        return self.parse.get('Mercator')

    @property
    def license(self):
        return self.parse.get('licenses')

    @property
    def bbox(self):
        south = self.parse['southwest'].get('lat')
        north = self.parse['northeast'].get('lat')
        west = self.parse['southwest'].get('lng')
        east = self.parse['northeast'].get('lng')
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = OpenCage('1552 Payette dr., Ottawa')
    print(g.json['mgrs'])
