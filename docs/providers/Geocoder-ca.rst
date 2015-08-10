Geocoder.ca
===========

Geocoder.ca - A Canadian and US location geocoder.
Using Geocoder you can retrieve Geolytica's geocoded data from Geocoder.ca.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geolytica('Ottawa, ON')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'Ottawa, ON' --provider geolytica

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `method`: (default=geocode) Use the following:

  - geocode

References
~~~~~~~~~~

- `API Reference <http://geocoder.ca/?api=1>`_

