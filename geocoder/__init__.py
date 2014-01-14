# -*- coding: utf-8 -*-

__title__ = 'geocoder'
__version__ = '0.1.3'
__author__ = 'Denis Carriere'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'

from geocoder import Geocoder

def google(location, proxies=''):
    return Geocoder(location=location, source='google', proxies=proxies)

def bing(location, proxies=''):
    return Geocoder(location=location, source='bing', proxies=proxies)

def maxmind(location, proxies=''):
    return Geocoder(location=location, source='maxmind', proxies=proxies)

def nokia(location, proxies=''):
    return Geocoder(location=location, source='nokia', proxies=proxies)

def esri(location, proxies=''):
    return Geocoder(location=location, source='esri', proxies=proxies)

def geolytica(location, proxies=''):
    return Geocoder(location=location, source='geolytica', proxies=proxies)

def mapquest(location, proxies=''):
    return Geocoder(location=location, source='mapquest', proxies=proxies)

def osm(location, proxies=''):
    return Geocoder(location=location, source='osm', proxies=proxies)

def tomtom(location, proxies=''):
    return Geocoder(location=location, source='tomtom', proxies=proxies)


