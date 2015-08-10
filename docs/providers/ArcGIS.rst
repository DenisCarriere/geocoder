ArcGIS
======

The World Geocoding Service finds addresses and places in all supported countries
from a single endpoint. The service can find point locations of addresses,
business names, and so on.  The output points can be visualized on a map,
inserted as stops for a route, or loaded as input for a spatial analysis.
an address, retrieving imagery metadata, or creating a route.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.arcgis('Redlands, CA')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'Redlands, CA' --provider arcgis

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `method`: (default=geocode) Use the following:

  - geocode

References
~~~~~~~~~~

- `ArcGIS Geocode API <https://developers.arcgis.com/rest/geocode/api-reference/geocoding-find.htm>`_



