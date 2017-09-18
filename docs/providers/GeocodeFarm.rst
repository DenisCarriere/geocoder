GeocodeFarm
===========

Geocode.Farm is one of the few providers that provide this highly
    specialized service for free. We also have affordable paid plans, of
    course, but our free services are of the same quality and provide the same
    results. The major difference between our affordable paid plans and our
    free API service is the limitations. On one of our affordable paid plans
    your limit is set based on the plan you signed up for, starting at 25,000
    query requests per day (API calls). On our free API offering, you are
    limited to 250 query requests per day (API calls).

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geocodefarm('Mountain View, CA')
    >>> g.json
    ...

This provider may return multiple results. You can access those results as described in the page ':doc:`/results`'.

Reverse Geocoding
~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geocodefarm([45.15, -75.14], method='reverse')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'Mountain View, CA' --provider geocodefarm
    $ geocode '45.15, -75.14' --provider geocodefarm --method reverse

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export GEOCODEFARM_API_KEY=<Secret API Key>

Parameters
----------

- `location`: The string to search for. Usually a street address. If reverse then should be a latitude/longitude.
- `key`: (optional) API Key. Only Required for Paid Users.
- `lang`: (optional) 2 digit lanuage code to return results in. Currently only "en"(English) or "de"(German) supported.
- `country`: (optional) The country to return results in. Used for biasing purposes and may not fully filter results to this specific country.
- `maxRows`: (default=1) Max number of results to fetch
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
----------

- `GeocodeFarm API Documentation <https://geocode.farm/geocoding/free-api-documentation/>`_
