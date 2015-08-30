GeoNames
========

GeoNames is mainly using REST webservices. Find nearby postal codes / reverse geocoding
This service comes in two flavours. You can either pass the lat/long or a postalcode/placename.

Using Geocoder you can retrieve GeoNames's geocoded data from GeoNames REST Web Services.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('New York City', username='<USERNAME>')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'New York City' --provider geonames

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export GEONAMES_USERNAME=<Secret Username>

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `username`: (required) needs to be passed with each request.
- `method`: (default=geocode) Use the following:

  - geocode

References
~~~~~~~~~~

- `GeoNames REST Web Services <http://www.geonames.org/export/web-services.html>`_
