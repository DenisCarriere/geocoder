#!/usr/bin/python
# coding: utf8

import sys
from .osm import Osm
from .w3w import W3W
from .bing import Bing
from .here import Here
from .yahoo import Yahoo
from .baidu import Baidu
from .tomtom import Tomtom
from .google import Google
from .arcgis import Arcgis
from .ottawa import Ottawa
from .yandex import Yandex
from .maxmind import Maxmind
from .opencage import OpenCage
from .geonames import Geonames
from .mapquest import Mapquest
from .timezone import Timezone
from .elevation import Elevation
from .geolytica import Geolytica
from .freegeoip import FreeGeoIP
from .canadapost import Canadapost
from .w3w_reverse import W3WReverse
from .here_reverse import HereReverse
from .bing_reverse import BingReverse
from .google_reverse import GoogleReverse
from .yandex_reverse import YandexReverse
from .mapquest_reverse import MapquestReverse
from .opencage_reverse import OpenCageReverse


def get(location, **kwargs):
    """Get Geocode

    :param ``location``: Your search location you want geocoded.
    :param ``provider``: The geocoding engine you want to use.
    :param ``method``: Define the method (geocode, method).
    """
    provider = kwargs.get('provider', 'bing').lower().strip()
    method = kwargs.get('method', 'geocode').lower().strip()
    options = {
        'osm': {'geocode': Osm},
        'here': {
            'geocode': Here,
            'reverse': HereReverse,
        },
        'baidu': {'geocode': Baidu},
        'yahoo': {'geocode': Yahoo},
        'tomtom': {'geocode': Tomtom},
        'arcgis': {'geocode': Arcgis},
        'ottawa': {'geocode': Ottawa},
        'maxmind': {'geocode': Maxmind},
        'geonames': {'geocode': Geonames},
        'freegeoip': {'geocode': FreeGeoIP},
        'w3w': {
            'geocode': W3W,
            'reverse': W3WReverse,
        },
        'yandex': {
            'geocode': Yandex,
            'reverse': YandexReverse,
        },
        'mapquest': {
            'geocode': Mapquest,
            'reverse': MapquestReverse,
        },
        'geolytica': {'geocode': Geolytica},
        'canadapost': {'geocode': Canadapost},
        'opencage': {
            'geocode': OpenCage,
            'reverse': OpenCageReverse,
        },
        'bing': {
            'geocode': Bing,
            'reverse': BingReverse,
        },
        'google': {
            'geocode': Google,
            'reverse': GoogleReverse,
            'timezone': Timezone,
            'elevation': Elevation,
        },
    }
    if isinstance(location, (list, dict)) and method == 'geocode':
        print('[ERROR] Please provide a string as the location.\n'
              '>>> g = geocoder.get("Ottawa ON", provider="google")')
        sys.exit()
    if provider not in options:
        print('[ERROR] Please provide a correct provider\n'
              'Ex: google, bing, osm, here, opencage, tomtom, mapquest\n'
              '$ geocode "Ottawa ON" --provider google\n'
              '>>> g = geocoder.get("Ottawa ON", provider="google")')
        sys.exit()
    else:
        if method not in options[provider]:
            print('[ERROR] Please provide a correct method\n'
                  'Ex: geocode, reverse, timezone, elevation\n'
                  '$ geocode "45.68, -75.15" --method reverse\n'
                  '>>> g = geocoder.get([45.68, -75.15], method="reverse")')
            sys.exit()
    return options[provider][method](location, **kwargs)


def google(location, **kwargs):
    """Google Provider

    :param location: Your search location you want geocoded.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
        > batch
        > timezone
        > elevation
    """
    return get(location, provider='google', **kwargs)


def yandex(location, **kwargs):
    """Yandex Provider

    :param location: Your search location you want geocoded.
    :param lang: Chose the following language:
        > ru-RU — Russian (by default)
        > uk-UA — Ukrainian
        > be-BY — Belarusian
        > en-US — American English
        > en-BR — British English
        > tr-TR — Turkish (only for maps of Turkey)
    :param kind: Type of toponym (only for reverse geocoding):
        > house - house or building
        > street - street
        > metro - subway station
        > district - city district
        > locality - locality (city, town, village, etc.)
    """
    return get(location, provider='yandex', **kwargs)


def w3w(location, **kwargs):
    """what3words Provider

    :param location: Your search location you want geocoded.
    :param key: W3W API key.
    :param method: Chose a method (geocode, method)
    """
    return get(location, provider='w3w', **kwargs)


def baidu(location, **kwargs):
    """Baidu Provider

    :param location: Your search location you want geocoded.
    :param key: Baidu API key.
    :param referer: Baidu API referer website.
    """
    return get(location, provider='baidu', **kwargs)


def ottawa(location, **kwargs):
    """Ottawa Provider

    :param location: Your search location you want geocoded.
    """
    return get(location, provider='ottawa', **kwargs)


def elevation(location, **kwargs):
    """Elevation - Google Provider

    :param location: Your search location you want to retrieve elevation data.
    """
    return get(location, method='elevation', provider='google', **kwargs)


def timezone(location, **kwargs):
    """Timezone - Google Provider

    :param location: Your search location you want to retrieve timezone data.
    :param timestamp: Define your own specified time to calculate timezone.
    """
    return get(location, method='timezone', provider='google', **kwargs)


def reverse(location, provider='google', **kwargs):
    """Reverse Geocoding

    :param location: Your search location you want to reverse geocode.
    :param key: (optional) use your own API Key from Bing.
    :param provider: (default=google) Use the following:
        > google
        > bing
    """
    return get(location, method='reverse', provider=provider, **kwargs)


def bing(location, **kwargs):
    """Bing Provider

    :param location: Your search location you want geocoded.
    :param key: (optional) use your own API Key from Bing.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='bing', **kwargs)


def yahoo(location, **kwargs):
    """Yahoo Provider

    :param ``location``: Your search location you want geocoded.
    """
    return get(location, provider='yahoo', **kwargs)


def geolytica(location, **kwargs):
    """Geolytica (Geocoder.ca) Provider

    :param location: Your search location you want geocoded.
    """
    return get(location, provider='geolytica', **kwargs)


def opencage(location, **kwargs):
    """Opencage Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from OpenCage.
    """
    return get(location, provider='opencage', **kwargs)


def arcgis(location, **kwargs):
    """ArcGIS Provider

    :param ``location``: Your search location you want geocoded.
    """
    return get(location, provider='arcgis', **kwargs)


def here(location, **kwargs):
    """HERE Provider

    :param location: Your search location you want geocoded.
    :param app_code: (optional) use your own Application Code from HERE.
    :param app_id: (optional) use your own Application ID from HERE.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='here', **kwargs)


def nokia(location, **kwargs):
    """HERE Provider

    :param location: Your search location you want geocoded.
    :param app_code: (optional) use your own Application Code from HERE.
    :param app_id: (optional) use your own Application ID from HERE.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='here', **kwargs)


def tomtom(location, **kwargs):
    """TomTom Provider

    :param location: Your search location you want geocoded.
    :param key: (optional) use your own API Key from TomTom.
    """
    return get(location, provider='tomtom', **kwargs)


def mapquest(location, **kwargs):
    """MapQuest Provider

    :param location: Your search location you want geocoded.
    :param key: (optional) use your own API Key from MapQuest.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
    """
    return get(location, provider='mapquest', **kwargs)


def osm(location, **kwargs):
    """OSM Provider

    :param location: Your search location you want geocoded.
    :param url: Custom OSM Server URL location
               (ex: http://nominatim.openstreetmap.org/search)
    """
    return get(location, provider='osm', **kwargs)


def maxmind(location='me', **kwargs):
    """MaxMind Provider

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='maxmind', **kwargs)


def freegeoip(location, **kwargs):
    """FreeGeoIP Provider

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='freegeoip', **kwargs)


def ip(location, **kwargs):
    """IP Address lookup

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your
                                current IP address's location.
    """
    return get(location, provider='maxmind', **kwargs)


def canadapost(location, **kwargs):
    """CanadaPost Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) API Key from CanadaPost Address Complete.
    """
    return get(location, provider='canadapost', **kwargs)


def postal(location, **kwargs):
    """CanadaPost Provider

    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from
                               CanadaPost Address Complete.
    """
    return get(location, provider='canadapost', **kwargs)


def geonames(location, **kwargs):
    """GeoNames Provider

    :param ``location``: Your search location you want geocoded.
    :param ``username``: (required) needs to be passed with each request.
    """
    return get(location, provider='geonames', **kwargs)
