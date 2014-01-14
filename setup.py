#!/usr/bin/env python

from distutils.core import setup

import geocode


with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

classifiers = [
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
]

keywords = [
    'geocode', 'geocoder', 'geocoding', 
    'lat', 'lng', 'latitude', 'longitude', 'x', 'y', 'xy', 'latlng',
    'google', 'bing', 'nokia', 'tomtom', 'esri', 'osm', 'mapquest', 'maxmind', 'geolytica'
]

setup(name = 'geocoder',
      version = '0.1.6',
      platform = ['Python 2.7'],
      license = 'Apache 2.0',
      long_description = readme + '\n\n' + history,
      install_requires = ['requests'],
      description = 'Python Geocoder (Google, Bing, OSM, ESRI, MaxMind, Mapquest, Nokia, Geolytica)',
      author = 'Denis Carriere',
      author_email = 'carriere.denis@gmail.com',
      url = 'https://github.com/DenisCarriere/geocoder.git',
      download_url = 'https://github.com/DenisCarriere/geocoder.git',
      packages = ['geocoder'],
      zip_safe = False,
      keywords = keywords,
      classifiers = classifiers,
     )