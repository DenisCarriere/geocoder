Google
======

Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway,
Mountain View, CA") into geographic coordinates (like latitude 37.423021 and
longitude -122.083739), which you can use to place markers or position the map.
Using Geocoder you can retrieve google's geocoded data from Google Geocoding API.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.json
    ...

Reverse Geocoding
~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google([45.15, -75.14], method='reverse')
    >>> g.json
    ...

Timezone
~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google([45.15, -75.14], method='timezone')
    >>> g.timeZoneName
    'Eastern Daylight Time'
    >>> g.timeZoneId
    'America/Toronto'
    >>> g.dstOffset
    3600
    >>> g.rawOffset
    -18000

Component Filtering
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> g = geocoder.google("Santa Cruz", components="country:ES")

Read me at Google's Geocoding API

https://developers.google.com/maps/documentation/geocoding/intro#ComponentFiltering


Places
~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google('white house', method='places')
    >>> g.latlng
    [38.8976763, -77.0365298]
    >>> g.address
    u'1600 Pennsylvania Ave NW, Washington, DC 20500, United States'
    >>> g.json
    ...


Elevation
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google([45.15, -75.14], method='elevation')
    >>> g.meters
    71.0
    >>> g.feet
    232.9
    >>> g.resolution
    38.17580795288086

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'Mountain View, CA' --provider google
    $ geocode 'white house' --provider google --method places
    $ geocode '45.15, -75.14' --provider google --method reverse
    $ geocode '45.15, -75.14' --provider google --method timezone
    $ geocode '45.15, -75.14' --provider google --method elevation

Environment Variables
---------------------

To make sure your API key is stored safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export GOOGLE_API_KEY=<Secret API Key>
    $ export GOOGLE_CLIENT=<Secret Client>
    $ export GOOGLE_CLIENT_SECRET=<Secret Client Secret>

Parameters
----------

- `location`: Your search location you want geocoded.
- `key`: Your Google developers free key.
- `language`: 2-letter code of preferred language of returned address elements.
- `client`: Google for Work client ID. Use with client_secret. Cannot use with key parameter
- `client_secret`: Google for Work client secret. Use with client.
- `proximity`: Search within given area (bbox, bounds, or around latlng)
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse
  - timezone
  - elevation
  - places


References
----------

- `Google Geocoding API <https://developers.google.com/maps/documentation/geocoding/>`_
- `Google Geocoding Best Practices <https://developers.google.com/maps/documentation/geocoding/best-practices/>`_
- `Google Places API <https://developers.google.com/places/web-service/intro/>`_
