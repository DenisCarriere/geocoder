#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import six
from geocoder.base import Base
from geocoder.keys import google_key, google_client, google_client_secret


class Google(Base):
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

    def __init__(self, location, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.location = location
        self.client = kwargs.get('client', google_client)
        self.client_secret = kwargs.get('client_secret', google_client_secret)
        self.params = {
            'address': location,
            'bounds': kwargs.get('bounds', ''),
            'language': kwargs.get('language', ''),
            'region': kwargs.get('region', ''),
            'components': kwargs.get('components', ''),
        }
        if self.client and self.client_secret:
            self.params['client'] = self.client
            self._encode_params()
        elif kwargs.get('key', google_key):
            self.params['key'] = kwargs.get('key', google_key)
        self._initialize(**kwargs)

    def _encode_params(self):
        # turn non-empty params into sorted list in order to maintain signature validity.
        # Requests will honor the order.
        self.params = sorted([(k, v) for (k, v) in self.params.items() if v])

        # the signature parameter needs to come in the end of the url
        self.params.append(self._sign_url(self.url, self.params, self.client_secret))

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

        # Return signature (to be appended as a param tuple to url)
        return "signature", encoded_signature

    """
    import ratelim
    import requests
    @staticmethod
    @ratelim.greedy(2500, 60 * 60 * 24)
    @ratelim.greedy(10, 1)
    @ratelim.greedy(100000, 60 * 60 * 24) # Google for Work daily limit
    @ratelim.greedy(50, 1) # Google for Work limit per second
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)
    """

    def _catch_errors(self):
        status = self.parse.get('status')
        if not status == 'OK':
            self.error = status

    def _exceptions(self):
        # Build intial Tree with results
        if self.parse['results']:
            self._build_tree(self.parse.get('results')[0])

            # Build Geometry
            self._build_tree(self.parse.get('geometry'))

            # Parse address components with short & long names
            for item in self.parse['address_components']:
                for category in item['types']:
                    self.parse[category]['long_name'] = item['long_name']
                    self.parse[category]['short_name'] = item['short_name']

    @property
    def lat(self):
        return self.parse['location'].get('lat')

    @property
    def lng(self):
        return self.parse['location'].get('lng')

    @property
    def place(self):
        return self.parse.get('place_id')

    @property
    def quality(self):
        quality = self.parse.get('types')
        if quality:
            return quality[0]

    @property
    def accuracy(self):
        return self.parse.get('location_type')

    @property
    def bbox(self):
        south = self.parse['southwest'].get('lat')
        west = self.parse['southwest'].get('lng')
        north = self.parse['northeast'].get('lat')
        east = self.parse['northeast'].get('lng')
        return self._get_bbox(south, west, north, east)

    @property
    def address(self):
        return self.parse.get('formatted_address')

    @property
    def postal(self):
        return self.parse['postal_code'].get('short_name')

    @property
    def subpremise(self):
        return self.parse['subpremise'].get('short_name')

    @property
    def housenumber(self):
        return self.parse['street_number'].get('short_name')

    @property
    def street(self):
        return self.parse['route'].get('short_name')

    @property
    def street_long(self):
        return self.parse['route'].get('long_name')

    @property
    def road_long(self):
        return self.street_long

    @property
    def neighborhood(self):
        return self.parse['neighborhood'].get('short_name')

    @property
    def sublocality(self):
        return self.parse['sublocality'].get('short_name')

    @property
    def city(self):
        city = self.parse['locality'].get('short_name')
        postal_town = self.postal_town
        if city:
            return city
        else:
            return postal_town

    @property
    def city_long(self):
        city_long = self.parse['locality'].get('long_name')
        postal_town_long = self.postal_town_long
        if city_long:
            return city_long
        else:
            return postal_town_long

    @property
    def postal_town(self):
        return self.parse['postal_town'].get('short_name')

    @property
    def postal_town_long(self):
        return self.parse['postal_town'].get('long_name')

    @property
    def county(self):
        return self.parse['administrative_area_level_2'].get('short_name')

    @property
    def state(self):
        return self.parse['administrative_area_level_1'].get('short_name')

    @property
    def state_long(self):
        return self.parse['administrative_area_level_1'].get('long_name')

    @property
    def province_long(self):
        return self.state_long

    @property
    def country(self):
        return self.parse['country'].get('short_name')

    @property
    def country_long(self):
        return self.parse['country'].get('long_name')

if __name__ == '__main__':
    g = Google('11 Wall Street, New York')
    g.debug()
