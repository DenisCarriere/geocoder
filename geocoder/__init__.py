#!/usr/bin/python
# coding: utf8

"""
geocoder library
~~~~~~~~~~~~~~~~

A pure Python Geocoding module made easy.

Every task is made easy with tons of ``help`` & ``debug`` commands!

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.google.geocode('<address>')
    >>> g.lat, g.lng
    45.413140 -75.656703
    ...

"""

__title__ = 'geocoder'
__author__ = 'Denis Carriere'
__author_email__ = 'carriere.denis@gmail.com'
__version__ = '1.0.2'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2013-2015 Denis Carriere'

# CORE
from .api import get, yahoo, bing, geonames, google, mapquest
from .api import nokia, osm, tomtom, geolytica, arcgis, opencage

# EXTRAS
from .api import timezone, elevation, ip, canadapost, reverse

# CLI
from cli import cli
