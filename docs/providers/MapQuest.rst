MapQuest
========

The geocoding service enables you to take an address and get the
associated latitude and longitude. You can also use any latitude
and longitude pair and get the associated address. Three types of
geocoding are offered: address, reverse, and batch.
Using Geocoder you can retrieve MapQuest's geocoded data from Geocoding Service.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.mapquest('San Francisco, CA', key='<API KEY>')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider mapquest --out geojson

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export MAPQUEST_API_KEY=<Secret API Key>

Parameters
----------

- `location`: Your search location you want geocoded.
- `method`: (default=geocode) Use the following:

  - geocode

References
----------

- `Mapquest Geocoding Service <http://www.mapquestapi.com/geocoding/>`_

