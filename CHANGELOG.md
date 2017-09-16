<!-- markdownlint-disable -->
# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

Table of releases
-----------------

<!-- TOC depthFrom:2 depthTo:2 orderedList:false -->

- [[Unreleased]](#unreleased)
- [[1.32.1] - 2017-09-16](#1321---2017-09-16)
- [[1.32.0] - 2017-09-11](#1320---2017-09-11)
- [[1.31.0] - 2017-09-06](#1310---2017-09-06)
- [[1.30.1] - 2017-08-29](#1301---2017-08-29)
- [[1.29.1] - 2017-08-22](#1291---2017-08-22)
- [[1.28.0] - 2017-08-19](#1280---2017-08-19)
- [[1.27.0] - 2017-08-14](#1270---2017-08-14)
- [[1.26.0] - 2017-08-11](#1260---2017-08-11)
- [[1.25.0] - 2017-08-04](#1250---2017-08-04)
- [[1.24.1] - 2017-08-02](#1241---2017-08-02)

<!-- /TOC -->

## [Unreleased]

## [1.32.1] - 2017-09-16

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.32.1) - PR [#289](https://github.com/DenisCarriere/geocoder/pull/289) & PR [#293](https://github.com/DenisCarriere/geocoder/pull/293) - (coverage 86%)**

* added coverage badge on README
* improved test coverage calling debug in majority of providers
* fixed debug() function to be compatible with python 2.7
* fixed all providers parsing on geocode method: no errors if some fields are not found in the JSON
* restaured backward compatibility: no errors when trying to access data on a result which is not OK


## [1.32.0] - 2017-09-11

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.32.0) - PR [#288](https://github.com/DenisCarriere/geocoder/pull/288) - (coverage 83%)**

- added pretty 'header' in README.md
- added Changelog (this file)
- refactored canadapost, moving key getter in keys.py
- refactored mapzen
- refactored ottawa
- refactored tomtom
- refactored yandex
- refactored tgos
- refactored opencage
- refactored maxmind
- refactored komoot
- refactored yahoo
- refactored baidu
- refactored gaode
- fixed `base.py: MultipleResultsQuery._catch_errors` which was not returning errors most of the time
- fixed issue #207: tomtom, making use of new API


## [1.31.0] - 2017-09-06

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.31.0) - [PR #286](https://github.com/DenisCarriere/geocoder/pull/286) - (coverage 73%)**

- added class attribute `_KEY_MANDATORY` [default to True]
- refactored freegeoip, also changed url
- refactored geocodefarm
- refactored ipinfo
- refactored geolytica
- refactored here
- refactored tamu
- fixed with PR #287: Allow tamu requests without zip code
- fixed issue #215: Unofficial endpoint for FreeGeoIP causes intermittent errors


## [1.30.1] - 2017-08-29

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.30.1)**

- refactored w3w
- refactored ipinfo
- refactored arcgis
- refactored osm
- fixed issue #154: Add ArcGIS Reverse geocoding
- fixed issue #279: Google client keys don't get picked up
- fixed issue #282: Accuracy is always None in 1.29.1 with Google Geocode
- fixed issue #260: updating what3words provider to use API v2


## [1.29.1] - 2017-08-22

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.29.1)**

- added refactoring guide
- fixed issue #276: Opencage geocoder circular lookup for Town


## [1.28.0] - 2017-08-19

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.28.0)**

- added Baidu reverse and Gaode providers (old style)


## [1.27.0] - 2017-08-14

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.27.0)**

- added doc and test to proximity + BBox


## [1.26.0] - 2017-08-11

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.26.0)**

- added `proximity` argument when geocoding with geonames, google, mapbox
- added `BBox` helper class
- added Snap
- refactored Google
- refactored mapquest
- refactored mapbox
- refactored bing
- fixed issue #272: Install with python 3.5 29 days ago
- fixed issue #270: Orderedset can't be installed without C++? 

## [1.25.0] - 2017-08-04

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.25.0)**

- added documentation on Work In Progress (mutiple results)
- fixed builds, passing again


## [1.24.1] - 2017-08-02

**[See on Pypi](https://pypi.python.org/pypi/geocoder/1.24.1) (Coverage 54%)**

- added coverage in make file
- refactored base.py to add support for multiple results with geonames. 