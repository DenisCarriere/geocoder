#!/usr/bin/python
# coding: utf8

"""
geocoder library
~~~~~~~~~~~~~~~~

A simplistic Python Geocoder.

Geocoder is an Apache2 Licensed Geocoding library, written in Python.

    >>> import geocoder
    >>> g = geocoder.google('Moscone Center')
    >>> g.latlng
    (37.784173, -122.401557)
    >>> g.city
    'San Francisco'
    ...

"""

__title__ = 'geocoder'
__version__ = '0.6.2'
__author__ = 'Denis Carriere'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'


from api import arcgis, bing, geonames, google, mapquest, nokia, osm, tomtom
from api import get, population, reverse, ip, canadapost, geolytica
from api import timezone, elevation
