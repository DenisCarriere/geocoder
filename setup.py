#!/usr/bin/env python

from distutils.core import setup

setup(name='Geocode',
      version='1.0',
      description='Python Geocoder',
      author='Denis Carriere',
      author_email='info@addxy.com',
      url='http://addxy.com',
      packages=['geocode.google', 'geocode.maxmind'],
     )