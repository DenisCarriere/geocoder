#!/usr/bin/python
# coding: utf8

import re
import requests
from .base import Base
from .keys import canadapost_key
from .location import Location


class Canadapost(Base):
    """
    Addres Complete API
    =======================
    The next generation of address finders, AddressComplete uses intelligent, fast
    searching to improve data accuracy and relevancy. Simply start typing a business
    name, address or Postal Code and AddressComplete will suggest results as you go.

    API Reference
    -------------
    https://www.canadapost.ca/pca/

    OSM Quality (6/6)
    -----------------
    [x] addr:housenumber
    [x] addr:street
    [x] addr:city
    [x] addr:state
    [x] addr:country
    [x] addr:postal
    """
    provider = 'canadapost'
    method = 'geocode'
    
    def __init__(self, location, **kwargs):
        self.url = 'https://ws1.postescanada-canadapost.ca/AddressComplete'
        self.url += '/Interactive/RetrieveFormatted/v2.00/json3ex.ws'
        self.location = location
        self.key = kwargs.get('key', canadapost_key)
        self.id = None
        self.json = dict()
        self.parse = dict()
        self.timeout = kwargs.get('timeout', 5.0)
        self.proxies = kwargs.get('proxies', '')

        # Functions
        self._retrieve_key()
        self._retrieve_id()

        # Final Connection
        self.params = {
            'Key': self.key,
            'Id': self.id,
            'Source': '',
        }
        if bool(self.key and self.id):
            self._initialize(**kwargs)

    def __repr__(self):
        return "<[{0}] {1} [{2} - {3}]>".format(self.status, self.provider, self.postal, self.address)

    def _retrieve_key(self):
        url = 'http://www.canadapost.ca/cpo/mc/personal/postalcode/fpc.jsf'
        try:
            r = requests.get(url, timeout=self.timeout, proxies=self.proxies)
            text = r.text
        except:
            text = ''
            self.error = 'ERROR - URL Connection'

        expression = r'key=(....-....-....-....)'
        pattern = re.compile(expression)
        match = pattern.search(text)
        if match:
            self.key = match.group(1)
            return self.key
        else:
            self.error = 'ERROR - No API Key'

    def _retrieve_id(self, last_id=''):
        params = {
            'Key': self.key,
            'LastId': last_id,
            'Country': "CAN",
            'SearchFor': 'Everything',
            'SearchTerm': self.location,
        }

        url = 'https://ws1.postescanada-canadapost.ca/AddressComplete'
        url += '/Interactive/Find/v2.00/json3ex.ws'
        try:
            r = requests.get(url, params=params, timeout=self.timeout, proxies=self.proxies)
            items = r.json().get('Items')
            self.status_code = 200
        except:
            items = None
            self.status_code = 404
            self.error = 'ERROR - URL Connection'
    
        if items:
            items = items[0]
            item_id = items['Id']
            description = items.get('Description')
            if item_id:
                if 'results' in description:
                    self._retrieve_id(item_id)
                elif 'Id' in items:
                    self.id = item_id
                    return self.id

    @property
    def lng(self):
        return ''

    @property
    def lat(self):
        return ''

    @property
    def wkt(self):
        return ''

    @property
    def geometry(self):
        return {}

    @property
    def ok(self):
        return bool(self.postal)

    @property
    def quality(self):
        return self._get_json_str('Type')

    @property
    def address(self):
        return self._get_json_str('Line1')

    @property
    def postal(self):
        return self._get_json_str('PostalCode')

    @property
    def housenumber(self):
        return self._get_json_str('BuildingNumber')

    @property
    def street(self):
        return self._get_json_str('Street')

    @property
    def city(self):
        return self._get_json_str('City')

    @property
    def state(self):
        return self._get_json_str('ProvinceName')

    @property
    def country(self):
        return self._get_json_str('CountryName')

if __name__ == '__main__':
    g = Canadapost("453 Booth Street, Ottawa")
    g.debug()