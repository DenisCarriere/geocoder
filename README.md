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
- [MapQuest]
- [MaxMind]
- [Nokia]
- [OpenCage]
- [OpenStreetMap]
- [GeoOttawa]
- [TomTom]
- [Yahoo]

## Documentation

Documentation is available at http://deniscarriere.github.io/geocoder

## Topic not available?

If you cannot find a topic you are looking for, please feel free to ask me [@DenisCarriere] or post them on the [Github Issues Page].

## Support

This project is free & open source, it would help greatly for you guys reading this to contribute, here are some of the ways that you can help make this Python Geocoder better.

## Feedback

Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the [Github Issues Page].

## Twitter

Speak up on Twitter [@DenisCarriere] and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags [#geocoder].

## Thanks to

A big thanks to all the people that help contribute: 

* [@flebel](https://github.com/flebel)
* [@patrickyan](https://github.com/patrickyan)
* [@themiurgo](https://github.com/themiurgo)
* [@esy](https://github.com/lambda-conspiracy)


[ArcGIS]: https://github.com/DenisCarriere/geocoder/wiki/ArcGIS
[Bing]: https://github.com/DenisCarriere/geocoder/wiki/Bing
[CanadaPost]: https://github.com/DenisCarriere/geocoder/wiki/CanadaPost
[FreeGeoIP]: https://github.com/DenisCarriere/geocoder/wiki/FreeGeoIP
[Geocoder.ca]: https://github.com/DenisCarriere/geocoder/wiki/Geocoder-ca
[Geonames]: https://github.com/DenisCarriere/geocoder/wiki/Geonames 
[Google]: https://github.com/DenisCarriere/geocoder/wiki/Google
[MapQuest]: https://github.com/DenisCarriere/geocoder/wiki/MapQuest
[MaxMind]: https://github.com/DenisCarriere/geocoder/wiki/MaxMind
[Nokia]: https://github.com/DenisCarriere/geocoder/wiki/Nokia
[OpenCage]: https://github.com/DenisCarriere/geocoder/wiki/OpenCage
[OpenStreetMap]: https://github.com/DenisCarriere/geocoder/wiki/OpenStreetMap
[GeoOttawa]: https://github.com/DenisCarriere/geocoder/wiki/GeoOttawa
[TomTom]: https://github.com/DenisCarriere/geocoder/wiki/TomTom
[Yahoo]: https://github.com/DenisCarriere/geocoder/wiki/Yahoo

[GeoJSON Support]: https://github.com/DenisCarriere/geocoder/wiki/GeoJSON-Support
[OpenStreetMap Support]: https://github.com/DenisCarriere/geocoder/wiki/OpenStreetMap-Support
[Command Line Interface]: https://github.com/DenisCarriere/geocoder/wiki/Command-Line-Interface
[Confidence Score]: https://github.com/DenisCarriere/geocoder/wiki/Confidence-Score
[Well Known Text Support]: https://github.com/DenisCarriere/geocoder/wiki/Well-Known-Text-Support

[providers]: https://pbs.twimg.com/media/Bqi8kThCUAAboo0.png
[badge_url]: http://badge.fury.io/py/geocoder
[travis_url]: https://travis-ci.org/DenisCarriere/geocoder
[badge]: https://badge.fury.io/py/geocoder.png
[travis]: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
[@DenisCarriere]: https://twitter.com/DenisCarriere
[#geocoder]: https://twitter.com/search?q=%23geocoder
[Github Issues Page]: https://github.com/DenisCarriere/geocoder/issues