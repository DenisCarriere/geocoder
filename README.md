# Geocoder

[![PyPi Badge][badge]][badge_url] [![Travis CI][travis]][travis_url] [![Coverage Status][coverage]][coverage_url]

Geocoder is a geocoding library, written in python, simple and consistent.

![][providers]

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

Consistant JSON responses from various providers.

```python
>>> g = geocoder.google('New York City')
>>> g.latlng
[40.7127837, -74.0059413]
>>> g.state
'New York'
>>> g.json
...
```

## Installation

To install Geocoder, simply:

```bash
$ pip install geocoder
```

## Providers

| Global        | Country       | Specialized |
|:--------------|:------------- |:------------|
| Google        | Yandex        | GeoOttawa   |
| Bing          | Geocoder.ca   | FreeGeoIP   |
| OpenStreetMap | Baidu         | MaxMind     |
| HERE        	|               | what3words  |
| TomTom        |               | CanadaPost  |
| MapQuest      |               | Geonames    |
| OpenCage      |               |             |
| Yahoo 		|               |             |
| ArcGIS        |               |             |


## Features

- Formats (JSON, GeoJSON, OSM, WKT)
- Command Line Interface
- Confidence Score

## Documentation

https://geocoder.readthedocs.org/

## Twitter

Speak up on Twitter [DenisCarriere] and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [python].

## Topic not available?

If you cannot find a topic you are looking for, please feel free to ask me [DenisCarriere] or post them on the [Github Issues Page].

## Feedback

Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page].

## Thanks to

A big thanks to all the people that help contribute:

- [Max Arnold] - Submitted Github Issue
- [Thanh Ha] - Cleaned up code & Unit Testing
- [Mahdi Yusuf] - Promoted by [Pycoders Weekly]
- [Alex Pilon] - Cleaned up code
- [Philip Hubertus] - Provided HERE improvements & documentation
- [Antonio Lima] - Improved code quality and introduced Rate Limits
- [Alexander Lukanin] - Improved Python 3 compatibilty
- [flebel] - Submitted Github Issues
- [patrickyan] - Submitted Github Issues
- [esy] - Submitted Github Issues

[Max Arnold]: https://github.com/max-arnold
[Thanh Ha]: https://twitter.com/zxiiro
[Alex Pilon]: http://alexpilon.ca
[Mahdi Yusuf]: https://twitter.com/myusuf3
[Pycoders Weekly]: https://twitter.com/pycoders
[Philip Hubertus]: https://twitter.com/philiphubs
[Antonio Lima]: https://twitter.com/themiurgo
[Alexander Lukanin]: https://github.com/alexanderlukanin13
[flebel]: https://github.com/flebel
[patrickyan]: https://github.com/patrickyan
[esy]: https://github.com/lambda-conspiracy

[providers]: http://i.imgur.com/vUJKCGl.png
[coverage]: https://coveralls.io/repos/DenisCarriere/geocoder/badge.svg
[coverage_url]: https://coveralls.io/r/DenisCarriere/geocoder
[badge]: https://badge.fury.io/py/geocoder.png
[badge_url]: http://badge.fury.io/py/geocoder
[travis]: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
[travis_url]: https://travis-ci.org/DenisCarriere/geocoder
[DenisCarriere]: https://twitter.com/DenisCarriere
[python]: https://twitter.com/search?q=%23python
[Github Issues Page]: https://github.com/DenisCarriere/geocoder/issues
