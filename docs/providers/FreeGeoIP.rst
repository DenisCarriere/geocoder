FreeGeoIP.net
=============
freegeoip.net provides a public HTTP API for software developers to
search the geolocation of IP addresses. It uses a database of IP addresses
that are associated to cities along with other relevant information like
time zone, latitude and longitude.

You're allowed up to 10,000 queries per hour by default. Once this
limit is reached, all of your requests will result in HTTP 403,
forbidden, until your quota is cleared.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.freegeoip('99.240.181.199')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '99.240.181.199' --provider freegeoip

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `method`: (default=geocode) Use the following:

  - geocode

References
~~~~~~~~~~

- `API Reference <http://freegeoip.net/>`_
