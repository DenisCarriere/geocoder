# Geocoder

[![badge][badge]][badge_url] [![travis][travis]][travis_url]

Geocoder is a geocoding library, written in python, simple and consistent.

![providers][providers]

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

## Features

- [GeoJSON Support]
- [OpenStreetMap Support]
- [Command Line Interface]
- [Confidence Score]
- [Well Known Text Support]

## Installation

To install Geocoder, simply:

```bash
$ pip install geocoder
```

## Providers

- [ArcGIS]
- [Bing]
- [CanadaPost]
- [FreeGeoIP]
- [Geocoder-ca]
- [Geonames]
- [Google]
- [HERE]
- [MapQuest]
- [MaxMind]
- [OpenCage]
- [OpenStreetMap]
- [GeoOttawa]
- [TomTom]
- [Yahoo]

## Documentation

Documentation is available at http://Geocoder.ReadTheDocs.org

## Twitter

Speak up on Twitter [DenisCarriere] and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [python].

## Topic not available?

If you cannot find a topic you are looking for, please feel free to ask me [DenisCarriere] or post them on the [Github Issues Page].

## Feedback

Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page].

## Thanks to

A big thanks to all the people that help contribute:

* [Thanh Ha]: Cleaned up code
* [Mahdi Yusuf]: Promotesyd by [Pycoders Weekly]
* [Alex Pilon]: Cleaned up code
* [Philip Hubertus]: Provided HERE improvements & documentation
* [Antonio Lima]: Improved code quality and introduced Rate Limits
* [Alexander Lukanin]: Improved Python 3 compatibilty
* [flebel]
* [patrickyan]
* [esy]

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

[ArcGIS]: http://geocoder.readthedocs.org/providers/ArcGIS
[Bing]: http://geocoder.readthedocs.org/providers/Bing
[CanadaPost]: http://geocoder.readthedocs.org/providers/CanadaPost
[FreeGeoIP]: http://geocoder.readthedocs.org/providers/FreeGeoIP
[Geocoder-ca]: http://geocoder.readthedocs.org/providers/Geocoder-ca
[Geonames]: http://geocoder.readthedocs.org/providers/Geonames
[Google]: http://geocoder.readthedocs.org/providers/Google
[HERE]: http://geocoder.readthedocs.org/providers/HERE
[MapQuest]: http://geocoder.readthedocs.org/providers/MapQuest
[MaxMind]: http://geocoder.readthedocs.org/providers/MaxMind
[OpenCage]: http://geocoder.readthedocs.org/providers/OpenCage
[OpenStreetMap]: http://geocoder.readthedocs.org/providers/OpenStreetMap
[GeoOttawa]: http://geocoder.readthedocs.org/providers/GeoOttawa
[TomTom]: http://geocoder.readthedocs.org/providers/TomTom
[Yahoo]: http://geocoder.readthedocs.org/providers/Yahoo

[GeoJSON Support]: http://geocoder.readthedocs.org/features/GeoJSON
[OpenStreetMap Support]: http://geocoder.readthedocs.org/features/OpenStreetMap
[Command Line Interface]: http://geocoder.readthedocs.org/features/Command-Line-Interface
[Confidence Score]: http://geocoder.readthedocs.org/features/Confidence-Score
[Well Known Text Support]: http://geocoder.readthedocs.org/features/Well-Known-Text-Support

[providers]: http://i.imgur.com/vUJKCGl.png
[badge_url]: http://badge.fury.io/py/geocoder
[travis_url]: https://travis-ci.org/DenisCarriere/geocoder
[badge]: https://badge.fury.io/py/geocoder.png
[travis]: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
[DenisCarriere]: https://twitter.com/DenisCarriere
[python]: https://twitter.com/search?q=%23python
[Github Issues Page]: https://github.com/DenisCarriere/geocoder/issues
