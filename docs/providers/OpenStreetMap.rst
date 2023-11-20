OpenStreetMap
=============

Nominatim (from the Latin, 'by name') is a tool to search OSM data by name
and address and to generate synthetic addresses of OSM points (reverse geocoding).
Using Geocoder you can retrieve OSM's geocoded data from Nominatim.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.osm('New York city')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

Nominatim Server
~~~~~~~~~~~~~~~~

Setting up your own offline Nominatim server is possible, using Ubuntu 20.04 or 22.04 OS and following the `Nominatim Install`_ instructions.  A Docker image is also available.  This enables you to request as much geocoding as your little heart desires!

.. code-block:: python

    >>> url = 'http://localhost/nominatim/'
    >>> url = 'localhost'
    >>> g = geocoder.osm("New York City", url=url)
    >>> g.json
    ...

OSM Addresses
~~~~~~~~~~~~~

The `addr tag`_ is the prefix for several `addr:*` keys to describe addresses.

This format is meant to be saved as a CSV and imported into JOSM.

.. code-block:: python

    >>> g = geocoder.osm('11 Wall Street, New York')
    >>> g.osm
    {
        "x": -74.010865,
        "y": 40.7071407,
        "addr:country": "United States of America",
        "addr:state": "New York",
        "addr:housenumber": "11",
        "addr:postal": "10005",
        "addr:city": "NYC",
        "addr:street": "Wall Street"
    }


Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'New York city' --provider osm --out geojson | jq .
    $ geocode 'New York city' -p osm -o osm
    $ geocode 'New York city' -p osm --url localhost

Parameters
----------

- `location`: Your search location you want geocoded.
- `url`: Custom OSM Server (ex: localhost)
- `maxRows`: (default=1) Max number of results to fetch
- `limit`: *Deprecated*, same as maxRows
- `method`: (default=geocode) Use the following:

    - geocode

References
----------

- `Nominatim <http://wiki.openstreetmap.org/wiki/Nominatim>`_
- `Nominatim Install`_
- `addr tag`_


.. _addr tag: http://wiki.openstreetmap.org/wiki/Key:addr
.. _Nominatim Install: http://nominatim.org/release-docs/latest/admin/Installation

