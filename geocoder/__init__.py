# -*- coding: utf-8 -*-

__title__ = 'geocoder'
__version__ = '0.1.90'
__author__ = 'Denis Carriere'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'

from geocoder import Geocoder
from google import Google
from bing import Bing
from maxmind import Maxmind
from nokia import Nokia
from esri import Esri
from mapquest import Mapquest
from osm import Osm
from tomtom import Tomtom


def google(location):
    return Geocoder(Google(location))

def bing(location, key=''):
    return Geocoder(Bing(location, key))

def maxmind(location):
    return Geocoder(Maxmind(location))

def ip(location):
    return maxmind(location)

def nokia(location, app_id='', app_code=''):
    return Geocoder(Nokia(location, app_id, app_code))

def esri(location):
    return Geocoder(Esri(location))

def mapquest(location):
    return Geocoder(Mapquest(location))

def osm(location):
    return Geocoder(Osm(location))

def tomtom(location):
    return Geocoder(Tomtom(location))


