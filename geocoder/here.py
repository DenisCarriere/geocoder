#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import app_id, app_code


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

    OSM Quality (6/6)
    -----------------
    - [x] addr:housenumber
    - [x] addr:street
    - [x] addr:city
    - [x] addr:state
    - [x] addr:country
    - [x] addr:postal

    Attributes (22/22)
    ------------------
    - [x] accuracy
    - [x] address
    - [x] bbox
    - [x] city
    - [x] confidence
    - [x] country
    - [x] country_name
    - [x] county
    - [x] encoding
    - [x] housenumber
    - [x] lat
    - [x] lng
    - [x] location
    - [x] neighborhood
    - [x] ok
    - [x] postal
    - [x] provider
    - [x] quality
    - [x] road
    - [x] state
    - [x] state_long
    - [x] status
    """
    provider = 'here'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocoder.api.here.com/6.2/geocode.json'
        self.location = location
        self.params = {
            'searchtext': location,
            'app_id': kwargs.get('app_id', app_id),
            'app_code': kwargs.get('app_code', app_code),
            'gen': 8,
        }
        self._initialize(**kwargs)

    def _exceptions(self):
        # Build intial Tree with results
        response = self.parse['Response']['View']
        if response:
            if response[0]['Result']:
                self._build_tree(response[0]['Result'][0])
        for item in self.parse['Address']['AdditionalData']:
            self.parse[item['key']] = self._encode(item['value'])

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
        return self.parse['Address'].get('District')

    @property
    def district(self):
        return self.neighborhood

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
    def state_long(self):
        return self.parse.get('StateName')

    @property
    def country(self):
        return self.parse['Address'].get('Country')

    @property
    def country_name(self):
        return self.parse.get('CountryName')

    @property
    def quality(self):
        return self.parse.get('MatchLevel')

    @property
    def accuracy(self):
        return self.parse.get('MatchType')

    @property
    def AdminInfo(self):
        return self.parse.get('AdminInfo')

    @property
    def bbox(self):
        south = self.parse['BottomRight'].get('Latitude')
        north = self.parse['TopLeft'].get('Latitude')
        west = self.parse['TopLeft'].get('Longitude')
        east = self.parse['BottomRight'].get('Longitude')
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Here('New York City')
    g.debug()
