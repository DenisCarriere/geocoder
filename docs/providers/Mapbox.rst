Mapbox
======

The Mapbox Geocoding API lets you convert location text into
geographic coordinates (1600 Pennsylvania Ave NW → -77.0366,38.8971).

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.mapbox('San Francisco, CA', key='<TOKEN>')
    >>> g.json
    ...

This provider may return multiple results. You can access those results as described in the page ':doc:`/results`'.

Request feature data that best matches input and is biased to the given {latitude} and {longitude} coordinates. In the above example, a query of "200 Queen Street" returns a subset of all relevant addresses in the world. By adding the proximity option, this subset can be biased towards a given area, returning a more relevant set of results. In addition, a bounding box can be supplied to restrict results.

.. code-block:: python

    >>> import geocoder
    >>> latlng = [45.3, -66.1]
    >>> g = geocoder.mapbox("200 Queen Street", proximity=latlng)
    >>> g.address
    "200 Queen St W, Saint John, New Brunswick E2M 2C8, Canada"
    >>> g = geocoder.mapbox("200 Queen Street")
    >>> g.address
    "200 Queen Street, Colac, Victoria 3250, Australia"
    >>> bbox = [-118.604794, 34.172684, -118.500938, 34.236144]
    >>> g = geocoder.mapbox("Winnetka", bbox=bbox)
    >>> g.address
    "Winnetka, Winnetka, California 91306, United States"
    >>> g = geocoder.mapbox("Winnetka")
    >>> g.address
    "Winnetka Heights, Dallas, Texas 75211, United States"
    ...

Please refer to :ref:`this section <bbox>` for more details.

Reverse Geocoding
~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> latlng = [45.3, -105.1]
    >>> g = geocoder.mapbox(latlng, method='reverse')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider mapbox --out geojson
    $ geocode '45.15, -75.14' --provider mapbox --method reverse

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export MAPBOX_ACCESS_TOKEN=<Secret Access Token>

Parameters
----------

- `location`: Your search location you want geocoded.
- `proximity`: Search nearby [lat, lng].
- `bbox`: Search within a bounding box [minX, minY, maxX, maxY]. Pass as an array.
- `key`: Use your own access token from Mapbox.
- `country`: Filtering by country code {cc} ISO 3166 alpha 2.
- `proximity`: Search within given area (bbox, bounds, or around latlng)
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
----------

- `Mapbox Geocoding API <https://www.mapbox.com/developers/api/geocoding/>`_
- `Get Mapbox Access Token <https://www.mapbox.com/account>`_
