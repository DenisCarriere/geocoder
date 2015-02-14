#!/usr/bin/python
# coding: utf8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# auto-convert README.md
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (ImportError, OSError):
    # we'll just use the poorly formatted Markdown file instead
    long_description = open('README.md').read()

install_requires = ['requests', 'ratelim']
setup_requires = ['tox', 'nose', 'flake8']

setup(
    name='geocoder',
    version='1.1.3',
    description="A complete Python Geocoding module made easy.",
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
    package_data={'': ['LICENSE', 'README.rst']},
    package_dir={'geocoder': 'geocoder'},
    include_package_data=True,
    setup_requires=setup_requires,
    install_requires=install_requires,
    zip_safe=False,
    keywords='geocoder arcgis tomtom opencage google bing mapquest nokia osm lat lng location addxy',
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
