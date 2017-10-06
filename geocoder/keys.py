#!/usr/bin/python
# coding: utf8
import os
import re
import requests


bing_key = os.environ.get('BING_API_KEY')
tomtom_key = os.environ.get('TOMTOM_API_KEY')
here_app_id = os.environ.get('HERE_APP_ID')
here_app_code = os.environ.get('HERE_APP_CODE')
geonames_username = os.environ.get('GEONAMES_USERNAME')
opencage_key = os.environ.get('OPENCAGE_API_KEY')
mapquest_key = os.environ.get('MAPQUEST_API_KEY')
baidu_key = os.environ.get('BAIDU_API_KEY')
baidu_security_key = os.environ.get('BAIDU_SECURITY_KEY')
gaode_key = os.environ.get('GAODE_API_KEY')
w3w_key = os.environ.get('W3W_API_KEY')
mapbox_access_token = os.environ.get('MAPBOX_ACCESS_TOKEN')
google_key = os.environ.get('GOOGLE_API_KEY')
google_client = os.environ.get('GOOGLE_CLIENT')
google_client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')
mapzen_key = os.environ.get('MAPZEN_API_KEY')
tamu_key = os.environ.get('TAMU_API_KEY')
geocodefarm_key = os.environ.get('GEOCODEFARM_API_KEY')
tgos_key = os.environ.get('TGOS_API_KEY')
locationiq_key = os.environ.get('LOCATIONIQ_API_KEY')


class CanadapostKeyLazySingleton(object):

    CANADAPOST_KEY_REGEX = re.compile(r"'(....-....-....-....)';")

    def __init__(self):
        self._key = None

    def __call__(self, **kwargs):
        if self._key is None:
            self._key = self.retrieve_key(**kwargs)
        return self._key

    @classmethod
    def retrieve_key(cls, **kwargs):
        # get key with traditionnal mechanism
        key = kwargs.get('key')
        canadapost_key = os.environ.get('CANADAPOST_API_KEY')
        if key or canadapost_key:
            return key if key else canadapost_key

        # fallback
        try:
            url = 'http://www.canadapost.ca/cpo/mc/personal/postalcode/fpc.jsf'
            timeout = kwargs.get('timeout', 5.0)
            proxies = kwargs.get('proxies', '')
            r = requests.get(url, timeout=timeout, proxies=proxies)
            match = cls.CANADAPOST_KEY_REGEX.search(r.text)
            if match:
                return match.group(1)
            else:
                raise ValueError('No API Key found')
        except Exception as err:
            raise ValueError('Could not retrieve API Key: %s' % err)


canadapost_key_getter = CanadapostKeyLazySingleton()
