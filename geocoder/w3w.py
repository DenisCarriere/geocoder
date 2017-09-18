#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import w3w_key


class W3WResult(OneResult):

    @property
    def lat(self):
        position = self.raw.get('geometry')
        if position:
            return position['lat']

    @property
    def lng(self):
        position = self.raw.get('geometry')
        if position:
            return position['lng']

    @property
    def language(self):
        return self.raw.get('language')

    @property
    def words(self):
        return self.raw.get('words')


class W3WQuery(MultipleResultsQuery):
    """
    What3Words
    ==========
    What3Words is a global grid of 57 trillion 3mx3m squares.
    Each square has a 3 word address that can be communicated quickly,
    easily and with no ambiguity.

    Addressing the world

    Everyone and everywhere now has an address

    Params
    ------
    :param location: Your search location you want geocoded.
    :param key: W3W API key.
    :param method: Chose a method (geocode, method)

    References
    ----------
    API Reference: https://docs.what3words.com/api/v2/
    Get W3W key: https://map.what3words.com/register?dev=true
    """
    provider = 'w3w'
    method = 'geocode'

    _URL = 'https://api.what3words.com/v2/forward'
    _RESULT_CLASS = W3WResult
    _KEY = w3w_key

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'addr': location,
            'key': provider_key,
        }

    def _adapt_results(self, json_response):
        return [json_response]

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = W3WQuery('embedded.fizzled.trial')
    g.debug()
