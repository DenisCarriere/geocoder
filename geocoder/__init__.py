# -*- coding: utf-8 -*-

__title__ = 'geocoder'
__version__ = '0.2.1'
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


