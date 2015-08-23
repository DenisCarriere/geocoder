MaxMind
=======

MaxMind's GeoIP2 products enable you to identify the location,
organization, connection speed, and user type of your Internet
visitors. The GeoIP2 databases are among the most popular and
accurate IP geolocation databases available.
Using Geocoder you can retrieve Maxmind's geocoded data from MaxMind's GeoIP2.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.maxmind('199.7.157.0')
    >>> g.latlng
    [45.413140, -75.656703]
    >>> g.city
    'Toronto'
    >>> g.json
    ...

Lookup your own IP
------------------

To retrieve your own IP address, simply have `''` or `'me'` as the input.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.maxmind('')
    >>> g.latlng
    [45.413140, -75.656703]
    >>> g.ip
    '199.7.157.0'
    >>> g.json
    ...


Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '8.8.8.8' --provider maxmind | jq .

Parameters
~~~~~~~~~~

- `location`: Your search IP Address you want geocoded.
- `location`: (optional) `'me'` will return your current IP address's location.
- `method`: (default=geocode) Use the following:

  - geocode

References
~~~~~~~~~~

- `MaxMind's GeoIP2 <https://www.maxmind.com/en/geolocation_landing>`_