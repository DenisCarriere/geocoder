#!/usr/bin/env python

import sys
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = [
    'requests>=2.2.0',
    'haversine>=0.1'
]

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist --formats=gztar upload')
    sys.exit()

entry_points = dict()
entry_points['console_scripts'] = ['geocoder = geocoder:_main', ]

with open('README.rst') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

here = os.path.dirname(os.path.abspath(__file__))

def get_version():
    f = open(os.path.join(here, 'geocoder/__init__.py'))
    version_file = f.read()
    f.close()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(
    name='geocoder',
    version=get_version(),
    long_description=readme,
    description="A simplistic Python Geocoder (Google, Bing, OSM & more)",
    author='Denis Carriere',
    author_email='carriere.denis@gmail.com',
    url='http://addxy.com',
    download_url='https://github.com/DenisCarriere/geocoder/tarball/master',
    license=license,
    entry_points=entry_points,
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
