# -*- coding: utf-8 -*-

__title__ = 'geocoder'
__version__ = '0.1.9'
__author__ = 'Denis Carriere'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'

from geocoder import Geocoder

def google(location):
    from google import Google

    return Geocoder(Google(location))

def bing(location, key=''):
    from bing import Bing
    return Geocoder(Bing(location, key))

def maxmind(location):
    from maxmind import Maxmind

    return ip(location)

def ip(location):
    return maxmind(location)

def nokia(location, app_id='', app_code=''):
    from nokia import Nokia

    return Geocoder(Nokia(location, app_id, app_code))

def esri(location):
    from esri import Esri

    return Geocoder(Esri(location))

def mapquest(location):
    from mapquest import Mapquest

    return Geocoder(Mapquest(location))

def osm(location):
    from osm import Osm

    return Geocoder(Osm(location))

def tomtom(location):
    from tomtom import Tomtom

    return Geocoder(Tomtom(location))


