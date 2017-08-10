API Overview
============

.. _install:

Installation
~~~~~~~~~~~~

To install Geocoder, simply:

.. code-block:: bash

    $ pip install geocoder

Or on any of the supported `Linux distros`_:

.. _Linux distros: https://snapcraft.io/docs/core/install

.. code-block:: bash

    $ sudo snap install geocoder
    
GitHub Install
--------------

Installing the latest version from GitHub:

.. code-block:: bash

    $ git clone https://github.com/DenisCarriere/geocoder
    $ cd geocoder
    $ python setup.py install

Or on any of the supported `Linux distros`_:

.. _Linux distros: https://snapcraft.io/docs/core/install

.. code-block:: bash

    $ sudo snap install geocoder --edge

Examples
~~~~~~~~

Many properties are available once the geocoder object is created.

Forward Geocoding
-----------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.geojson
    >>> g.json
    >>> g.wkt
    >>> g.osm
    ...

Reverse Geocoding
-----------------

.. code-block:: python

    >>> g = geocoder.google([45.15, -75.14], method='reverse')
    >>> g.city
    >>> g.state
    >>> g.state_long
    >>> g.country
    >>> g.country_long
    ...

House Addresses
---------------

.. code-block:: python

    >>> g = geocoder.google("453 Booth Street, Ottawa ON")
    >>> g.housenumber
    >>> g.postal
    >>> g.street
    >>> g.street_long
    ...

IP Addresses
------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.ip('199.7.157.0')
    >>> g = geocoder.ip('me')
    >>> g.latlng
    >>> g.city

Command Line Interface
----------------------

Basic usesage with CLI

.. code-block:: bash

    $ geocode "Ottawa, ON" --provider bing

Saving results into a file

.. code-block:: bash

    $ geocode "Ottawa, ON"  >> ottawa.geojson

Reverse geocoding with CLI

.. code-block:: bash

    $ geocode "45.15, -75.14" --provider google --method reverse

Using JQ to query out a specific attribute

.. code-block:: bash

    $ geocode "453 Booth Street" -p canadapost --output json | jq .postal

Using a Session
---------------

In case you have several addresses to encode, to use persistent HTTP connection as recommended by the request-library
http://docs.python-requests.org/en/master/user/advanced/#session-objects
you might use the following:


.. code-block:: python

    >>> with requests.Session() as session:
    >>>    berlin = geocoder.google("Ritterstr. 12, 10969 Berlin", session=session)
    >>>    ottawa = geocoder.google("453 Booth Street, Ottawa ON", session=session)


Error Handling
~~~~~~~~~~~~~~

If there is an error in the connection to the server, the exception raised by the `requests` library will be
propagated up to the caller. This will be an instance of `requests.exceptions.RequestException`.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.osm("Tower Bridge, London", url="http://nonexistent.example.com")
    Traceback (most recent call last):
    
    ...
    
    requests.exceptions.ConnectionError: HTTPConnectionPool(host='nonexistent.example.com', port=80): Max retries exceeded with url: /?limit=1&format=jsonv2&addressdetails=1&q=foo (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x7f6b004d9390>: Failed to establish a new connection: [Errno -2] Name or service not known',))

If geocoder was able to contact the server, but no result could be found for the given search terms, the `ok`
attribute on the returned object will be `False`.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.osm("Mount Doom, Mordor")
    >>> g.ok
    False
    >>> g.json
    {'status': 'ERROR - No results found', 'location': 'Mount Doom, Mordor', 'provider': 'osm', 'status_code': 200, 'ok': False, 'encoding': 'utf-8'}
