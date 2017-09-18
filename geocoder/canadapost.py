#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import canadapost_key_getter


class CanadapostIdResult(OneResult):

    @property
    def ok(self):
        return bool(self.item_id)

    @property
    def item_id(self):
        return self.raw.get('Id')

    @property
    def next_action(self):
        return self.raw.get('Next')


class CanadapostIdQuery(MultipleResultsQuery):

    provider = 'canadapost'
    method = 'id'

    _URL = 'https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/Find/v2.10/json3ex.ws'
    _RESULT_CLASS = CanadapostIdResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        if not provider_key:
            provider_key = canadapost_key_getter(**kwargs)

        return {
            'Key': provider_key,
            'LastId': kwargs.get('last_id', ''),
            'Country': kwargs.get('country', 'ca'),
            'SearchFor': 'Everything',
            'SearchTerm': location,
            'LanguagePreference': kwargs.get('language', 'en'),
            '$cache': 'true'
        }

    def _adapt_results(self, json_response):
        return json_response['Items']


class CanadapostResult(OneResult):

    @property
    def ok(self):
        return bool(self.postal)

    @property
    def quality(self):
        return self.raw.get('Type')

    @property
    def accuracy(self):
        return self.raw.get('DataLevel')

    @property
    def address(self):
        return self.raw.get('Line1')

    @property
    def postal(self):
        return self.raw.get('PostalCode')

    @property
    def housenumber(self):
        return self.raw.get('BuildingNumber')

    @property
    def street(self):
        return self.raw.get('Street')

    @property
    def city(self):
        return self.raw.get('City')

    @property
    def state(self):
        return self.raw.get('ProvinceName')

    @property
    def country(self):
        return self.raw.get('CountryName')

    @property
    def unit(self):
        return self.raw.get('SubBuilding')

    @property
    def domesticId(self):
        return self.raw.get('DomesticId')

    @property
    def label(self):
        return self.raw.get('Label')


class CanadapostQuery(MultipleResultsQuery):
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

    _URL = 'https://ws1.postescanada-canadapost.ca/AddressComplete/Interactive/RetrieveFormatted/v2.10/json3ex.ws'
    _RESULT_CLASS = CanadapostResult
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        if not provider_key:
            provider_key = canadapost_key_getter(**kwargs)

        self.key = provider_key

        last_id = ''
        next_action = 'Find'
        while next_action == 'Find':
            ids = CanadapostIdQuery(location, key=provider_key, last_id=last_id, **kwargs)
            next_action = ids.next_action
            last_id = ids.item_id

        if not ids.item_id:
            raise ValueError("Could not get any Id for given location")

        return {
            'Key': provider_key,
            'Id': ids.item_id,
            'Source': '',
            'MaxResults': kwargs.get('maxRows', 1),
            'cache': 'true'
        }

    def _adapt_results(self, json_response):
        return json_response['Items']

    @property
    def canadapost_api_key(self):
        return self.key


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = CanadapostQuery("453 Booth Street, ON")
    g.debug()
