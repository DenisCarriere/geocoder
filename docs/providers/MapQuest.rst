MapQuest
========

The geocoding service enables you to take an address and get the
associated latitude and longitude. You can also use any latitude
and longitude pair and get the associated address. Three types of
geocoding are offered: address, reverse, and batch.
Using Geocoder you can retrieve MapQuest's geocoded data from Geocoding Service.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.mapquest('San Francisco, CA', key='<API KEY>')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

A bounding box can be supplied as an array of the form [minX, minY, maxX, maxY] to bump results within a the bounding box to the top.

.. code-block:: python

    >>> import geocoder
    >>> bbox = [-118.604794, 34.172684, -118.500938, 34.236144]
    >>> g = geocoder.here("Winnetka", bbox=bbox)
    >>> g.lng, g.lat
    (-118.571098, 34.213299)
    >>> g = geocoder.here("Winnetka")
    >>> g.lng, g.lat
    (-87.734719, 42.107106)
    ...

This provider gives access to batch geocoding services that allow you to geocode up to 100 addresses at the same time.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.mapquest(['Mountain View, CA', 'Boulder, Co'], method='batch')
    >>> for result in g:
    ...   print(result.address, result.latlng)
    ...
    ('Mountain View', [37.39008, -122.08139])
    ('Boulder', [40.015831, -105.27927])
    ...

Reverse Geocoding
~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.mapquest([45.15, -75.14], method='reverse', key='<API KEY>')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider mapquest --out geojson

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export MAPQUEST_API_KEY=<Secret API Key>

Parameters
----------

- `location`: Your search location you want geocoded.
- `maxRows`: (default=1) Max number of results to fetch
- `bbox`: Search within a bounding box [minX, minY, maxX, maxY]. Pass as an array.
- `method`: (default=geocode) Use the following:

  - geocode
  - batch

References
----------

- `Mapquest Geocoding Service <http://www.mapquestapi.com/geocoding/>`_
- `Get Free API Key <https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free>`_
