Geocoder
========

.. image:: https://pypip.in/v/geocoder/badge.png
    :target: http://badge.fury.io/py/geocoder

.. image:: https://pypip.in/d/geocoder/badge.png
    :target: https://pypi.python.org/pypi/geocoder/


A simplistic Python Geocoder.

Geocoder is an Apache2 Licensed Geocoding library, written in Python.


.. code-block:: pycon

    >>> import geocoder
    >>> g = geocoder.google('Moscone Center')
    >>> g.latlng
    (37.784173, -122.401557)
    >>> g.city
    'San Francisco'
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
    >>> g = geocoder.google('1600 Amphitheatre Pkwy, Mountain View, CA')
    >>> g.latlng
    (37.784173, -122.401557)
    >>> g.postal
    '94043'
    >>> g.city
    'Mountain View'
    >>> g.country
    'United States'
    ...


Getting JSON
````````````

.. code-block:: pycon
    
    >>> g = geocoder.google('1600 Amphitheatre Parkway, Mountain View, CA')
    >>> g.json
    {'address': '1600 Amphitheatre Parkway, Mountain View, CA 94043, USA',
    'bbox': {'northeast': {'lat': 37.4233474802915, 'lng': -122.0826054197085},
    'southwest': {'lat': 37.4206495197085, 'lng': -122.0853033802915}},
    'city': 'Mountain View',
    'country': 'United States',
    'lat': 37.4219985,
    'lng': -122.0839544,
    'location': '1600 Amphitheatre Parkway, Mountain View, CA 94043, USA',
    'ok': True,
    'postal': '94043',
    'provider': 'Google',
    'quality': 'ROOFTOP',
    'status': 'OK'}
    ...

Distance Calculator
```````````````````
Using the Great Circle distance by using the Harversine formula.

.. code-block:: pycon

    >>> d = geocoder.distance('Ottawa', 'Toronto')
    >>> d.km
    351.902264779
    >>> d.miles
    218.672067333
    ...

Different ways to use the Distance calculator

.. code-block:: pycon

    >>> from geocoder import distance
    >>> ottawa = (45.4215296, -75.69719309999999)
    >>> toronto = {'lat':43.653226, 'lng':-79.3831843}
    >>> km = distance(ottawa, toronto).km
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


Geocoding IP Address
````````````````````

.. code-block:: pycon

    >>> ip = geocoder.ip('74.125.226.99')
    >>> ip.latlng
    (37.4192, -122.0574)
    >>> ip.address
    'Mountain View, California United States'

    ## Try using Reverse Geocoding with your results
    >>> g = geocoder.reverse(ip.latlng)
    >>> g.address
    'Sevryns Road, Mountain View, CA 94043, USA'
    ...


Geocoder Attributes
-------------------
- address
- location
- city
- country
- postal
- quality
- status
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
    
    ## Priority Geocoders
    >>> geocoder.google(<location>)
    >>> geocoder.osm(<location>)

    ## Secondary Geocoders
    >>> geocoder.mapquest(<location>)
    >>> geocoder.arcgis(<location>)
    >>> geocoder.bing(<location>, key='XXXXX')
    >>> geocoder.nokia(<location>, app_id='XXXXX', app_code='XXXXX')
    >>> geocoder.tomtom(<location>, key='XXXXX')
    ...


Command Line
````````````

.. code-block:: bash

    $ geocoder Ottawa
    45.4215296, -75.69719309999999


More interaction with command line will soon follow.
    

Contribute
----------

Please feel free to give any feedback on this module, it is still in it's early stages of production. If you have any questions about GIS & Python you can contact @DenisCarriere for any questions.

