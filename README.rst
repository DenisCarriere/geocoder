========
Geocoder
========

Simple and consistent geocoding library written in Python.

.. image:: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
   :target: https://travis-ci.org/DenisCarriere/geocoder

.. image:: https://coveralls.io/repos/DenisCarriere/geocoder/badge.png
   :target: https://coveralls.io/r/DenisCarriere/geocoder

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

.. image:: http://i.imgur.com/vUJKCGl.png
   :width: 570
   :height: 340
   :alt: Geocoding Providers


Example
=======

Consistant JSON responses from various providers.

.. code-block:: python

    >>> g = geocoder.google('New York City')
    >>> g.latlng
    [40.7127837, -74.0059413]
    >>> g.state
    'New York'
    >>> g.json
    ...

API Overview
============

Many properties are available once the geocoder object is created.

Forward
-------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.geojson
    >>> g.json
    >>> g.wkt
    >>> g.osm
    ...

Reverse
-------

.. code-block:: python

    >>> g = geocoder.google([45.15, -75.14], method='reverse')
    >>> g.city
    >>> g.state
    >>> g.state_long
    >>> g.country
    >>> g.country_long
    ...

House Addresses
---------------

.. code-block:: python

    >>> g = geocoder.google("453 Booth Street, Ottawa ON")
    >>> g.housenumber
    >>> g.postal
    >>> g.street
    >>> g.street_long
    ...

IP Addresses
------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.ip('199.7.157.0')
    >>> g = geocoder.ip('me')
    >>> g.latlng
    >>> g.city

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode "Ottawa, ON"  >> ottawa.geojson
    $ geocode "Ottawa, ON" \
        --provide google \
        --out geojson \
        --method geocode

Providers
=========

.. csv-table::
   :header: Provider, Optimal, Access
   :widths: 20, 15, 15

    ArcGIS_, World
    Baidu_, China, API key
    Bing_, World, API key
    CanadaPost_, Canada, API key
    FreeGeoIP_, World
    `Geocoder.ca`_, North America, Rate Limit
    GeoNames_, World, Username
    GeoOttawa_, Ottawa
    Google_, World, Rate Limit
    HERE_, World, API key
    MapQuest_, World, API key
    MaxMind_, World
    OpenCage_, World, API key
    OpenStreetMap_, World
    TomTom_, World, API key
    What3Words_, World, API key
    Yahoo_, World
    Yandex_, Russia

Installation
============

PyPi Install
------------

To install Geocoder, simply:

.. code-block:: python

    $ pip install geocoder

GitHub Install
--------------

Installing the latest version from Github:

.. code-block:: python

    $ git clone https://github.com/DenisCarriere/geocoder
    $ cd geocoder
    $ python setup.py install


Documentation
=============

https://geocoder.readthedocs.org/

Twitter
=======

Speak up on Twitter DenisCarriere_ and tell me how you use this Python Geocoder. New updates will be pushed to Twitter Hashtags python_.

Topic not available?
====================

If you cannot find a topic you are looking for, please feel free to ask me DenisCarriere_ or post them on the `Github Issues Page`_.

Feedback
========

Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the `Github Issues Page`_.


.. _DenisCarriere: https://twitter.com/DenisCarriere
.. _python: https://twitter.com/search?q=%23python
.. _`Github Issues Page`: https://github.com/DenisCarriere/geocoder/issues

.. _`Distance Tool`: http://geocoder.readthedocs.org/en/latest/features/Distance/
.. _Google: http://geocoder.readthedocs.org/en/latest/providers/Google/
.. _Bing: http://geocoder.readthedocs.org/en/latest/providers/Bing/
.. _OpenStreetMap: http://geocoder.readthedocs.org/en/latest/providers/OpenStreetMap/
.. _HERE: http://geocoder.readthedocs.org/en/latest/providers/HERE/
.. _TomTom: http://geocoder.readthedocs.org/en/latest/providers/TomTom/
.. _MapQuest: http://geocoder.readthedocs.org/en/latest/providers/MapQuest/
.. _OpenCage: http://geocoder.readthedocs.org/en/latest/providers/OpenCage/
.. _Yahoo: http://geocoder.readthedocs.org/en/latest/providers/Yahoo/
.. _ArcGIS: http://geocoder.readthedocs.org/en/latest/providers/ArcGIS/
.. _Yandex: http://geocoder.readthedocs.org/en/latest/providers/Yandex/
.. _`Geocoder.ca`: http://geocoder.readthedocs.org/en/latest/providers/Geocoder-ca/
.. _Baidu: http://geocoder.readthedocs.org/en/latest/providers/Baidu/
.. _GeoOttawa: http://geocoder.readthedocs.org/en/latest/providers/GeoOttawa/
.. _FreeGeoIP: http://geocoder.readthedocs.org/en/latest/providers/FreeGeoIP/
.. _MaxMind: http://geocoder.readthedocs.org/en/latest/providers/MaxMind/
.. _What3Words: http://geocoder.readthedocs.org/en/latest/providers/What3Words/
.. _CanadaPost: http://geocoder.readthedocs.org/en/latest/providers/CanadaPost/
.. _GeoNames: http://geocoder.readthedocs.org/en/latest/providers/GeoNames/