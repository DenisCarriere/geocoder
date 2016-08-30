#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import re
import requests
from geocoder.base import Base
from geocoder.keys import canadapost_key


class Canadapost(Base):
    """
    Addres Complete API
    =======================
    The next generation of address finders, AddressComplete uses
    intelligent, fast searching to improve data accuracy and relevancy.
    Simply start typing a business name, address or Postal Code
    and AddressComplete will suggest results as you go.

    Params
    ------
    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) API Key from CanadaPost Address Complete.
    :param ``language``: (default=en) Output language preference.
    :param ``country``: (default=ca) Geofenced query by country.

    API Reference
    -------------
    https://www.canadapost.ca/pca/
    """
    provider = 'canadapost'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://ws1.postescanada-canadapost.ca/AddressComplete' \
                   '/Interactive/RetrieveFormatted/v2.10/json3ex.ws'

        self.location = location
        self.key = self._get_api_key(canadapost_key, **kwargs)
        self.timeout = kwargs.get('timeout', 5.0)
        self.proxies = kwargs.get('proxies', '')
        self._language = kwargs.get('language', 'en')
        self._country = kwargs.get('country', 'ca')
        self.id = ''

        # Connect to CanadaPost to retrieve API key if none are provided
        if not self.key:
            self._retrieve_key()
        self._retrieve_id()

        if self.key and self.id:
            self.params = {
                'Key': self.key,
                'Id': self.id,
                'Source': '',
                'cache': 'true'
            }
            self._initialize(**kwargs)
        else:
            self.json = dict()
            self.parse = self.tree()
            self._json()

    def _retrieve_key(self):
        url = 'http://www.canadapost.ca/cpo/mc/personal/postalcode/fpc.jsf'
        text = ''
        try:
            r = requests.get(url, timeout=self.timeout, proxies=self.proxies)
            text = r.text
        except:
            self.error = 'ERROR - URL Connection'

        if text:
            expression = r"'(....-....-....-....)';"
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
            'Country': self._country,
            'SearchFor': 'Everything',
            'SearchTerm': self.location,
            'LanguagePreference': self._language,
            '$cache': 'true'
        }
        items = []

        url = 'https://ws1.postescanada-canadapost.ca/AddressComplete' \
              '/Interactive/Find/v2.10/json3ex.ws'
        try:
            r = requests.get(url, params=params,
                             timeout=self.timeout,
                             proxies=self.proxies)
            items = r.json().get('Items')
            self.status_code = 200
        except:
            self.status_code = 404
            self.error = 'ERROR - URL Connection'

        if items:
            first_item = items[0]
            if 'Error' in first_item:
                self.error = first_item['Description']
            else:
                item_id = first_item['Id']
                description = first_item.get('Description')
                if item_id:
                    if 'results' in description:
                        self._retrieve_id(item_id)
                    elif 'Id' in first_item:
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

    @property
    def unit(self):
        return self.parse.get('SubBuilding')

    @property
    def domesticId(self):
        return self.parse.get('DomesticId')

    @property
    def label(self):
        return self.parse.get('Label')

    @property
    def canadapost_api_key(self):
        return self.key

if __name__ == '__main__':
    g = Canadapost("453 Booth Street, ON")
    g.debug()
