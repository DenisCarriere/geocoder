#!/usr/bin/python
# coding: utf8
from setuptools import setup

__version__ = '1.2.4'
requirements_file = "requirements.txt"
requirements = [pkg.strip() for pkg in open(requirements_file).readlines()]

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst') + "\n"
except(IOError, ImportError):
    long_description = open('README.md').read() + "\n"

setup(
    name='geocoder',
    version=__version__,
    description="Geocoder is a geocoding library, written in python,"
                " simple and consistent.",
    long_description=long_description,
    author='Denis Carriere',
    author_email='carriere.denis@gmail.com',
    url='https://github.com/DenisCarriere/geocoder',
    download_url='https://github.com/DenisCarriere/geocoder/tarball/master',
    license=open('LICENSE').read(),
    entry_points='''
        [console_scripts]
        geocode=geocoder.cli:cli
    ''',
    packages=['geocoder'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'geocoder': 'geocoder'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='geocoder arcgis tomtom opencage google bing here',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
