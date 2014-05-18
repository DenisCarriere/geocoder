#!/usr/bin/env python

import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = [
    'requests>=2.2.0'
]

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist --formats=gztar upload')
    sys.exit()

with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='geocoder',
    version='0.5.6',
    long_description=readme,
    description="A simplistic Python Geocoder (Google, Bing, OSM & more)",
    author='Denis Carriere',
    author_email='carriere.denis@gmail.com',
    url='http://addxy.com',
    download_url='https://github.com/DenisCarriere/geocoder/tarball/master',
    license=license,
    packages=['geocoder'],
    package_data={'': ['LICENSE', 'README.rst']},
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
