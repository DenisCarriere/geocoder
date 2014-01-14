#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ['requests']

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

setup(name = 'Geocoder',
      version = '0.1.3',
      long_description = readme + '\n\n' + history,
      description = 'Python Geocoder (Google, Bing, OSM, ESRI, MaxMind, Mapquest, Nokia, Geolytica)',
      author = 'Denis Carriere',
      author_email = 'info@addxy.com',
      url = 'http://addxy.com',
      download_url = 'https://github.com/DenisCarriere/geocoder.git',
      packages = ['geocoder'],
      install_requires = requires,
      include_package_data=True,
      zip_safe=False,
      keywords = [
        'geocode', 'geocoder', 'geocoding', 
        'lat', 'lng', 'latitude', 'longitude', 'x', 'y', 'xy', 'latlng'
        'google', 'bing', 'nokia', 'tomtom', 'esri', 'osm', 'mapquest', 'maxmind', 'geolytica'],
      classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),

)