Mapbox
======

The Mapbox Geocoding API lets you convert location text into
geographic coordinates (1600 Pennsylvania Ave NW → -77.0366,38.8971).

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.mapbox('San Francisco, CA', access_token='<ACCESS TOKEN>')
    >>> g.json
    ...

Reverse Geocoding
-----------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.mapbox([45.15, -75.14], method='reverse')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider mapbox --out geojson
    $ geocode '45.15, -75.14' --provider mapbox --method reverse

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export MAPBOX_ACCESS_TOKEN=<Secret Access Token>

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `proximity`: Search nearby [lat, lng].
- `access_token`: use your own access token from Mapbox.
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
~~~~~~~~~~

- `Mabpox Geocoding API <https://www.mapbox.com/developers/api/geocoding/>`_
- `Get Mabpox Access Token <https://www.mapbox.com/account>`_
    