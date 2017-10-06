LocationIQ
===========

`LocationIQ`_ provides geocoding based on OpenStreetMap's `Nominatim`_. It is fully compatible
with OSM except for the requirement of an API Key. Please refer to the :doc:`./OpenStreetMap` docs
for more details. You can signup for a free API Key `here <http://locationiq.org/#register>`.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.locationiq('New York city', key='...')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

Reverse Geocoding
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.locationiq([45.15, -75.14], key='...', method='reverse')
    >>> g.json
    ...

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export LOCATIONIQ_API_KEY=<Secret API Key>

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'New York city' --provider locationiq --key <key> --output geojson | jq .
    $ geocode 'New York City' --provider locationiq --key <key> --output osm

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

- `LocationIQ <https://locationiq.org>`_
- `Nominatim <http://wiki.openstreetmap.org/wiki/Nominatim>`_
