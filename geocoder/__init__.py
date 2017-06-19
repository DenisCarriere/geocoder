#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

"""
Geocoder
~~~~~~~~

Simple and consistent geocoding library written in Python.

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

Consistant JSON responses from various providers.

    >>> g = geocoder.google('New York City')
    >>> g.latlng
    [40.7127837, -74.0059413]
    >>> g.state
    'New York'
    >>> g.json
    ...

"""

__title__ = 'geocoder'
__author__ = 'Denis Carriere'
__author_email__ = 'carriere.denis@gmail.com'
__version__ = '1.23.0'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2013-2016 Denis Carriere'

# CORE
from geocoder.api import get, yahoo, bing, geonames, mapquest, google, mapbox  # noqa
from geocoder.api import nokia, osm, tomtom, geolytica, arcgis, opencage  # noqa
from geocoder.api import maxmind, ipinfo, freegeoip, ottawa, here, baidu, w3w  # noqa
from geocoder.api import yandex, mapzen, komoot, tamu, geocodefarm, tgos, uscensus  # noqa

# EXTRAS
from geocoder.api import timezone, elevation, places, ip, canadapost, reverse, distance, location  # noqa

# CLI
from geocoder.cli import cli  # noqa
