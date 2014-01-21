Geocoder
========

.. image:: https://badge.fury.io/py/geocoder.png
    :target: http://badge.fury.io/py/geocoder

.. image:: https://pypip.in/d/geocoder/badge.png
    :target: https://pypi.python.org/pypi/geocoder/

A simplistic Python Geocoder.

Geocoder is an Apache2 Licensed Geocoding library, written in Python.


.. code-block:: pycon

    >>> import geocoder
    >>> g = geocoder.get('Parliament Hill, Ottawa')
    >>> g.latlng
    [45.4235937, -75.700929]
    >>> g.latitude
    45.4235937
    >>> g.address
    'Parliament Hill, Wellington Street, Ottawa, ON, Canada'

Installation
------------

To install Geocoder, simplpy:

.. code-block:: bash

    $ pip install geocoder


Geocoding Providers
-------------------

- Google
- MaxMind (IP address instead of location)
- Mapquest
- OSM
- ESRI
- Bing (Key Required)
- TomTom (Key Required)
- Nokia (App ID & App Code Required)


Documentation
-------------
    
Basic Usage
```````````

.. code-block:: pycon

    >>> import geocoder
    >>> g = geocoder.osm('1600 Amphitheatre Pkwy, Mountain View, CA')
    >>> g.xy
    [-122.0850862, 37.4228139]
    >>> g.postal
    '94043'
    >>> g.address
    'Google Headquaters, 1600, Amphitheatre Parkway, Mountain View...'
    >>> g.bbox
    [(37.4228134155273, -122.085090637207), (37.4228172302246, -122.085083007812)]
    # bbox = [SouthWest, NorthEast]
    >>> g.quality
    'commercial'
    >>> g.x, g.y
    (-122.0850862, 37.4228139)
    >>> g.south, g.west
    (37.4228134155273, -122.085090637207)
    ...

Geocoding IP Address
````````````````````

.. code-block:: pycon

    >>> g = geocoder.ip('74.125.226.99')
    >>> g
    <[OK] Geocoder MaxMind [Mountain View, California United States]>
    >>> g.xy
    [-122.0574, 37.4192]
    ...

Geocoding using a Loop
``````````````````````

.. code-block :: pycon
    
    >>> for provider in ['google', 'osm', 'mapquest']:
    >>>     g = geocoder.get(<location>, provider=provider)


Geocoder Attributes
```````````````````
- address (string, UTF-8)
- location (string)
- postal (string)
- quality (string)
- status (string)
- ok (boolean)
- x, lng, longitude (float)
- y, lat, latitude (float)
- latlng, xy (string)
- bbox (string, y1 x1 y2 x2)
- southwest (string, y1 x1)
- northeast (string, y2 x2)
- south, west, north, east (float)

Geocoding Providers
```````````````````

.. code-block:: pycon
    
    >>> geocoder.get(<location>, provider=<provider>)
    >>> geocoder.google(<location>)
    >>> geocoder.ip(<IP>)
    >>> geocoder.maxmind(<IP>)
    >>> geocoder.mapquest(<location>)
    >>> geocoder.esri(<location>)
    >>> geocoder.osm(<location>)
    >>> geocoder.tomtom(<location>, key='XXXXX')
    >>> geocoder.bing(<location>, key='XXXXX')
    >>> geocoder.nokia(<location>, app_id='XXXXX', app_code='XXXXX')

    ...


Contribute
----------

Please feel free to give any feedback on this module, it is still in it's early stages of production. If you have any questions about GIS & Python you can contact @DenisCarriere for any questions.

.. _`the repository`: https://github.com/DenisCarriere/geocoder.git
