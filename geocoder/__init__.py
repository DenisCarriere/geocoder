# -*- coding: utf-8 -*-

__title__ = 'geocoder'
__version__ = '0.1.0'
__author__ = 'Denis Carriere'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'


from geocoder import *



def google(location, proxy=''):
    return Geocode(location=location, source='google', proxy=proxy)

def bing(location, proxy=''):
    return Geocode(location=location, source='bing', proxy=proxy)

def maxmind(location, proxy=''):
    return Geocode(location=location, source='maxmind', proxy=proxy)

def nokia(location, proxy=''):
    return Geocode(location=location, source='nokia', proxy=proxy)

def esri(location, proxy=''):
    return Geocode(location=location, source='esri', proxy=proxy)

def geolytica(location, proxy=''):
    return Geocode(location=location, source='geolytica', proxy=proxy)

def mapquest(location, proxy=''):
    return Geocode(location=location, source='mapquest', proxy=proxy)

def osm(location, proxy=''):
    return Geocode(location=location, source='osm', proxy=proxy)




