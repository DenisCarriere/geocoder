# -*- coding: utf-8 -*-

__title__ = 'geocoder'
__version__ = '0.2.6'
__author__ = 'Denis Carriere'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'

from geocoder import Geocoder
from osm import Osm
from esri import Esri
from bing import Bing
from nokia import Nokia
from tomtom import Tomtom
from google import Google
from maxmind import Maxmind
from mapquest import Mapquest

def google(location, proxies=''):
    return Geocoder(Google(location, proxies=proxies))

def maxmind(location):
    return Geocoder(Maxmind(location))

def ip(location):
    return maxmind(location)

def esri(location):
    return Geocoder(Esri(location))

def mapquest(location):
    return Geocoder(Mapquest(location))

def osm(location):
    return Geocoder(Osm(location))

def tomtom(location, key=''):
    return Geocoder(Tomtom(location))

def bing(location, key=''):
    return Geocoder(Bing(location, key))

def nokia(location, app_id='', app_code=''):
    return Geocoder(Nokia(location, app_id, app_code))

def get(location, provider='google', proxies='', key='', app_id='', app_code=''):
    provider = provider.lower()
    options = {
        'google': google,
        'ip': maxmind,
        'maxmind': maxmind,
        'esri': esri,
        'mapquest': mapquest,
        'osm': osm,
        'tomtom': tomtom,
        'bing': bing,
        'tomtom': tomtom,
        'nokia': nokia,
    }
    if provider in ['google']:
        return options[provider](location, proxies=proxies)
    elif provider in ['bing', 'tomtom']:
        return options[provider](location, key=key)
    elif provider in ['nokia']:
        return options[provider](location, app_id='', app_code='')
    elif provider in ['osm', 'mapquest', 'maxmind', 'ip', 'esri']:
        return options[provider](location)
    else:
        raise 'ERROR - Please provide a valid <Provider> (ex: Google, Bing, Nokia)'
