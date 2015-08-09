.. _mapbox:

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
    >>> g = geocoder.mapbox('San Francisco, CA')
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

Parameters
----------

- `location`: Your search location you want geocoded.
- `proximity`: Search nearby [lat, lng].
- `method`: (default=geocode) Use the following:
    - geocode
    - reverse
    - batch

References
----------

- `GitHub Repo <https://github.com/DenisCarriere/geocoder>`_
- `Mabpox Geocoding API <https://www.mapbox.com/developers/api/geocoding/>`_
- `Get Mabpox Access Token <https://www.mapbox.com/account>`_
    