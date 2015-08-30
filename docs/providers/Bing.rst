Bing
====

The Bing™ Maps REST Services Application Programming Interface (API)
provides a Representational State Transfer (REST) interface to
perform tasks such as creating a static map with pushpins, geocoding
an address, retrieving imagery metadata, or creating a route.
Using Geocoder you can retrieve Bing's geocoded data from Bing Maps REST Services.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.bing('Mountain View, CA', key='<API KEY>')
    >>> g.json
    ...

Reverse Geocoding
-----------------

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
~~~~~~~~~~~~~~~~~~~~~

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export BING_API_KEY=<Secret API Key>

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `key`: use your own API Key from Bing.
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
~~~~~~~~~~

- `Bing Maps REST Services <http://msdn.microsoft.com/en-us/library/ff701714.aspx>`_
