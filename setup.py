#!/usr/bin/env python

import geocoder

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requires = ['requests>=2.2.0']

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
    'geocode', 'geocoder', 'geocoding', 'ip',
    'lat', 'lng', 'latitude', 'longitude', 'x', 'y', 'xy', 'latlng',
    'google', 'bing', 'nokia', 'tomtom', 'esri', 'osm', 'mapquest', 'maxmind'
]

setup(name = 'geocoder',
      version = geocoder.__version__,
      license = 'Apache 2.0',
      long_description = readme,
      description = 'Python Geocoder (Google, Bing, OSM, TomTom, ESRI, MaxMind, Mapquest, Nokia)',
      author = 'Denis Carriere',
      author_email = 'info@addxy.com',
      url = 'http://addxy.com',
      include_package_data=True,
      install_requires=requires,
      packages = find_packages(),
      keywords = keywords,
      classifiers = classifiers,
     )