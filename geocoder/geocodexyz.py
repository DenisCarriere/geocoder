#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import geocodexyz_key


class GeocodeXYZResult(OneResult):

    def _get_value(self, json_obj, key, type=None):
        value = json_obj.get(key, {})
        if value:
            value = value.strip()
        if type and value:
            return type(value)
        return value

    def __init__(self, json_content):
        # create safe shortcuts
        self._standard = json_content.get('standard', {})

        # proceed with super.__init__
        super(GeocodeXYZResult, self).__init__(json_content)

    @property
    def lat(self):
        return self._get_value(self.raw, 'latt', float)

    @property
    def lng(self):
        return self._get_value(self.raw, 'longt', float)

    @property
    def remaining_credits(self):
        return self._get_value(self.raw, 'remaining_credits', int)

    @property
    def confidence(self):
        return self._get_value(self._standard, 'confidence', float)

    @property
    def country(self):
        return self._get_value(self._standard, 'countryname')

    @property
    def country_code(self):
        return self._get_value(self._standard, 'prov')

    @property
    def city(self):
        return self._get_value(self._standard, 'city')

    @property
    def region(self):
        return self._get_value(self._standard, 'region')

    @property
    def street(self):
        return self._get_value(self._standard, 'addresst')

    @property
    def postal(self):
        return self._get_value(self._standard, 'postal')

    @property
    def housenumber(self):
        return self._get_value(self._standard, 'stnumber')

    @property
    def address(self):
        if self.street_number:
            return u'{0} {1}, {2}'.format(
                self.street_number, self.route, self.locality)
        elif self.route and self.route != 'un-known':
            return u'{0}, {1}'.format(self.route, self.locality)
        else:
            return self.locality


class GeocodeXYZQuery(MultipleResultsQuery):
    """API to retrieve data from geocode.xyz

    Geocode.xyz uses only open data sources, including but not limited to
    OpenStreetMap, Geonames, Osmnames, openaddresses.io, UK Ordnance Survey,
    www.dati.gov.it, data.europa.eu/euodp/en/data, PSMA Geocoded National
    Address File (Australia), etc.

    """
    provider = 'geocodexyz'
    method = 'geocode'

    _URL = 'https://geocode.xyz/'
    _RESULT_CLASS = GeocodeXYZResult
    _KEY = geocodexyz_key
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        params = {
            'json': 1,
            'locate': location,
        }
        if 'region' in kwargs:
            region = kwargs.pop('region')
            if region:
                params.update({'region': region})
        if 'strictmode' in kwargs:
            params.update({'strictmode': kwargs.pop('strictmode')})
        if 'strict' in kwargs:
            params.update({'strict': kwargs.pop('strict')})
        if 'auth' in kwargs:
            params.update({'auth': kwargs.pop('auth')})
        else:
            params.update({'auth': provider_key})
        return params

    def _adapt_results(self, json_response):
        return [json_response]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = GeocodeXYZQuery('1552 Payette dr., Ottawa')
    g.debug()
