#!/usr/bin/env python

from distutils.core import setup

setup(name='Geocoder',
      version='0.1.3',
      description='Python Geocoder (Google, Bing, OSM, ESRI, MaxMind, Mapquest, Nokia, Geolytica)',
      author='Denis Carriere',
      author_email='info@addxy.com',
      url='http://addxy.com',
      download_url='https://github.com/DenisCarriere/geocoder.git',
      packages=['geocoder'],
      keywords = [
        'geocode',
        'geocoder', 
        'geocoding', 
        'lat', 'lng', 'latitude', 'longitude', 'x', 'y', 'xy', 'latlng'
        'google', 
        'bing',
        'nokia',
        'tomtom',
        'esri',
        'osm',
        'mapquest',
        'maxmind',
        'geolytica']
      )