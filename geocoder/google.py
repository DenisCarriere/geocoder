#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import six
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import google_key, google_client, google_client_secret
from collections import OrderedDict
import ratelim


class GoogleResult(OneResult):

    def __init__(self, json_content):
        # flatten geometry
        geometry = json_content.get('geometry', {})
        self._location = geometry.get('location', {})
        self._location_type = geometry.get('location_type', {})
        self._viewport = geometry.get('viewport', {})

        # Parse address components with short & long names
        for item in json_content['address_components']:
            for category in item['types']:
                json_content.setdefault(category, {})
                json_content[category]['long_name'] = item['long_name']
                json_content[category]['short_name'] = item['short_name']

        # proceed with super.__init__
        super(GoogleResult, self).__init__(json_content)

    @property
    def lat(self):
        return self._location.get('lat')

    @property
    def lng(self):
        return self._location.get('lng')

    @property
    def place(self):
        return self.raw.get('place_id')

    @property
    def quality(self):
        quality = self.raw.get('types')
        if quality:
            return quality[0]

    @property
    def accuracy(self):
        return self._location_type

    @property
    def bbox(self):
        south = self._viewport.get('southwest', {}).get('lat')
        west = self._viewport.get('southwest', {}).get('lng')
        north = self._viewport.get('northeast', {}).get('lat')
        east = self._viewport.get('northeast', {}).get('lng')
        return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self.raw.get('formatted_address')

    @property
    def postal(self):
        return self.raw.get('postal_code', {}).get('short_name')

    @property
    def subpremise(self):
        return self.raw.get('subpremise', {}).get('short_name')

    @property
    def housenumber(self):
        return self.raw.get('street_number', {}).get('short_name')

    @property
    def street(self):
        return self.raw.get('route', {}).get('short_name')

    @property
    def street_long(self):
        return self.raw.get('route', {}).get('long_name')

    @property
    def road_long(self):
        return self.street_long

    @property
    def neighborhood(self):
        return self.raw.get('neighborhood', {}).get('short_name')

    @property
    def sublocality(self):
        return self.raw.get('sublocality', {}).get('short_name')

    @property
    def city(self):
        return self.raw.get('locality', {}).get('short_name') or self.postal_town

    @property
    def city_long(self):
        return self.raw.get('locality', {}).get('long_name') or self.postal_town_long

    @property
    def postal_town(self):
        return self.raw.get('postal_town', {}).get('short_name')

    @property
    def postal_town_long(self):
        return self.raw.get('postal_town', {}).get('long_name')

    @property
    def county(self):
        return self.raw.get('administrative_area_level_2', {}).get('short_name')

    @property
    def state(self):
        return self.raw.get('administrative_area_level_1', {}).get('short_name')

    @property
    def state_long(self):
        return self.raw.get('administrative_area_level_1', {}).get('long_name')

    @property
    def province_long(self):
        return self.state_long

    @property
    def country(self):
        return self.raw.get('country', {}).get('short_name')

    @property
    def country_long(self):
        return self.raw.get('country', {}).get('long_name')


class GoogleQuery(MultipleResultsQuery):
    """
    Google Geocoding API
    ====================
    Geocoding is the process of converting addresses into geographic
    coordinates (like latitude 37.423021 and longitude -122.083739),
    which you can use to place markers or position the map.
    API Reference
    -------------
    https://developers.google.com/maps/documentation/geocoding

    For ambiguous queries or 'nearby' type queries, use the Places Text Search instead.
    https://developers.google.com/maps/documentation/geocoding/best-practices#automated-system

    Parameters
    ----------
    :param location: Your search location you want geocoded.
    :param components: Component Filtering
    :param method: (default=geocode) Use the following:
        > geocode
        > places
        > reverse
        > timezone
        > elevation
    :param key: Your Google developers free key.
    :param language: 2-letter code of preferred language of returned address elements.
    :param client: Google for Work client ID. Use with client_secret. Cannot use with key parameter
    :param client_secret: Google for Work client secret. Use with client.
    """
    provider = 'google'
    method = 'geocode'

    _URL = 'https://maps.googleapis.com/maps/api/geocode/json'
    _RESULT_CLASS = GoogleResult
    _KEY = google_key
    _KEY_MANDATORY = False

    def _build_params(self, location, provider_key, **kwargs):
        params = self._location_init(location, **kwargs)
        params['language'] = kwargs.get('language', '')
        self.rate_limit = kwargs.get('rate_limit', True)

        # adapt params to authentication method
        # either with client / secret
        self.client = kwargs.get('client', google_client)
        self.client_secret = kwargs.get('client_secret', google_client_secret)

        if self.client and self.client_secret:
            params['client'] = self.client
            return self._encode_params(params)
        # or API key
        else:
            # provider_key is computed in base.py:
            # either cls._KEY (google_key) or kwargs['key'] if provided
            params['key'] = provider_key
            return params

    def _location_init(self, location, **kwargs):
        return {
            'address': location,
            'bounds': kwargs.get('bounds', ''),
            'components': kwargs.get('components', ''),
            'region': kwargs.get('region', ''),
        }

    def _encode_params(self, params):
        # turn non-empty params into sorted list in order to maintain signature validity.
        # Requests will honor the order.
        ordered_params = sorted([(k, v)
                                 for (k, v) in params.items() if v])
        params = OrderedDict(ordered_params)

        # the signature parameter needs to come in the end of the url
        params['signature'] = self._sign_url(
            self.url, ordered_params, self.client_secret)

        return params

    def _sign_url(self, base_url=None, params=None, client_secret=None):
        """ Sign a request URL with a Crypto Key.
        Usage:
        from urlsigner import sign_url
        signed_url = sign_url(base_url=my_url,
                              params=url_params,
                              client_secret=CLIENT_SECRET)
        Args:
        base_url - The trunk of the URL to sign. E.g. https://maps.googleapis.com/maps/api/geocode/json
        params - List of tuples of URL parameters INCLUDING YOUR CLIENT ID ('client','gme-...')
        client_secret - Your Crypto Key from Google for Work
        Returns:
        The signature as a dictionary #signed request URL
        """
        import hashlib
        import hmac
        import base64
        if six.PY3:
            from urllib.parse import urlparse, urlencode
        else:
            from urllib import urlencode
            from urlparse import urlparse

        # Return if any parameters aren't given
        if not base_url or not self.client_secret or not self.client:
            return None

        # assuming parameters will be submitted to Requests in identical order!
        url = urlparse(base_url + "?" + urlencode(params))

        # We only need to sign the path+query part of the string
        url_to_sign = (url.path + "?" + url.query).encode('utf-8')

        # Decode the private key into its binary format
        # We need to decode the URL-encoded private key
        decoded_key = base64.urlsafe_b64decode(client_secret)

        # Create a signature using the private key and the URL-encoded
        # string using HMAC SHA1. This signature will be binary.
        signature = hmac.new(decoded_key, url_to_sign, hashlib.sha1)

        # Encode the binary signature into base64 for use within a URL
        encoded_signature = base64.urlsafe_b64encode(signature.digest())

        # Return signature (to be appended as a 'signature' in params)
        return encoded_signature

    def rate_limited_get(self, *args, **kwargs):
        if not self.rate_limit:
            return super(GoogleQuery, self).rate_limited_get(*args, **kwargs)
        elif self.client and self.client_secret:
            return self.rate_limited_get_for_work(*args, **kwargs)
        else:
            return self.rate_limited_get_for_dev(*args, **kwargs)

    @ratelim.greedy(2500, 60 * 60 * 24)
    @ratelim.greedy(10, 1)
    def rate_limited_get_for_dev(self, *args, **kwargs):
        return super(GoogleQuery, self).rate_limited_get(*args, **kwargs)

    @ratelim.greedy(100000, 60 * 60 * 24)  # Google for Work daily limit
    @ratelim.greedy(50, 1)  # Google for Work limit per second
    def rate_limited_get_for_work(self, *args, **kwargs):
        return super(GoogleQuery, self).rate_limited_get(*args, **kwargs)

    def _catch_errors(self, json_response):
        status = json_response.get('status')
        if not status == 'OK':
            self.error = status

        return self.error

    def _adapt_results(self, json_response):
        return json_response.get('results', [])


if __name__ == '__main__':
    g = GoogleQuery('11 Wall Street, New York')
    g.debug()
