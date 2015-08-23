Opencage
========

OpenCage Geocoder simple, easy, and open geocoding for the entire world
Our API combines multiple geocoding systems in the background.
Each is optimized for different parts of the world and types of requests.We aggregate the best results from open data sources and algorithms so you don't have to.
Each is optimized for different parts of the world and types of requests.
Using Geocoder you can retrieve OpenCage's geocoded data from OpenCage Geocoding Services.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.opencage('San Francisco, CA')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider opencage --out geojson | jq .

Parameters
----------

- `location`: Your search location you want geocoded.
- `key`: (optional) use your own API Key from OpenCage.
- `method`: (default=geocode) Use the following:
    - geocode

References
----------

- `OpenCage Geocoding Services <http://geocoder.opencagedata.com/api.html>`_

