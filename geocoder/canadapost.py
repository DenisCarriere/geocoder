#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import canadapost_key
import re
import requests
from .location import Location


class Canadapost(Base):
    provider = 'canadapost'
    api = 'Addres Complete API'
    url = 'https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/RetrieveFormatted/v2.00/json3ex.ws'
    _description = 'The next generation of address finders, AddressComplete uses intelligent, fast\n'
    _description += 'searching to improve data accuracy and relevancy. Simply start typing a business\n'
    _description += 'name, address or Postal Code and AddressComplete will suggest results as you go.'
    _api_reference = ['[{0}](https://www.canadapost.ca/pca/)'.format(api)]
    _api_parameter = [':param ``country``: (default=\'CAN\') biase the search on a selected country.']
    _api_parameter  = [':param ``key``: (optional) use your own API Key from CanadaPost Address Complete.']
    _example = ['>>> g = geocoder.canadapost(\'<address>\')',
                '>>> g.postal',
                '\'K1R 7K9\'']

    def __init__(self, location, key=canadapost_key, reverse=False):
        self.location = location
        self.reverse = reverse
        self.key = key
        self.id = None
        self.json = dict()
        self.parse = dict()
        self.params = dict()

        # Functions
        self._retrieve_key()
        self._retrieve_id()

        # Attributes
        self.params['Key'] = self.key
        self.params['Id'] = self.id
        self.params['Source'] = ''

        # Initialize
        if bool(self.key and self.id):
            self._connect()
            self._parse(self.content)
            self._json()

    def __repr__(self):
        return "<[{0}] {1} [{2} - {3}]>".format(self.status, self.provider, self.postal, self.address)

    def _retrieve_key(self):
        url = 'http://www.canadapost.ca/cpo/mc/personal/postalcode/fpc.jsf'
        try:
            r = requests.get(url, timeout=self._timeout)
            text = r.text
        except:
            text = str('')
            self._error = 'ERROR - URL Connection'

        expression = r'key=(....-....-....-....)'
        pattern = re.compile(expression)
        match = pattern.search(text)
        if match:
            self.key = match.group(1)
            return self.key
        else:
            self._error = 'ERROR - No API Key'

    def _retrieve_id(self, last_id=''):
        params = dict()
        params['Key'] = self.key
        params['LastId'] = last_id
        params['Country'] = "CAN"
        params['SearchFor'] = 'Everything'
        params['SearchTerm'] = self.location

        url = 'https://ws1.postescanada-canadapost.ca/AddressComplete'
        url += '/Interactive/Find/v2.00/json3ex.ws'
        try:
            r = requests.get(url, params=params, timeout=self._timeout)
            items = r.json().get('Items')
            self.status_code = 200
        except:
            items = None
            self.status_code = 404
            self._error = 'ERROR - URL Connection'
    
        if items:
            items = items[0]
            item_id = items['Id']
            description = items.get('Description')
            if item_id:
                if 'results' in description:
                    self._retrieve_id(item_id)
                elif 'Id' in items:
                    self.id = item_id

    @property
    def lng(self):
        return 0.0

    @property
    def lat(self):
        return 0.0

    @property
    def wkt(self):
        return str('')

    @property
    def geometry(self):
        return dict()

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
    g.help()
    g.debug()