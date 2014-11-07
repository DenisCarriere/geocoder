#!/usr/bin/python
# coding: utf8

from .base import Base


class Mapquest(Base):
    provider = 'mapquest'
    api = 'Geocoding Service'
    url = 'http://www.mapquest.ca/_svc/searchio'
    _description = 'The geocoding service enables you to take an address and get the \n'
    _description += 'associated latitude and longitude. You can also use any latitude \n'
    _description += 'and longitude pair and get the associated address. Three types of \n'
    _description += 'geocoding are offered: address, reverse, and batch.'
    _api_reference = ['[{0}](http://www.mapquestapi.com/geocoding/)'.format(api)]
    _api_parameter  = []

    def __init__(self, location):
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.params = dict()
        self.params['action'] = 'search'
        self.params['query0'] = location
        self.params['maxResults'] = 1
        self.params['page'] = 0
        self.params['thumbMaps'] = 'false'

        # Initialize
        self._connect()
        self._parse(self.content)
        self._json()

    @property
    def lat(self):
        return self._get_json_float('latLng-lat')

    @property
    def lng(self):
        return self._get_json_float('latLng-lng')

    @property
    def address(self):
        return self._get_json_str('address-singleLineAddress')

    @property
    def quality(self):
        return self._get_json_str('address-quality')

    @property
    def postal(self):
        return self._get_json_str('address-postalCode')

    @property
    def city(self):
        return self._get_json_str('address-locality')

    @property
    def state(self):
        return self._get_json_str('address-regionLong')

    @property
    def country(self):
        return self._get_json_str('address-countryLong')

if __name__ == '__main__':
    g = Mapquest('453 Booth Street, Ottawa')
    g.help()
    g.debug()
