#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery


class MaxmindResults(OneResult):

    def __init__(self, json_content):
        # create safe shortcuts
        self._location = json_content.get('location', {})
        self._traits = json_content.get('traits', {})

        # proceed with super.__init__
        super(MaxmindResults, self).__init__(json_content)

    @property
    def lat(self):
        return self._location.get('latitude')

    @property
    def lng(self):
        return self._location.get('longitude')

    @property
    def timezone(self):
        return self._location.get('time_zone')

    @property
    def metro_code(self):
        return self._location.get('metro_code')

    @property
    def domain(self):
        return self._traits.get('domain')

    @property
    def isp(self):
        return self._traits.get('isp')

    @property
    def organization(self):
        return self._traits.get('organization')

    @property
    def ip(self):
        return self._traits.get('ip_address')

    @property
    def postal(self):
        return self.raw.get('postal', {}).get('code')

    @property
    def city(self):
        return self.raw.get('city', {}).get('names', {}).get('en')

    @property
    def state(self):
        return self.raw.get('subdivision', {}).get('names', {}).get('en')

    @property
    def country(self):
        return self.raw.get('country', {}).get('names', {}).get('en')

    @property
    def country_code(self):
        return self.raw.get('country', {}).get('iso_code')

    @property
    def continent(self):
        return self.raw.get('continent', {}).get('names', {}).get('en')

    @property
    def continent_code(self):
        return self.raw.get('continent', {}).get('code')

    @property
    def address(self):
        if self.city:
            return u'{0}, {1}, {2}'.format(self.city, self.state, self.country)
        elif self.state:
            return u'{0}, {1}'.format(self.state, self.country)
        elif self.country:
            return u'{0}'.format(self.country)
        else:
            return u''


class MaxmindQuery(MultipleResultsQuery):
    """
    MaxMind's GeoIP2
    =======================
    MaxMind's GeoIP2 products enable you to identify the location,
    organization, connection speed, and user type of your Internet
    visitors. The GeoIP2 databases are among the most popular and
    accurate IP geolocation databases available.

    API Reference
    -------------
    https://www.maxmind.com/en/geolocation_landing
    """
    provider = 'maxmind'
    method = 'geocode'

    _URL = 'https://www.maxmind.com/geoip/v2.0/city_isp_org/{0}'
    _RESULT_CLASS = MaxmindResults
    _KEY_MANDATORY = False

    def _build_headers(self, provider_key, **kwargs):
        return {
            'Referer': 'https://www.maxmind.com/en/geoip_demo',
            'Host': 'www.maxmind.com',
        }

    def _build_params(self, location, provider_key, **kwargs):
        return {'demo': 1}

    def _before_initialize(self, location, **kwargs):
        location = location or 'me'
        self.url = self._URL.format(location)

    def _catch_errors(self, json_response):
        error = json_response.get('error')
        if error:
            self.error = json_response.get('code')

        return self.error

    def _adapt_results(self, json_response):
        return [json_response]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = MaxmindQuery('8.8.8.8')
    g.debug()
