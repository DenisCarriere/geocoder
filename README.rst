Python Geocoder
===============

.. image:: https://badge.fury.io/py/geocoder.png
    :target: http://badge.fury.io/py/geocoder

.. image:: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
    :target: https://travis-ci.org/DenisCarriere/geocoder


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

You can install, upgrade, uninstall Geocoder with these commands:

.. code-block:: bash

    $ pip install geocoder
    $ pip install --upgrade geocoder
    $ pip uninstall geocoder 


Documentation
-------------

Search with Google
``````````````````

Using the Geocoder API from Google, this is a simplistic approach
to return you all the same results that Google would provide.

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

If you are using a **Google App for business**.
Here is how you can enter your key client-id & secret keyd.

.. code-block:: pycon

    >>> client = 'gme-XXXXXX'
    >>> secret = 'XXXXXXXXXX'
    >>> g = geocoder.google(<address>, client=client, secret=secret)
    ...

If you have a FREE account, you might only have an API key.
This will still work using your Application's quota limits.

.. code-block:: pycon

    >>> api_key = 'XXXXXXX'
    >>> g = geocoder.google(<address>, api_key=api_key)
    ...


Getting JSON
````````````

The web uses JSON and GeoJSON, here is how to return your Geocoded address into this format.

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

GeoJSON is a widely used, open format for encoding geographic data, and is supported by a number of popular applications. 

.. code-block:: pycon

    >>> import simplejson as json
    >>> g = geocoder.google('Ottawa, ON')
    >>> json.dumps(g.geojson, indent=4)
    {
    "geometry": {
        "type": "Point",
        "coordinates": [
            -75.69719309999999,
            45.4215296
        ]
    },
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    },
    "type": "Feature",
    "properties": {
        "status": "OK",
        "city": "Ottawa",
        "ok": true,
        "country": "Canada",
    ...


Using Proxies & Timeout
```````````````````````
There many obvious reasons why you would need to use proxies,
here is the basic syntax on how to successfully use them.

Timeouts are used to stop the connection if it reaches a certain time.

.. code-block:: pycon

    >>> proxies = '111.161.126.84:80'
    >>> g = geocoder.google('Ottawa', proxies=proxies, timeout=5.0)
    <[OK] Geocoder Google [Ottawa, ON, Canada]>
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

Different ways to use the Distance calculator, you can input the locations by using a tuple (lat, lng) or a dictionary with lat/lng keys.

.. code-block:: pycon

    >>> import geocoder
    >>> ottawa = (45.4215296, -75.69719309999999)
    >>> toronto = {'lat':43.653226, 'lng':-79.3831843}
    >>> d = geocoder.distance(ottawa, toronto)
    >>> d.meters
    351902
    ...

Reverse Geocoding
`````````````````

Using Google's reverse geocoding API, you are able to input a set of coordinates and geocode its location.

.. code-block:: pycon

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

Retrieves geocoding data from MaxMind's GeoIP2 services

.. code-block:: pycon

    >>> g = geocoder.ip('74.125.226.99')
    >>> g.address
    'Mountain View, California United States'
    >>> g.latlng
    (37.4192, -122.0574)

Geocoding your current IP address, simply use **me** as the input.

.. code-block:: pycon

    >>> g = geocoder.ip('me')
    >>> g.address
    'Ottawa, Ontario Canada'
    >>> g.latlng
    (45.4805, -75.5237)
    ...

Population Data from City
`````````````````````````

Retrieves population data from Geonames's Web Service API.

.. code-block:: pycon

    >>> pop = geocoder.population('Springfield, Virginia')
    >>> pop
    30484
    ...

Geocoder Attributes
-------------------
- address
- location
- city
- state
- country
- postal
- quality
- status
- population (integer)
- ok (boolean)
- x, lng, longitude (float)
- y, lat, latitude (float)
- latlng, xy (tuple)
- bbox {southwest, northeast}
- southwest {lat, lng}
- northeast {lat, lng}
- south, west, north, east (float)


Distance Attributes
-------------------
- km (float)
- miles (float)
- meters (integer)
- feet (integer)


Geocoding Providers
```````````````````

.. code-block:: pycon
    
    ## Priority Geocoders
    >>> geocoder.google(<location>)
    >>> geocoder.reverse(<latlng>)
    >>> geocoder.ip(<ip>)

    ## Secondary Geocoders
    >>> geocoder.osm(<location>)
    >>> geocoder.mapquest(<location>)
    >>> geocoder.arcgis(<location>)
    >>> geocoder.geonames(<location>, username='XXXXX')
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
    

Support this module
-------------------

This project is free & open source, it would help greatly for you guys reading this to contribute, here are some of the ways that you can help make this Python Geocoder better.

Feedback
````````
Please feel free to give any feedback on this module. If you find any bugs or any enhancements to recommend please send some of your comments/suggestions to the `Github Issues Page <https://github.com/DenisCarriere/geocoder/issues>`_.

Twitter
```````
Speak up on Twitter and tell us how you use this Python Geocoder module by using the following Twitter Hashtags `@Addxy <https://twitter.com/search?q=%40Addxy>`_ `#geocoder <https://twitter.com/search?q=%23geocoder>`_.



