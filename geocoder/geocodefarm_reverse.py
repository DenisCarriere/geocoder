#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import

import logging

from geocoder.location import Location
from geocoder.geocodefarm import GeocodeFarmQuery


class GeocodeFarmReverse(GeocodeFarmQuery):
    """
    Geocode.Farm
    =======================
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
    :param lat: The numerical latitude value for which you wish to obtain the closest, human-readable address.
    :param lon: The numerical longitude value for which you wish to obtain the closest, human-readable address.
    :param key: (optional) API Key. Only Required for Paid Users.
    :param lang: (optional) 2 digit lanuage code to return results in. Currently only "en"(English) or "de"(German) supported.
    :param country: (optional) The country to return results in. Used for biasing purposes and may not fully filter results to this specific country.

    API Reference
    -------------
    https://geocode.farm/geocoding/free-api-documentation/
    """
    provider = 'geocodefarm'
    method = 'reverse'

    _URL = 'https://www.geocode.farm/v3/json/reverse/'

    def _build_params(self, location, provider_key, **kwargs):
        location = Location(location)
        return {
            'lat': location.latitude,
            'lon': location.longitude,
            'key': provider_key,
            'lang': kwargs.get('lang', ''),
            'country': kwargs.get('country', ''),
        }


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = GeocodeFarmReverse([45.3, -75.4])
    g.debug()
