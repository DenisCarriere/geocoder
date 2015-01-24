#!/usr/bin/python
# coding: utf8

from .keys import *
from .osm import Osm
from .bing import Bing
from .nokia import Nokia
from .yahoo import Yahoo
from .tomtom import Tomtom
from .google import Google
from .arcgis import Arcgis
from .ottawa import Ottawa
from .maxmind import Maxmind
from .opencage import OpenCage
from .geonames import Geonames
from .mapquest import Mapquest
from .timezone import Timezone
from .elevation import Elevation
from .geolytica import Geolytica
from .freegeoip import FreeGeoIP
from .canadapost import Canadapost
from .bing_reverse import BingReverse
from .google_reverse import GoogleReverse
from .mapquest_reverse import MapquestReverse
from .opencage_reverse import OpenCageReverse


def get(location, **kwargs):
    """Get Geocode

    :param ``location``: Your search location you want geocoded.
    :param ``provider``: The geocoding engine you want to use.
    :param ``reverse``: Use True to apply a reverse geocoding to a LatLng input.
    """
    kwargs.setdefault('method', 'geocode')
    provider = kwargs.get('provider','').lower().strip()
    method = kwargs.get('method','').lower().strip()
    options = {
        'osm': {'geocode': Osm},
        'nokia': {'geocode': Nokia},
        'yahoo': {'geocode': Yahoo},
        'tomtom': {'geocode': Tomtom},
        'arcgis': {'geocode': Arcgis},
        'ottawa': {'geocode': Ottawa},
        'maxmind': {'geocode': Maxmind},
        'geonames': {'geocode': Geonames},
        'freegeoip': {'geocode': FreeGeoIP},
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
    return options[provider][method](location, **kwargs)

def google(location, **kwargs):
    """Google Provider

    :param location: Your search location you want geocoded.
    :param short_name: (optional) if ``False`` will retrieve the results with Long names.
    :param method: (default=geocode) Use the following:
        > geocode
        > reverse
        > batch
        > timezone
        > elevation
    """
    return get(location, provider='google', **kwargs)

def ottawa(location, **kwargs):
    """Ottawa Provider

    :param location: Your search location you want to retrieve elevation data.
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

def nokia(location, **kwargs):
    """Nokia Provider
    
    :param location: Your search location you want geocoded.
    :param app_code: (optional) use your own Application Code from Nokia.
    :param app_id: (optional) use your own Application ID from Nokia.
    """
    return get(location, provider='nokia', **kwargs)

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
    """
    return get(location, provider='osm', **kwargs)

def maxmind(location='me', **kwargs):
    """MaxMind Provider

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your current IP address's location.
    """
    return get(location, provider='maxmind', **kwargs)

def freegeoip(location, **kwargs):
    """FreeGeoIP Provider

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your current IP address's location.
    """
    return get(location, provider='freegeoip', **kwargs)

def ip(location, **kwargs):
    """IP Address lookup

    :param location: Your search IP Address you want geocoded.
    :param location: (optional) if left blank will return your current IP address's location.
    """
    return get(location, provider='maxmind', **kwargs)

def canadapost(location, **kwargs):
    """CanadaPost Provider
    
    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from CanadaPost Address Complete.
    """
    return get(location, provider='canadapost', **kwargs)

def postal(location, **kwargs):
    """CanadaPost Provider
    
    :param ``location``: Your search location you want geocoded.
    :param ``key``: (optional) use your own API Key from CanadaPost Address Complete.
    """
    return get(location, provider='canadapost', **kwargs)

def geonames(location, **kwargs):
    """GeoNames Provider
    
    :param ``location``: Your search location you want geocoded.
    :param ``username``: (required) needs to be passed with each request.
    """
    return get(location, provider='geonames', **kwargs)

