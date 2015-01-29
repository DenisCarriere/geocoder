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

    OSM Quality (5/6)
    -----------------
    [ ] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal

    Attributes (14/19)
    ------------------
    [ ] accuracy
    [x] address
    [ ] bbox
    [x] city
    [ ] confidence
    [x] country
    [x] county
    [ ] housenumber
    [x] lat
    [x] lng
    [x] location
    [ ] neighborhood
    [x] ok
    [x] postal
    [x] provider
    [x] quality
    [x] state
    [x] status
    [x] street
    """
    provider = 'mapquest'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://www.mapquestapi.com/geocoding/v1/address'
        self.location = location
        self.headers = {
            'referer':'http://www.mapquestapi.com/geocoding/',
            'host': 'www.mapquestapi.com',
        }
        self.params = {
            'key': self._get_mapquest_key(**kwargs),
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