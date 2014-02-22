Geocoder
========

.. image:: https://badge.fury.io/py/geocoder.png
    :target: http://badge.fury.io/py/geocoder

.. image:: https://pypip.in/d/geocoder/badge.png
    :target: https://pypi.python.org/pypi/geocoder/

A simplistic Python Geocoder.

Geocoder is an Apache2 Licensed Geocoding library, written in Python.


.. code-block:: pycon

    >>> from geocoder import google
    >>> g = google('Parliament Hill, Ottawa')
    >>> g.latlng
    (45.4235937, -75.700929)
    ...

Installation
------------

To install Geocoder, simply:

.. code-block:: bash

    $ pip install geocoder

Documentation
-------------
    
Basic Usage
```````````

.. code-block:: pycon

    >>> import geocoder
    >>> g = geocoder.osm('1600 Amphitheatre Pkwy, Mountain View, CA')
    >>> g.latlng
    (-122.0850862, 37.4228139)
    >>> g.postal
    '94043'
    ...


Getting JSON
````````````

.. code-block:: pycon

    >>> g.json
    {'address': u'1600 Amphitheatre Parkway, Mountain View, CA 94043, USA',
    'bbox': {'northeast': {'lat': 37.4233474802915, 'lng': -122.0826054197085},
    'southwest': {'lat': 37.4206495197085, 'lng': -122.0853033802915}},
    'lat': 37.4219985,
    'lng': -122.0839544,
    'location': '1600 Amphitheatre Pkwy, Mountain View, CA',
    'ok': True,
    'postal': u'94043',
    'provider': 'Google',
    'quality': u'ROOFTOP',
    'status': u'OK'}
    ...


Reverse Geocoding
`````````````````

.. code-block:: pycon
    
    ## Input methods
    >>> geocoder.reverse(lat, lng)
    >>> geocoder.reverse(latlng)

    ## Results
    >>> latlng = (48.85837, 2.2944813)
    >>> g = geocoder.reverse(latlng)
    <[OK] Geocoder Google [Eiffel Tower, Paris, France]>
    ...

Bounding Box (Extent)
`````````````````````

.. code-block:: pycon
    
    >>> g = geocoder.osm('1600 Amphitheatre Pkwy, Mountain View, CA')
    >>> g.bbox
    {'northeast': {'lat': 37.4233474802915, 'lng': -122.0826054197085},
    'southwest': {'lat': 37.4206495197085, 'lng': -122.0853033802915}}
    >>> g.southwest
    {'lat': 37.4206495197085, 'lng': -122.0853033802915}
    >>> g.south
    37.4206495197085
    ...


Bbox Values
```````````
- bbox
- southwest
- northeast
- south
- west
- north
- east


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
    ...

Geocoder Attributes
-------------------
- address (string, UTF-8)
- location (string)
- postal (string)
- quality (string)
- status (string)
- ok (boolean)
- x, lng, longitude (float)
- y, lat, latitude (float)
- latlng, xy (tuple)
- bbox {southwest, northeast}
- southwest {lat, lng}
- northeast {lat, lng}
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


Command Line
````````````

.. code-block:: bash

    $ geocode Ottawa
    45.4215296, -75.69719309999999


More interaction with command line will soon follow.
    

Contribute
----------

Please feel free to give any feedback on this module, it is still in it's early stages of production. If you have any questions about GIS & Python you can contact @DenisCarriere for any questions.

