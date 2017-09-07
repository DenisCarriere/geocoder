#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import geocodefarm_key


class GeocodeFarmResult(OneResult):

    @property
    def lat(self):
        lat = self.raw['COORDINATES'].get('latitude')
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = self.raw['COORDINATES'].get('longitude')
        if lng:
            return float(lng)

    @property
    def accuracy(self):
        return self.raw.get('accuracy')

    @property
    def bbox(self):
        south = self.raw['BOUNDARIES'].get('southwest_latitude')
        west = self.raw['BOUNDARIES'].get('southwest_longitude')
        north = self.raw['BOUNDARIES'].get('northeast_latitude')
        east = self.raw['BOUNDARIES'].get('northeast_longitude')
        return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self.raw.get('formatted_address')

    @property
    def housenumber(self):
        return self.raw['ADDRESS'].get('street_number')

    @property
    def street(self):
        return self.raw['ADDRESS'].get('street_name')

    @property
    def neighborhood(self):
        return self.raw['ADDRESS'].get('neighborhood')

    @property
    def city(self):
        return self.raw['ADDRESS'].get('locality')

    @property
    def county(self):
        return self.raw['ADDRESS'].get('admin_2')

    @property
    def state(self):
        return self.raw['ADDRESS'].get('admin_1')

    @property
    def country(self):
        return self.raw['ADDRESS'].get('country')

    @property
    def postal(self):
        return self.raw['ADDRESS'].get('postal_code')

    @property
    def elevation(self):
        return self.raw['LOCATION_DETAILS'].get('elevation')

    @property
    def timezone_long(self):
        return self.raw['LOCATION_DETAILS'].get('timezone_long')

    @property
    def timezone_short(self):
        return self.raw['LOCATION_DETAILS'].get('timezone_short')


class GeocodeFarmQuery(MultipleResultsQuery):
    """
    Geocode.Farm
    ============
    Geocode.Farm is one of the few providers that provide this highly
    specialized service for free. We also have affordable paid plans, of
    course, but our free services are of the same quality and provide the same
    results. The major difference between our affordable paid plans and our
    free API service is the limitations. On one of our affordable paid plans
    your limit is set based on the plan you signed up for, starting at 25,000
    query requests per day (API calls). On our free API offering, you are
    limited to 250 query requests per day (API calls).

    Params
    ------
    :param location: The string to search for. Usually a street address.
    :param key: (optional) API Key. Only Required for Paid Users.
    :param lang: (optional) 2 digit lanuage code to return results in. Currently only "en"(English) or "de"(German) supported.
    :param country: (optional) The country to return results in. Used for biasing purposes and may not fully filter results to this specific country.

    API Reference
    -------------
    https://geocode.farm/geocoding/free-api-documentation/
    """
    provider = 'geocodefarm'
    method = 'geocode'

    _URL = 'https://www.geocode.farm/v3/json/forward/'
    _RESULT_CLASS = GeocodeFarmResult
    _KEY = geocodefarm_key
    _KEY_MANDATORY = False

    def __init__(self, location, **kwargs):
        super(GeocodeFarmQuery, self).__init__(location, **kwargs)

        self.api_status = {}
        self.api_account = {}

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'addr': location,
            'key': provider_key,
            'lang': kwargs.get('lang', ''),
            'country': kwargs.get('country', ''),
            'count': kwargs.get('maxRows', 1),
        }

    def _catch_errors(self, json_response):
        status = json_response['geocoding_results']['STATUS'].get('status')
        if not status == 'SUCCESS':
            self.error = status

    def _adapt_results(self, json_response):
        return json_response['geocoding_results']['RESULTS']

    def _parse_results(self, json_response):
        super(GeocodeFarmQuery, self)._parse_results(json_response)

        # store status and account details
        self.api_status = json_response['geocoding_results']['STATUS']
        self.api_account = json_response['geocoding_results']['ACCOUNT']

    @property
    def access(self):
        return self.api_status.get('access')

    @property
    def address_provided(self):
        return self.api_status.get('address_provided')

    @property
    def ip_address(self):
        return self.api_account.get('ip_address')

    @property
    def distribution_license(self):
        return self.api_account.get('distribution_license')

    @property
    def usage_limit(self):
        usage_limit = self.api_account.get('usage_limit')
        if usage_limit:
            return int(usage_limit)

    @property
    def used_today(self):
        used_today = self.api_account.get('used_today')
        if used_today:
            return int(used_today)

    @property
    def used_total(self):
        used_total = self.api_account.get('used_total')
        if used_total:
            return int(used_total)

    @property
    def first_used(self):
        return self.api_account.get('first_used')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = GeocodeFarmQuery("New York City")
    g.debug()
