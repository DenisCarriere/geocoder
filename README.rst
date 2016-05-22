Python Geocoder
===============

|image0| |image1| |image2| |image3|

Simple and consistent geocoding library written in Python.

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different JSON
responses between each other.

It can be very difficult sometimes to parse a particular geocoding
provider since each one of them have their own JSON schema.

Here is a typical example of retrieving a Lat & Lng from Google using
Python, things shouldn't be this hard.

.. code:: python

    >>> import requests
    >>> url = 'https://maps.googleapis.com/maps/api/geocode/json'
    >>> params = {'sensor': 'false', 'address': 'Mountain View, CA'}
    >>> r = requests.get(url, params=params)
    >>> results = r.json()['results']
    >>> location = results[0]['geometry']['location']
    >>> location['lat'], location['lng']
    (37.3860517, -122.0838511)

Now lets use Geocoder to do the same task.

.. code:: python

    >>> import geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.latlng
    (37.3860517, -122.0838511)

Documentation
-------------

https://geocoder.readthedocs.org/

API Overview
------------

Many properties are available once the geocoder object is created.

Forward
~~~~~~~

.. code:: python

    >>> import geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.geojson
    >>> g.json
    >>> g.wkt
    >>> g.osm

Reverse
~~~~~~~

.. code:: python

    >>> g = geocoder.google([45.15, -75.14], method='reverse')
    >>> g.city
    >>> g.state
    >>> g.state_long
    >>> g.country
    >>> g.country_long

House Addresses
~~~~~~~~~~~~~~~

.. code:: python

    >>> g = geocoder.google("453 Booth Street, Ottawa ON")
    >>> g.housenumber
    >>> g.postal
    >>> g.street
    >>> g.street_long

IP Addresses
~~~~~~~~~~~~

.. code:: python

    >>> g = geocoder.ip('199.7.157.0')
    >>> g = geocoder.ip('me')
    >>> g.latlng
    >>> g.city

Bounding Box
~~~~~~~~~~~~

Accessing the JSON & GeoJSON attributes will be different

.. code:: python

    >>> g = geocoder.google("Ottawa")
    >>> g.bbox
    {"northeast": [45.53453, -75.2465979], "southwest": [44.962733, -76.3539158]}

    >>> g.geojson['bbox']
    [-76.3539158, 44.962733, -75.2465979, 45.53453]

    >>> g.southwest
    [44.962733, -76.3539158]

Command Line Interface
----------------------

.. code:: bash

    $ geocode "Ottawa, ON"  >> ottawa.geojson
    $ geocode "Ottawa, ON" \
        --provide google \
        --out geojson \
        --method geocode

Providers
---------

+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| Provider                                                                           | Optimal   | Usage Policy                                                                                       |
+====================================================================================+===========+====================================================================================================+
| `ArcGIS <http://geocoder.readthedocs.org/providers/ArcGIS.html>`__                 | World     |                                                                                                    |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Baidu <http://geocoder.readthedocs.org/providers/Baidu.html>`__                   | China     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Bing <http://geocoder.readthedocs.org/providers/Bing.html>`__                     | World     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `CanadaPost <http://geocoder.readthedocs.org/providers/CanadaPost.html>`__         | Canada    | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `FreeGeoIP <http://geocoder.readthedocs.org/providers/FreeGeoIP.html>`__           | World     |                                                                                                    |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Geocoder.ca <http://geocoder.readthedocs.org/providers/Geocoder-ca.html>`__       | CA & US   | Rate Limit                                                                                         |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `GeocodeFarm <https://geocode.farm/>`__                                            | World     | `Policy <https://geocode.farm/geocoding/free-api-documentation/>`__                                |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `GeoNames <http://geocoder.readthedocs.org/providers/GeoNames.html>`__             | World     | Username                                                                                           |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `GeoOttawa <http://geocoder.readthedocs.org/providers/GeoOttawa.html>`__           | Ottawa    |                                                                                                    |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Google <http://geocoder.readthedocs.org/providers/Google.html>`__                 | World     | Rate Limit, `Policy <https://developers.google.com/maps/documentation/geocoding/usage-limits>`__   |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `HERE <http://geocoder.readthedocs.org/providers/HERE.html>`__                     | World     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `IPInfo <http://geocoder.readthedocs.org/providers/IPInfo.html>`__                 | World     |                                                                                                    |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Mapbox <http://geocoder.readthedocs.org/providers/Mapbox.html>`__                 | World     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `MapQuest <http://geocoder.readthedocs.org/providers/MapQuest.html>`__             | World     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Mapzen <http://geocoder.readthedocs.org/providers/Mapzen.html>`__                 | World     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `MaxMind <http://geocoder.readthedocs.org/providers/MaxMind.html>`__               | World     |                                                                                                    |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `OpenCage <http://geocoder.readthedocs.org/providers/OpenCage.html>`__             | World     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `OpenStreetMap <http://geocoder.readthedocs.org/providers/OpenStreetMap.html>`__   | World     | `Policy <https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy>`__                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Tamu <http://geoservices.tamu.edu/Services/Geocode/WebService/>`__                | US        | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `TomTom <http://geocoder.readthedocs.org/providers/TomTom.html>`__                 | World     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `What3Words <http://geocoder.readthedocs.org/providers/What3Words.html>`__         | World     | API key                                                                                            |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Yahoo <http://geocoder.readthedocs.org/providers/Yahoo.html>`__                   | World     |                                                                                                    |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `Yandex <http://geocoder.readthedocs.org/providers/Yandex.html>`__                 | Russia    |                                                                                                    |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+
| `TGOS <http://geocoder.readthedocs.org/providers/TGOS.html>`__                     | Taiwan    |                                                                                                    |
+------------------------------------------------------------------------------------+-----------+----------------------------------------------------------------------------------------------------+

Installation
------------

PyPi Install
~~~~~~~~~~~~

To install Geocoder, simply:

.. code:: bash

    $ pip install geocoder

GitHub Install
~~~~~~~~~~~~~~

Installing the latest version from Github:

.. code:: bash

    $ git clone https://github.com/DenisCarriere/geocoder
    $ cd geocoder
    $ python setup.py install

Twitter
-------

Speak up on Twitter [@DenisCarriere](https://twitter.com/DenisCarriere)
and tell me how you use this Python Geocoder. New updates will be pushed
to Twitter Hashtags
`#python <https://twitter.com/search?q=%23python>`__.

Feedback
--------

Please feel free to give any feedback on this module. If you find any
bugs or any enhancements to recommend please send some of your
comments/suggestions to the `Github Issues
Page <https://github.com/DenisCarriere/geocoder/issues>`__.

.. |image0| image:: https://img.shields.io/pypi/v/geocoder.svg
   :target: https://pypi.python.org/pypi/geocoder
.. |image1| image:: https://img.shields.io/pypi/dm/geocoder.svg
   :target: https://pypi.python.org/pypi/geocoder
.. |image2| image:: https://travis-ci.org/DenisCarriere/geocoder.svg?branch=master
   :target: https://travis-ci.org/DenisCarriere/geocoder
.. |image3| image:: https://coveralls.io/repos/DenisCarriere/geocoder/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/DenisCarriere/geocoder?branch=master
