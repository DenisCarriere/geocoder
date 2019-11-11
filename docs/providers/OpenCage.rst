Opencage
========

OpenCage Geocoder simple, easy, and open geocoding for the entire world
Our API combines multiple geocoding systems in the background.
Each is optimized for different parts of the world and types of requests.We aggregate the best results from open data sources and algorithms so you don't have to.
Each is optimized for different parts of the world and types of requests.
Using Geocoder you can retrieve OpenCage's geocoded data from OpenCage Geocoding Services.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.opencage('San Francisco, CA', key='<API Key>')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

Reverse Geocoding
~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.opencage([45.15, -75.14], method='reverse')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider opencage --out geojson --key '<API Key>' | jq .

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export OPENCAGE_API_KEY=<Secret API Key>

Parameters
----------

- `location`: Your search location you want geocoded.
- `key`: (optional) use your own API Key from OpenCage.
- `maxRows`: (default=1) Max number of results to fetch
- `countrycode`: (default=None) A string representing the country codes to restrict the search to (e.g. 'ca,us')
- `method`: (default=geocode) Use the following:

    - geocode

References
----------

- `OpenCage Geocoding Services <https://geocoder.opencagedata.com/api>`_

