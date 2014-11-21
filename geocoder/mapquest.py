#!/usr/bin/python
# coding: utf8

import re
import requests
from .base import Base
from .keys import mapquest_key


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

    OSM Quality (3/6)
    -----------------
    [ ] addr:housenumber
    [ ] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [ ] addr:postal
    """
    provider = 'mapquest'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://www.mapquestapi.com/geocoding/v1/address'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.key = self._get_mapquest_key(**kwargs)
        self.headers = {
            'referer':'http://www.mapquestapi.com/geocoding/',
            'host': 'www.mapquestapi.com',
        }
        self.params = {
            'key': self.key,
            'location': location,
            'maxResults': 1,
        }
        self._initialize(**kwargs)

    def _get_mapquest_key(self, **kwargs):
        key = kwargs.get('key', mapquest_key)
        if key:
            return key
        if not key:
            url = 'http://www.mapquestapi.com/media/js/config_key.js'
            timeout = kwargs.get('timeout', 5.0)
            proxies = kwargs.get('proxies', '')

            try:
                r = requests.get(url, timeout=timeout, proxies=proxies)
                text = r.content
            except:
                self.error = 'ERROR - Could not retrieve API Key'
                self.status_code = 404

            expression = r"APP_KEY = '(.+)'"
            pattern = re.compile(expression)
            match = pattern.search(text)
            if match:
                return match.group(1)
            else:
                self.error = 'ERROR - No API Key'

    @property
    def lat(self):
        return self._get_json_float('latLng-lat')

    @property
    def lng(self):
        return self._get_json_float('latLng-lng')

    @property
    def housenumber(self):
        return ''

    @property
    def street(self):
        return self._get_json_str('locations-street')

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
        return self._get_json_str('locations-geocodeQuality')

    @property
    def postal(self):
        return self._get_json_str('locations-postalCode')

    @property
    def neighborhood(self):
        return self._get_json_str('locations-adminArea6')

    @property
    def city(self):
        return self._get_json_str('locations-adminArea5')

    @property
    def county(self):
        return self._get_json_str('locations-adminArea4')

    @property
    def state(self):
        return self._get_json_str('locations-adminArea3')

    @property
    def country(self):
        return self._get_json_str('locations-adminArea1')

if __name__ == '__main__':
    g = Mapquest('1552 Payette dr., Ottawa Ontario')
    g.debug()