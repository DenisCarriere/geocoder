Python Geocoder
===============
[![](https://img.shields.io/pypi/v/geocoder.svg)](https://pypi.python.org/pypi/geocoder)
[![Snap Status](https://build.snapcraft.io/badge/DenisCarriere/geocoder.svg)](https://build.snapcraft.io/user/DenisCarriere/geocoder)
[![](https://travis-ci.org/DenisCarriere/geocoder.svg?branch=master)](https://travis-ci.org/DenisCarriere/geocoder)

Simple and consistent geocoding library written in Python.

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

Now lets use Geocoder to do the same task.

```python
>>> import geocoder
>>> g = geocoder.google('Mountain View, CA')
>>> g.latlng
(37.3860517, -122.0838511)
```

Documentation
-------------
https://geocoder.readthedocs.org/


API Overview
------------
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

Command Line Interface
----------------------
```bash
$ geocode "Ottawa, ON"  >> ottawa.geojson
$ geocode "Ottawa, ON" \
    --provide google \
    --out geojson \
    --method geocode
```

Providers
---------
| Provider                       | Optimal       | Usage Policy                    |
|:-------------------------------|:--------------|:--------------------------------|
| [ArcGIS][ArcGIS]               | World         |                                 |
| [Baidu][Baidu]                 | China         | API key                         |
| [Bing][Bing]                   | World         | API key                         |
| [CanadaPost][CanadaPost]       | Canada        | API key                         |
| [FreeGeoIP][FreeGeoIP]         | World         |                                 |
| [Geocoder.ca][Geocoder.ca]     | CA & US       | Rate Limit                      |
| [GeocodeFarm][GeocodeFarm]     | World         | [Policy][GeocodeFarm-Policy]    |
| [GeoNames][GeoNames]           | World         | Username                        |
| [GeoOttawa][GeoOttawa]         | Ottawa        |                                 |
| [Google][Google]               | World         | Rate Limit, [Policy][Google-Policy] |
| [HERE][HERE]                   | World         | API key                         |
| [IPInfo][IPInfo]               | World         |                                 |
| [Mapbox][Mapbox]               | World         | API key                         |
| [MapQuest][MapQuest]           | World         | API key                         |
| [Mapzen][Mapzen]               | World         | API key                         |
| [MaxMind][MaxMind]             | World         |                                 |
| [OpenCage][OpenCage]           | World         | API key                         |
| [OpenStreetMap][OpenStreetMap] | World         | [Policy][OpenStreetMap-Policy]  |
| [Tamu][Tamu]                   | US            | API key                         |
| [TomTom][TomTom]               | World         | API key                         |
| [What3Words][What3Words]       | World         | API key                         |
| [Yahoo][Yahoo]                 | World         |                                 |
| [Yandex][Yandex]               | Russia        |                                 |
| [TGOS][TGOS]                   | Taiwan        |                                 |

Installation
------------

### PyPi Install

To install Geocoder, simply:

```bash
$ pip install geocoder
```

### GitHub Install

Installing the latest version from Github:

```bash
$ git clone https://github.com/DenisCarriere/geocoder
$ cd geocoder
$ python setup.py install
```

Twitter
-------
Speak up on Twitter [@DenisCarriere](https://twitter.com/DenisCarriere) and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [#python](https://twitter.com/search?q=%23python).

Feedback
--------
Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page](https://github.com/DenisCarriere/geocoder/issues).

[TGOS]: http://geocoder.readthedocs.org/providers/TGOS.html
[Mapbox]: http://geocoder.readthedocs.org/providers/Mapbox.html
[Google]: http://geocoder.readthedocs.org/providers/Google.html
[Google-Policy]: https://developers.google.com/maps/documentation/geocoding/usage-limits
[Bing]: http://geocoder.readthedocs.org/providers/Bing.html
[OpenStreetMap]: http://geocoder.readthedocs.org/providers/OpenStreetMap.html
[OpenStreetMap-Policy]: https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy
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
[MaxMind]: http://geocoder.readthedocs.org/providers/MaxMind.html
[Mapzen]: http://geocoder.readthedocs.org/providers/Mapzen.html
[What3Words]: http://geocoder.readthedocs.org/providers/What3Words.html
[CanadaPost]: http://geocoder.readthedocs.org/providers/CanadaPost.html
[GeoNames]: http://geocoder.readthedocs.org/providers/GeoNames.html
[IPInfo]: http://geocoder.readthedocs.org/providers/IPInfo.html
[Tamu]: http://geoservices.tamu.edu/Services/Geocode/WebService/
[GeocodeFarm]: https://geocode.farm/
[GeocodeFarm-Policy]: https://geocode.farm/geocoding/free-api-documentation/
