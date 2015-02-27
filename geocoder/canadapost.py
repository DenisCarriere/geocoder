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

    Attributes (13/17)
    ------------------
    [x] accuracy
    [x] address
    [ ] bbox
    [x] city
    [ ] confidence
    [x] country
    [x] housenumber
    [ ] lat
    [ ] lng
    [x] location
    [x] ok
    [x] postal
    [x] provider
    [x] quality
    [x] state
    [x] status
    [x] street
    """
    provider = 'canadapost'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://ws1.postescanada-canadapost.ca/AddressComplete'
        self.url += '/Interactive/RetrieveFormatted/v2.00/json3ex.ws'
        self.location = location
        self.key = kwargs.get('key', canadapost_key)
        self.timeout = kwargs.get('timeout', 5.0)
        self.proxies = kwargs.get('proxies', '')

        # Connect to CanadaPost to retrieve API key if none are provided
        if not self.key:
            self._retrieve_key()
        self._retrieve_id()

        # Define parameters
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

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['Items']:
            self._build_tree(self.parse['Items'][0])

    @property
    def ok(self):
        return bool(self.postal)

    @property
    def quality(self):
        return self.parse.get('Type')

    @property
    def accuracy(self):
        return self.parse.get('DataLevel')

    @property
    def address(self):
        return self.parse.get('Line1')

    @property
    def postal(self):
        return self.parse.get('PostalCode')

    @property
    def housenumber(self):
        return self.parse.get('BuildingNumber')

    @property
    def street(self):
        return self.parse.get('Street')

    @property
    def city(self):
        return self.parse.get('City')

    @property
    def state(self):
        return self.parse.get('ProvinceName')

    @property
    def country(self):
        return self.parse.get('CountryName')

if __name__ == '__main__':
    g = Canadapost("453 Booth Street, Ottawa")
    g.debug()
