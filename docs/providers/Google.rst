.. _google:

Google
======

Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway,
Mountain View, CA") into geographic coordinates (like latitude 37.423021 and
longitude -122.083739), which you can use to place markers or position the map.
Using Geocoder you can retrieve google's geocoded data from Google Geocoding API.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.json
    ...

Reverse Geocoding
-----------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google([45.15, -75.14], method='reverse')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'Mountain View, CA' --provider google
    $ geocode '45.15, -75.14' --provider google --method reverse

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse
  - timezone
  - elevation

References
~~~~~~~~~~

- `GitHub Repo <https://github.com/DenisCarriere/geocoder>`_
- `GitHub Wiki <https://github.com/DenisCarriere/geocoder/wiki>`_
- `Google Geocoding API <https://developers.google.com/maps/documentation/geocoding/>`_