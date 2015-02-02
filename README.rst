Geocoder |badge| |travis|
-------------------------

Geocoder is a MIT Licensed Geocoding library, written in Python, simple
and consistant.

.. figure:: http://i.imgur.com/vUJKCGl.png
   :alt: providers

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different JSON
responses between each other.

Consistant JSON responses from various providers.

.. code:: python

    >>> g = geocoder.google('New York City')
    >>> g.latlng
    [40.7127837, -74.0059413]
    >>> g.state
    'New York'
    >>> g.json
    ...

Features
--------

-  `GeoJSON
   Support <https://github.com/DenisCarriere/geocoder/wiki/GeoJSON-Support>`__
-  `OpenStreetMap
   Support <https://github.com/DenisCarriere/geocoder/wiki/OpenStreetMap-Support>`__
-  `Command Line
   Interface <https://github.com/DenisCarriere/geocoder/wiki/Command-Line-Interface>`__
-  `Confidence
   Score <https://github.com/DenisCarriere/geocoder/wiki/Confidence-Score>`__
-  `Well Known Text
   Support <https://github.com/DenisCarriere/geocoder/wiki/Well-Known-Text-Support>`__

Installation
------------

To install Geocoder, simply:

.. code:: bash

    $ pip install geocoder

Providers
---------

-  `ArcGIS <https://github.com/DenisCarriere/geocoder/wiki/ArcGIS>`__
-  `Bing <https://github.com/DenisCarriere/geocoder/wiki/Bing>`__
-  `CanadaPost <https://github.com/DenisCarriere/geocoder/wiki/CanadaPost>`__
-  `FreeGeoIP <https://github.com/DenisCarriere/geocoder/wiki/FreeGeoIP>`__
-  `Geocoder.ca <https://github.com/DenisCarriere/geocoder/wiki/Geocoder-ca>`__
-  `Geonames <https://github.com/DenisCarriere/geocoder/wiki/Geonames>`__
-  `Google <https://github.com/DenisCarriere/geocoder/wiki/Google>`__
-  `HERE <https://github.com/DenisCarriere/geocoder/wiki/HERE>`__
-  `MapQuest <https://github.com/DenisCarriere/geocoder/wiki/MapQuest>`__
-  `MaxMind <https://github.com/DenisCarriere/geocoder/wiki/MaxMind>`__
-  `OpenCage <https://github.com/DenisCarriere/geocoder/wiki/OpenCage>`__
-  `OpenStreetMap <https://github.com/DenisCarriere/geocoder/wiki/OpenStreetMap>`__
-  `GeoOttawa <https://github.com/DenisCarriere/geocoder/wiki/GeoOttawa>`__
-  `TomTom <https://github.com/DenisCarriere/geocoder/wiki/TomTom>`__
-  `Yahoo <https://github.com/DenisCarriere/geocoder/wiki/Yahoo>`__

Documentation
-------------

Documentation is available at http://deniscarriere.github.io/geocoder

Topic not available?
--------------------

If you cannot find a topic you are looking for, please feel free to ask
me @\ `DenisCarriere <https://twitter.com/DenisCarriere>`__ or post them
on the `Github Issues
Page <https://github.com/DenisCarriere/geocoder/issues>`__.

Support
-------

This project is free & open source, it would help greatly for you guys
reading this to contribute, here are some of the ways that you can help
make this Python Geocoder better.

Feedback
--------

Please feel free to give any feedback on this module. If you find any
bugs or any enhancements to recommend please send some of your
comments/suggestions to the `Github Issues
Page <https://github.com/DenisCarriere/geocoder/issues>`__.

Twitter
-------

Speak up on Twitter [@DenisCarriere] and tell me how you use this Python
Geocoder. New updates will be pushed to Twitter Hashtags
`#geocoder <https://twitter.com/search?q=%23geocoder>`__.

Thanks to
---------

A big thanks to all the people that help contribute:

-  @\ `alexanderlukanin13 <https://github.com/alexanderlukanin13>`__
-  @\ `themiurgo <https://github.com/themiurgo>`__
-  @\ `flebel <https://github.com/flebel>`__
-  @\ `patrickyan <https://github.com/patrickyan>`__
-  @\ `esy <https://github.com/lambda-conspiracy>`__

.. |badge| image:: https://badge.fury.io/py/geocoder.png
   :target: http://badge.fury.io/py/geocoder
.. |travis| image:: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
   :target: https://travis-ci.org/DenisCarriere/geocoder
