#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import six
from geocoder.base import Base
from geocoder.keys import geocodefarm_key


class GeocodeFarm(Base):
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

    def __init__(self, location, **kwargs):
        self.url = 'https://www.geocode.farm/v3/json/forward/'

        key = kwargs.get('key', geocodefarm_key)

        self.params = {
            'addr': location,
            'key': key if key else None,
            'lang': kwargs.get('lang', ''),
            'country': kwargs.get('country', ''),
        }
        self._initialize(**kwargs)

    def _catch_errors(self):
        status = self.parse['STATUS'].get('status')
        if not status == 'SUCCESS':
            self.error = status

    def _exceptions(self):
        geocoding_results = self.parse['geocoding_results']
        if geocoding_results:
            self._build_tree(geocoding_results['RESULTS'][0])
            self._build_tree(geocoding_results['STATUS'])
            self._build_tree(geocoding_results['ACCOUNT'])

    @property
    def lat(self):
        lat = self.parse['COORDINATES'].get('latitude')
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = self.parse['COORDINATES'].get('longitude')
        if lng:
            return float(lng)

    @property
    def accuracy(self):
        return self.parse.get('accuracy')

    @property
    def bbox(self):
        south = self.parse['BOUNDARIES'].get('southwest_latitude')
        west = self.parse['BOUNDARIES'].get('southwest_longitude')
        north = self.parse['BOUNDARIES'].get('northeast_latitude')
        east = self.parse['BOUNDARIES'].get('northeast_longitude')
        return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self.parse.get('formatted_address')

    @property
    def housenumber(self):
        return self.parse['ADDRESS'].get('street_number')

    @property
    def street(self):
        return self.parse['ADDRESS'].get('street_name')

    @property
    def neighborhood(self):
        return self.parse['ADDRESS'].get('neighborhood')

    @property
    def city(self):
        return self.parse['ADDRESS'].get('locality')

    @property
    def county(self):
        return self.parse['ADDRESS'].get('admin_2')

    @property
    def state(self):
        return self.parse['ADDRESS'].get('admin_1')

    @property
    def country(self):
        return self.parse['ADDRESS'].get('country')

    @property
    def postal(self):
        return self.parse['ADDRESS'].get('postal_code')

    @property
    def elevation(self):
        return self.parse['LOCATION_DETAILS'].get('elevation')

    @property
    def timezone_long(self):
        return self.parse['LOCATION_DETAILS'].get('timezone_long')

    @property
    def timezone_short(self):
        return self.parse['LOCATION_DETAILS'].get('timezone_short')

    @property
    def access(self):
        return self.parse['STATUS'].get('access')

    @property
    def address_provided(self):
        return self.parse['STATUS'].get('address_provided')

    @property
    def ip_address(self):
        return self.parse['ACCOUNT'].get('ip_address')

    @property
    def distribution_license(self):
        return self.parse['ACCOUNT'].get('distribution_license')

    @property
    def usage_limit(self):
        usage_limit = self.parse['ACCOUNT'].get('usage_limit')
        if usage_limit:
            return int(usage_limit)

    @property
    def used_today(self):
        used_today = self.parse['ACCOUNT'].get('used_today')
        if used_today:
            return int(used_today)

    @property
    def used_total(self):
        used_total = self.parse['ACCOUNT'].get('used_total')
        if used_total:
            return int(used_total)

    @property
    def first_used(self):
        return self.parse['ACCOUNT'].get('first_used')

if __name__ == '__main__':
    g = GeocodeFarm("New York City")
    g.debug()
