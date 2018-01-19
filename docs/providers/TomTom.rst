TomTom
======

The Geocoding API gives developers access to TomTom’s first class geocoding service.
Developers may call this service through either a single or batch geocoding request.
This service supports global coverage, with house number level matching in over 50 countries,
and address point matching where available.
Using Geocoder you can retrieve TomTom's geocoded data from Geocoding API.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.tomtom('San Francisco, CA', key='<API KEY>')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider tomtom --out geojson

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export TOMTOM_API_KEY=<Secret API Key>

Parameters
----------

- `location`: Your search location you want geocoded.
- `key`: Use your own API Key from TomTom.
- `maxRows`: (default=1) Max number of results to fetch
- `countrySet`: Comma separated string of country codes (e.g. FR,ES). This will limit the search to the specified countries
- `lon`: Longitude e.g. lon=-121.89 lat./lon. where results should be biased (supplying a lat./lon. without a radius will only bias the search results to that area)
- `lat`: Latitude e.g.lat=37.337 lat./lon. where results should be biased (supplying a lat./lon. without a radius will only bias the search results to that area)
- `radius`: If radius and position are set, the results will be constrained to the defined area. The radius parameter is specified in meters.
- `method`: (default=geocode) Use the following:

  - geocode

References
----------

- `TomTom Geocoding API <https://developer.tomtom.com/online-search/online-search-documentation-geocoding/geocode>`_
