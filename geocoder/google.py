#!/usr/bin/python
# coding: utf8

from base import Base
import hashlib
import urllib
import hmac
import base64
import urlparse


class Google(Base):
    name = 'Google'
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def __init__(self, location, client='', secret='', api_key=''):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['sensor'] = 'false'
        self.params['address'] = location

        # New Encryption for Authentication Google Maps for Business
        if bool(client and secret):
            self.params['client'] = client
            self.params['signature'] = self.get_signature(self.url, self.params, secret)

        # Using old Authentication Google Maps V3
        elif api_key:
            self.params['key'] = api_key

    def get_signature(self, url, params, secret):
        # Convert the URL string to a URL
        params = urllib.urlencode(params)
        url = urlparse.urlparse(url + '?' + params)

        # Signature Key
        urlToSign = url.path + "?" + url.query

        # Decode the private key into its binary format
        decodedKey = base64.urlsafe_b64decode(secret)

        # Create a signature using the private key and the URL-encoded
        # string using HMAC SHA1. This signature will be binary.
        signature = hmac.new(decodedKey, urlToSign, hashlib.sha1)

        # Encode the binary signature into base64 for use within a URL
        encodedSignature = base64.urlsafe_b64encode(signature.digest())
        return encodedSignature
        
    def lat(self):
        return self.safe_coord('location-lat')

    def lng(self):
        return self.safe_coord('location-lng')

    def address(self):
        return self.safe_format('results-formatted_address')

    def status(self):
        return self.safe_format('status')

    def quality(self):
        return self.safe_format('geometry-location_type')

    def postal(self):
        return self.safe_format('postal_code')

    def bbox(self):
        south = self.json.get('southwest-lat')
        west = self.json.get('southwest-lng')
        north = self.json.get('northeast-lat')
        east = self.json.get('northeast-lng')
        return self.safe_bbox(south, west, north, east)

    def city(self):
        return self.safe_format('locality')

    def state(self):
        return self.safe_format('administrative_area_level_1')

    def country(self):
        return self.safe_format('country')

if __name__ == '__main__':
    pass
