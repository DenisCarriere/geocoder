#!/usr/bin/python
# coding: utf8

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.6.2'
requires = ['requests>=2.3.0', 'xmltodict>=0.9.0']

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='geocoder',
    version=version,
    description="A simplistic Python Geocoder (Google, Bing, OSM & more)",
    long_description=readme,
    author='Denis Carriere',
    author_email='carriere.denis@gmail.com',
    url='https://github.com/DenisCarriere/geocoder',
    download_url='https://github.com/DenisCarriere/geocoder/tarball/master',
    license=license,
    packages=['geocoder'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'geocoder': 'geocoder'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='geocoder google lat lng location addxy',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
