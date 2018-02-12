Bing
====

The Bing™ Maps REST Services Application Programming Interface (API)
provides a Representational State Transfer (REST) interface to
perform tasks such as creating a static map with pushpins, geocoding
an address, retrieving imagery metadata, or creating a route.
Using Geocoder you can retrieve Bing's geocoded data from Bing Maps REST Services.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.bing('Mountain View, CA', key='<API KEY>')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'. If you want to search using a structured address, use the detailed method.

.. code-block:: python

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.bing(None, locality='Ottawa', adminDistrict='Ontario', method='details', key='<API KEY>')
    >>> g.json
    ...

Reverse Geocoding
~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.bing([45.15, -75.14], method='reverse')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'Mountain View, CA' --provider bing
    $ geocode '45.15, -75.14' --provider bing --method reverse

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export BING_API_KEY=<Secret API Key>

Parameters
----------

- `location`: Your search location you want geocoded.
- `addressLine`: (method=details) Official street line, uses `location` if not provided.
- `postalCode`: (method=details) The post code, postal code, or ZIP.
- `locality`: (method=details) The locality, such as the city or neighborhood.
- `adminDistrict`: (method=details) The subdivision name in the country of region for an address.
- `countryRegion`: (method=details) The ISO country code for the country.
- `key`: use your own API Key from Bing.
- `maxRows`: (default=1) Max number of results to fetch
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
----------

- `Bing Maps REST Services <http://msdn.microsoft.com/en-us/library/ff701714.aspx>`_
