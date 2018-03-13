#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import MultipleResultsQuery
from geocoder.mapquest import MapquestResult
from geocoder.keys import mapquest_key


class MapQuestBatchResult(MapquestResult):

    @property
    def ok(self):
        return bool(self.quality)


class MapquestBatch(MultipleResultsQuery):
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
    method = 'batch'

    _RESULT_CLASS = MapQuestBatchResult
    _URL = 'http://www.mapquestapi.com/geocoding/v1/batch'
    _TIMEOUT = 30
    _KEY = mapquest_key

    def _build_params(self, location, provider_key, **kwargs):
        self._TIMEOUT = kwargs.get('timeout', 30)

        return {
            'key': provider_key,
            'location': location,
            'maxResults': 1,
            'outFormat': 'json',
        }

    def _adapt_results(self, json_response):
        results = json_response.get('results', [])
        if results:
            return [result['locations'][0] for result in results]

        return []


if __name__ == '__main__':
    g = MapquestBatch(['Denver,CO', 'Boulder,CO'])
    g.debug()
