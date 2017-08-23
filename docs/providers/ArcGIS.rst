ArcGIS
======

The World Geocoding Service finds addresses and places in all supported countries
from a single endpoint. The service can find point locations of addresses,
business names, and so on.  The output points can be visualized on a map,
inserted as stops for a route, or loaded as input for a spatial analysis.
an address, retrieving imagery metadata, or creating a route.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.arcgis('Redlands, CA')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'Redlands, CA' --provider arcgis

Parameters
----------

- `location`: Your search location you want geocoded.
- `maxRows`: (default=1) Max number of results to fetch
- `limit`: *Deprecated*, same as maxRows
- `method`: (default=geocode) Use the following:

  - geocode

References
----------

- `ArcGIS Geocode API <https://developers.arcgis.com/rest/geocode/api-reference/overview-world-geocoding-service.htm>`_
