# Geocoder [![badge][badge]][badge_url] [![travis][travis]][travis_url]

Geocoder is a MIT Licensed Geocoding library, written in Python, 
simple and consistant.

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
- [Geocoder.ca]
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

Documentation is available at http://deniscarriere.github.io/geocoder

## Twitter

Speak up on Twitter [DenisCarriere] and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [#python].

## Topic not available?

If you cannot find a topic you are looking for, please feel free to ask me [DenisCarriere] or post them on the [Github Issues Page].

## Feedback

Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page].

## Thanks to

A big thanks to all the people that help contribute: 

* [Philip Hubertus]: Provided HERE improvements & documentation
* [Antonio Lima]: Improved code quality and introduced Rate Limits
* [Alexander Lukanin]: Improved Python 3 compatibilty
* [flebel]
* [patrickyan]
* [esy]



[Philip Hubertus]: https://twitter.com/philiphubs
[Antonio Lima]: https://twitter.com/themiurgo
[Alexander Lukanin]: https://github.com/alexanderlukanin13
[flebel]: https://github.com/flebel
[patrickyan]: https://github.com/patrickyan
[esy]: https://github.com/lambda-conspiracy

[ArcGIS]: providers/ArcGIS
[Bing]: providers/Bing
[CanadaPost]: providers/CanadaPost
[FreeGeoIP]: providers/FreeGeoIP
[Geocoder.ca]: providers/Geocoder-ca
[Geonames]: providers/Geonames 
[Google]: providers/Google
[HERE]: providers/HERE
[MapQuest]: providers/MapQuest
[MaxMind]: providers/MaxMind
[OpenCage]: providers/OpenCage
[OpenStreetMap]: providers/OpenStreetMap
[GeoOttawa]: providers/GeoOttawa
[TomTom]: providers/TomTom
[Yahoo]: providers/Yahoo

[GeoJSON Support]: features/GeoJSON
[OpenStreetMap Support]: features/OpenStreetMap
[Command Line Interface]: features/Command-Line-Interface
[Confidence Score]: features/Confidence-Score
[Well Known Text Support]: features/Well-Known-Text-Support

[providers]: http://i.imgur.com/vUJKCGl.png
[badge_url]: http://badge.fury.io/py/geocoder
[travis_url]: https://travis-ci.org/DenisCarriere/geocoder
[badge]: https://badge.fury.io/py/geocoder.png
[travis]: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
[DenisCarriere]: https://twitter.com/DenisCarriere
[#python]: https://twitter.com/search?q=%23python
[Github Issues Page]: https://github.com/DenisCarriere/geocoder/issues
