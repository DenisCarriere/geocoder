#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import mapquest_key


class Mapquest(Base):
    """
    MapQuest
    ========
    The geocoding service enables you to take an address and get the
    associated latitude and longitude. You can also use any latitude
    and longitude pair and get the associated address. Three types of
    geocoding are offered: address, reverse, and batch.

    API Reference
    -------------
    http://www.mapquestapi.com/geocoding/
    """
    provider = 'mapquest'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://www.mapquestapi.com/geocoding/v1/address'
        self.location = location
        self.headers = {
            'referer': 'http://www.mapquestapi.com/geocoding/',
            'host': 'www.mapquestapi.com',
        }
        self.params = {
            'key': self._get_api_key(mapquest_key, **kwargs),
            'location': location,
            'maxResults': 1,
            'outFormat': 'json',
        }
        self._initialize(**kwargs)

    def _catch_errors(self):
        if self.content and 'The AppKey submitted with this request is invalid' in self.content:
            raise ValueError('MapQuest API Key invalid')

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])
        if self.parse['locations']:
            self._build_tree(self.parse['locations'][0])

    @property
    def lat(self):
        return self.parse['latLng'].get('lat')

    @property
    def lng(self):
        return self.parse['latLng'].get('lng')

    @property
    def street(self):
        return self.parse.get('street')

    @property
    def address(self):
        if self.street:
            return self.street
        elif self.city:
            return self.city
        elif self.country:
            return self.country

    @property
    def quality(self):
        return self.parse.get('geocodeQuality')

    @property
    def postal(self):
        return self.parse.get('postalCode')

    @property
    def neighborhood(self):
        return self.parse.get('adminArea6')

    @property
    def city(self):
        return self.parse.get('adminArea5')

    @property
    def county(self):
        return self.parse.get('adminArea4')

    @property
    def state(self):
        return self.parse.get('adminArea3')

    @property
    def country(self):
        return self.parse.get('adminArea1')

if __name__ == '__main__':
    g = Mapquest('1552 Payette dr., Ottawa Ontario')
    g.debug()
