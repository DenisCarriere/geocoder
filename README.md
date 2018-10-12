<!-- markdownlint-disable -->
<h1 align="center" style="margin:1em">
  <a href="https://geocoder.readthedocs.org/">
    <img src="https://github.com/DenisCarriere/geocoder/raw/master/docs/_static/geocoder.png"
         alt="Markdownify"
         width="200"></a>
  <br />
  Python Geocoder
</h1>

<h4 align="center">
  Simple and consistent geocoding library written in Python.
</h4>

<p align="center">
  <a href="http://geocoder.readthedocs.io/?badge=master">
    <img src="https://readthedocs.org/projects/geocoder/badge/?version=master"
         alt="RDT">
  </a>
  <a href="https://pypi.python.org/pypi/geocoder">
    <img src="https://img.shields.io/pypi/v/geocoder.svg"
         alt="PyPi">
  </a>
  <a href="https://build.snapcraft.io/user/DenisCarriere/geocoder">
    <img src="https://build.snapcraft.io/badge/DenisCarriere/geocoder.svg"
         alt="Snap">
  </a>
  <a href="https://travis-ci.org/DenisCarriere/geocoder">
    <img src="https://travis-ci.org/DenisCarriere/geocoder.svg?branch=master"
         alt="Travis">
  </a>
  <a href="https://codecov.io/gh/DenisCarriere/geocoder">
    <img src="https://codecov.io/gh/DenisCarriere/geocoder/branch/master/graph/badge.svg"
         alt="Codecov" />
  </a>
</p>
<br>

Table of content
----------------

<!-- TOC -->

- [Overview](#overview)
- [A glimpse at the API](#a-glimpse-at-the-api)
    - [Forward](#forward)
    - [Multiple results](#multiple-results)
    - [Reverse](#reverse)
    - [House Addresses](#house-addresses)
    - [IP Addresses](#ip-addresses)
    - [Bounding Box](#bounding-box)
- [Command Line Interface](#command-line-interface)
- [Providers](#providers)
- [Installation](#installation)
    - [PyPi Install](#pypi-install)
    - [GitHub Install](#github-install)
    - [Snap Install](#snap-install)
- [Feedback](#feedback)
- [Contribution](#contribution)
    - [Documenting](#documenting)
    - [Coding](#coding)
- [ChangeLog](#changelog)

<!-- /TOC -->

## Overview

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

It can be very difficult sometimes to parse a particular geocoding provider
since each one of them have their own JSON schema.

Here is a typical example of retrieving a Lat & Lng from Google using Python,
things shouldn't be this hard.

```python
>>> import requests
>>> url = 'https://maps.googleapis.com/maps/api/geocode/json'
>>> params = {'sensor': 'false', 'address': 'Mountain View, CA'}
>>> r = requests.get(url, params=params)
>>> results = r.json()['results']
>>> location = results[0]['geometry']['location']
>>> location['lat'], location['lng']
(37.3860517, -122.0838511)
```

Now lets use Geocoder to do the same task

```python
>>> import geocoder
>>> g = geocoder.google('Mountain View, CA')
>>> g.latlng
(37.3860517, -122.0838511)
```

## A glimpse at the API

Many properties are available once the geocoder object is created.

### Forward

```python
>>> import geocoder
>>> g = geocoder.google('Mountain View, CA')
>>> g.geojson
>>> g.json
>>> g.wkt
>>> g.osm
```

### Multiple queries ('batch' geocoding)

```python
>>> import geocoder
>>> g = geocoder.mapquest(['Mountain View, CA', 'Boulder, Co'], method='batch')
>>> for result in g:
...   print(result.address, result.latlng)
...
('Mountain View', [37.39008, -122.08139])
('Boulder', [40.015831, -105.27927])
```

### Multiple results

```python
>>> import geocoder
>>> g = geocoder.geonames('Mountain View, CA', maxRows=5)
>>> print(len(g))
5
>>> for result in g:
...   print(result.address, result.latlng)
...
Mountain View ['37.38605', '-122.08385']
Mountain View Elementary School ['34.0271', '-117.59116']
Best Western Plus Mountainview Inn and Suites ['51.79516', '-114.62793']
Best Western Mountainview Inn ['49.3338', '-123.1446']
Mountain View Post Office ['37.393', '-122.07774']
```


> The providers currently supporting multiple results are listed in the table [below](#providers).

### Reverse

```python
>>> g = geocoder.google([45.15, -75.14], method='reverse')
>>> g.city
>>> g.state
>>> g.state_long
>>> g.country
>>> g.country_long
```

### House Addresses

```python
>>> g = geocoder.google("453 Booth Street, Ottawa ON")
>>> g.housenumber
>>> g.postal
>>> g.street
>>> g.street_long
```

### IP Addresses

```python
>>> g = geocoder.ip('199.7.157.0')
>>> g = geocoder.ip('me')
>>> g.latlng
>>> g.city
```

### Bounding Box

Accessing the JSON & GeoJSON attributes will be different

```python
>>> g = geocoder.google("Ottawa")
>>> g.bbox
{"northeast": [45.53453, -75.2465979], "southwest": [44.962733, -76.3539158]}

>>> g.geojson['bbox']
[-76.3539158, 44.962733, -75.2465979, 45.53453]

>>> g.southwest
[44.962733, -76.3539158]
```

## Command Line Interface

```bash
$ geocode "Ottawa, ON"  >> ottawa.geojson
$ geocode "Ottawa, ON" \
    --provide google \
    --out geojson \
    --method geocode
```

## Providers

| Provider                       | Optimal   | Usage Policy                    | Multiple results | Reverse | Proximity | Batch |
|:-------------------------------|:----------|:--------------------------------|:-----------------|:--------|:----------|:------|
| [ArcGIS][ArcGIS]               | World     |                                 | yes              | yes     |           |       |
| [Baidu][Baidu]                 | China     | API key                         |                  | yes     |           |       |
| [Bing][Bing]                   | World     | API key                         | yes              | yes     |           | yes   |
| [CanadaPost][CanadaPost]       | Canada    | API key                         | yes              |         |           |       |
| [FreeGeoIP][FreeGeoIP] This API endpoint is deprecated and will stop working on July 1st, 2018.         | World     | Rate Limit, [Policy][FreeGeoip-Policy]                |                  |         |           |       |
| [Gaode][Gaode]                 | China     | API key                         |                  | yes     |           |       |
| [Geocoder.ca][Geocoder.ca] (Geolytica) | CA & US | Rate Limit                |                  |         |           |       |
| [GeocodeFarm][GeocodeFarm]     | World     | [Policy][GeocodeFarm-Policy]    | yes              | yes     |           |       |
| [GeoNames][GeoNames]           | World     | Username                        | yes              |         | yes       |       |
| [GeoOttawa][GeoOttawa]         | Ottawa    |                                 | yes              |         |           |       |
| [Gisgraphy][Gisgraphy]         | World     | API key                         | yes              | yes     | yes       |       |
| [Google][Google]               | World     | Rate Limit, [Policy][G-Policy]  | yes              | yes     | yes       |       |
| [HERE][HERE]                   | World     | API key                         | yes              | yes     |           |       |
| [IPInfo][IPInfo]               | World     | Rate Limit, [Plans][IP-Plans]   |                  |         |           |       |
| [Komoot][Komoot] (OSM powered) | World     |                                 | yes              | yes     |           |       |
| [LocationIQ][LocationIQ]       | World     | API Key                         | yes              | yes     |           |       |
| [Mapbox][Mapbox]               | World     | API key                         | yes              | yes     | yes       |       |
| [MapQuest][MapQuest]           | World     | API key                         | yes              | yes     |           | yes   |
| [~~Mapzen~~][Mapzen]           | Shutdown  | API key                         | yes              | yes     |           |       |
| [MaxMind][MaxMind]             | World     |                                 |                  |         |           |       |
| [OpenCage][OpenCage]           | World     | API key                         | yes              | yes     |           |       |
| [OpenStreetMap][OpenStreetMap] | World     | [Policy][OpenStreetMap-Policy]  | yes              | yes     |           |       |
| [Tamu][Tamu]                   | US        | API key                         |                  |         |           |       |
| [TGOS][TGOS]                   | Taiwan    |                                 |                  |         |           |       |
| [TomTom][TomTom]               | World     | API key                         | yes              |         |           |       |
| [USCensus][USCensus]           | US        |                                 |                  | yes     |           | yes   |
| [What3Words][What3Words]       | World     | API key                         |                  | yes     |           |       |
| [Yahoo][Yahoo]                 | World     |                                 |                  |         |           |       |
| [Yandex][Yandex]               | Russia    |                                 | yes              | yes     |           |       |

## Installation

### PyPi Install

To install Geocoder, simply:

```bash
$ pip install geocoder
...
```

### GitHub Install

Installing the latest version from Github:

```bash
$ git clone https://github.com/DenisCarriere/geocoder
...
$ cd geocoder
$ python setup.py install
...
```

### Snap Install

To install the stable geocoder [snap](https://snapcraft.io) in any of the [supported Linux distros](https://snapcraft.io/docs/core/install):

```bash
$ sudo snap install geocoder
...
```

If you want to help testing the latest changes from the master branch, you can install it from the edge channel:

```bash
$ sudo snap install geocoder --edge
...
```

The installed snap will be updated automatically every time a new version is pushed to the store.


## Feedback

Please feel free to give any feedback on this module.

Speak up on Twitter [@DenisCarriere](https://twitter.com/DenisCarriere) and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [#python](https://twitter.com/search?q=%23python).

## Contribution

If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page](https://github.com/DenisCarriere/geocoder/issues).

Some way to contribute, from the most generic to the most detailed:

### Documenting

If you are not comfortable with development, you can still contribute with the documentation.

- review the documentation of a specific provider. Most of the time they are lacking details...
- review the parameters for a specific method, compared to what is supported by the provider
- review documentation for command line

If you miss any feature, just create an issue accordingly. Be sure to describe your use case clearly, and to provide links to the correct sources.

### Coding

- add support for a new provider. _Documentation TBD_, starting point possible with [wip_guide](https://geocoder.readthedocs.io/wip_guide.html).
- extend methods for an existing support, i.e support an additionnal API). _Documentation TBD_
- extend support of an existing API, i.e, support more (json) fields from the response, or more parameters. _Documentation TBD_


## ChangeLog

See [CHANGELOG.md](./CHANGELOG.md)


[TGOS]: http://geocoder.readthedocs.org/providers/TGOS.html
[Mapbox]: http://geocoder.readthedocs.org/providers/Mapbox.html
[Google]: http://geocoder.readthedocs.org/providers/Google.html
[G-Policy]: https://developers.google.com/maps/documentation/geocoding/usage-limits
[Bing]: http://geocoder.readthedocs.org/providers/Bing.html
[LocationIQ]: http://geocoder.readthedocs.org/providers/LocationIQ.html
[OpenStreetMap]: http://geocoder.readthedocs.org/providers/OpenStreetMap.html
[OpenStreetMap-Policy]: https://operations.osmfoundation.org/policies/nominatim/
[HERE]: http://geocoder.readthedocs.org/providers/HERE.html
[TomTom]: http://geocoder.readthedocs.org/providers/TomTom.html
[MapQuest]: http://geocoder.readthedocs.org/providers/MapQuest.html
[OpenCage]: http://geocoder.readthedocs.org/providers/OpenCage.html
[Yahoo]: http://geocoder.readthedocs.org/providers/Yahoo.html
[ArcGIS]: http://geocoder.readthedocs.org/providers/ArcGIS.html
[Yandex]: http://geocoder.readthedocs.org/providers/Yandex.html
[Geocoder.ca]: http://geocoder.readthedocs.org/providers/Geocoder-ca.html
[Baidu]: http://geocoder.readthedocs.org/providers/Baidu.html
[GeoOttawa]: http://geocoder.readthedocs.org/providers/GeoOttawa.html
[FreeGeoIP]: http://geocoder.readthedocs.org/providers/FreeGeoIP.html
[FreeGeoip-Policy]: https://github.com/apilayer/freegeoip#readme
[MaxMind]: http://geocoder.readthedocs.org/providers/MaxMind.html
[Mapzen]: https://mapzen.com/blog/shutdown
[What3Words]: http://geocoder.readthedocs.org/providers/What3Words.html
[CanadaPost]: http://geocoder.readthedocs.org/providers/CanadaPost.html
[GeoNames]: http://geocoder.readthedocs.org/providers/GeoNames.html
[IPInfo]: http://geocoder.readthedocs.org/providers/IPInfo.html
[Tamu]: http://geoservices.tamu.edu/Services/Geocode/WebService/
[GeocodeFarm]: https://geocode.farm/
[GeocodeFarm-Policy]: https://geocode.farm/geocoding/free-api-documentation/
[Gaode]: http://geocoder.readthedocs.org/providers/.html
[IP-Plans]: http://ipinfo.io/pricing
[Komoot]: http://photon.komoot.de
[USCensus]: https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html
[Gisgraphy]: https://premium.gisgraphy.com/
