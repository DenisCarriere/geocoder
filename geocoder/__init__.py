# -*- coding: utf-8 -*-

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

"""

__title__ = 'geocoder'
__version__ = '0.3.7'
__author__ = 'Denis Carriere'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Denis Carriere'

from geocoder import Geocoder
from osm import Osm
from bing import Bing
from nokia import Nokia
from arcgis import Arcgis
from tomtom import Tomtom
from google import Google
from maxmind import Maxmind
from mapquest import Mapquest

def google(location, proxies=''):
    """
    Retrieves geocoding data from Google's geocoding API V3

    >>> g = geocoder.google('Ottawa, Ontario')
    >>> g.latlng
    (45.4215296, -75.69719309999999)
    >>> g.country
    'Canada'

    Official Docs
    -------------
    https://developers.google.com/maps/documentation/geocoding/
    """
    return Geocoder(Google(location=location, proxies=proxies))

def ip(location):
    """
    Geocodes an IP address using MaxMind's services.

    >>> g = geocoder.ip('74.125.226.99')
    >>> g.latlng
    (37.4192, -122.0574)
    >>> g.address
    'Mountain View, California United States'

    Official Docs
    -------------
    http://www.maxmind.com/en/geolocation_landing
    """
    return maxmind(location)

def reverse(lat, lng='', proxies=''):
    """
    Reverse geocodes a location based on Lat & Lng inputs 
    using Google's reverse geocoding API V3.

    >>> latlng = (37.4192, -122.0574)
    >>> g = geocoder.reverse(latlng)
    >>> g.address
    'Sevryns Road, Mountain View, CA 94043, USA'
    >>> g.postal
    '94043'

    Official Docs
    -------------
    https://developers.google.com/maps/documentation/geocoding/#ReverseGeocoding
    """
    return Geocoder(Google(location='', lat=lat, lng=lng, proxies=proxies))

def osm(location):
    """
    Retrieves geocoding data from OSM's data using Nominatim's geocoding API.

    >>> g = geocoder.osm('Tacloban City')
    >>> g.latlng
    (11.2430274, 125.0081402)
    >>> g.country
    'Philippines'

    Official Docs
    -------------
    http://wiki.openstreetmap.org/wiki/Nominatim
    """
    return Geocoder(Osm(location))

def arcgis(location):
    """
    Retrieves geocoding data from ArcGIS's REST geocoding API.

    >>> g = geocoder.arcgis('380 New York St, Redlands, California')
    >>> g.latlng
    (34.05649072776595, -117.19566584280369)
    >>> g.postal
    '92373'

    Official Docs
    -------------
    http://resources.arcgis.com/en/help/arcgis-rest-api/
    """
    return Geocoder(Arcgis(location))

def mapquest(location):
    """
    Retrieves geocoding data from MapQuest's address geocoding API.

    >>> g = geocoder.mapquest('1555 Blake street, Denver')
    >>> g.latlng
    (39.740009, -104.992264)
    >>> g.quality
    'CITY'
    
    Official Docs
    -------------
    http://www.mapquestapi.com/geocoding/
    """
    return Geocoder(Mapquest(location))

def tomtom(location, key=''):
    """
    Retrieves geocoding data from TomTom's geocoding API.

    >>> key = 'XXXXX'
    >>> g = geocoder.tomtom('Amsterdam, Netherlands', key=key)
    >>> g.latlng
    (52.373166, 4.89066)
    >>> g.quality
    'city'

    Official Docs
    -------------
    http://developer.tomtom.com/products/geocoding_api
    """
    return Geocoder(Tomtom(location))

def bing(location, key=''):
    """
    Retrieves geocoding data from Bing's REST location API.

    >>> key = 'XXXXX'
    >>> g = geocoder.bing('Medina, Washington', key=key)
    >>> g.latlng
    (47.615821838378906, -122.23892211914062)
    >>> g.country
    'United States'

    Official Docs
    -------------
    http://msdn.microsoft.com/en-us/library/ff701714.aspx
    """
    return Geocoder(Bing(location, key))

def nokia(location, app_id='', app_code=''):
    """
    Retrieves geocoding data from Nokia's HERE geocoder API.

    >>> app_id = 'XXXXX'
    >>> app_code = 'XXXXX'
    >>> g = geocoder.nokia('Keilaniemi, Espoo')
    >>> g.latlng
    (60.1759338, 24.8327808)
    >>> g.country
    'FIN'

    Official Docs
    -------------
    https://developer.here.com/rest-apis/documentation/geocoder/topics/resources.html
    """

    return Geocoder(Nokia(location, app_id, app_code))
