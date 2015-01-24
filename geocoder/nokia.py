#!/usr/bin/python
# coding: utf8

from base import Base
from keys import app_id, app_code


class Nokia(Base):
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
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal

    Attributes (19/19)
    ------------------
    [x] accuracy
    [x] address
    [x] bbox
    [x] city
    [x] confidence
    [x] country
    [x] county
    [x] housenumber
    [x] lat
    [x] lng
    [x] location
    [x] neighborhood
    [x] ok
    [x] postal
    [x] provider
    [x] quality
    [x] state
    [x] status
    [x] street
    """
    provider = 'nokia'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://geocoder.api.here.com/6.2/geocode.json'
        self.location = location
        self.params = {
            'searchtext': location,
            'app_id': kwargs.get('app_id', app_id),
            'app_code': kwargs.get('app_code', app_code),
            'gen': 4,
        }
        self._initialize(**kwargs)


    def _exceptions(self):
        # Build intial Tree with results
        response = self.parse['Response']['View']
        if response:
            if response[0]['Result']:
                self._build_tree(response[0]['Result'][0])

    @property
    def lat(self):
        return self.parse['DisplayPosition']['Latitude']

    @property
    def lng(self):
        return self.parse['DisplayPosition']['Longitude']

    @property
    def address(self):
        return self.parse['Address']['Label']

    @property
    def postal(self):
        return self.parse['Address']['PostalCode']

    @property
    def housenumber(self):
        return self.parse['Address']['HouseNumber']

    @property
    def street(self):
        return self.parse['Address']['Street']

    @property
    def neighborhood(self):
        return self.parse['Address']['District']

    @property
    def city(self):
        return self.parse['Address']['City']

    @property
    def county(self):
        return self.parse['Address']['County']

    @property
    def state(self):
        return self.parse['Address']['State']

    @property
    def country(self):
        return self.parse['Address']['Country']

    @property
    def quality(self):
        return self.parse['MatchLevel']

    @property
    def accuracy(self):
        return self.parse['MatchType']

    @property
    def bbox(self):
        south = self.parse['BottomRight']['Latitude']
        north = self.parse['TopLeft']['Latitude']
        west = self.parse['TopLeft']['Longitude']
        east = self.parse['BottomRight']['Longitude']
        return self._get_bbox(south, west, north, east)

if __name__ == '__main__':
    g = Nokia('1552 Payette dr., Ottawa ON')
    g.debug()