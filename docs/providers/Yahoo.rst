Yahoo
=====

Yahoo PlaceFinder is a geocoding Web service that helps developers make
their applications location-aware by converting street addresses or
place names into geographic coordinates (and vice versa).
Using Geocoder you can retrieve Yahoo's geocoded data from Yahoo BOSS Geo Services.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.yahoo('San Francisco, CA')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider yahoo --out geojson

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `method`: (default=geocode) Use the following:

  - geocode

References
~~~~~~~~~~

- `Yahoo BOSS Geo Services <https://developer.yahoo.com/boss/geo/>`_
