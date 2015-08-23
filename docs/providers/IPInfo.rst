IP Info.io
==========

Use the IPInfo.io IP lookup API to quickly and simply integrate IP geolocation 
into your script or website. Save yourself the hassle of setting up local GeoIP 
libraries and having to remember to regularly update the data.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.ipinfo('199.7.157.0')
    >>> g.latlng
    [45.413140, -75.656703]
    >>> g.city
    'Toronto'
    >>> g.json
    ...

Lookup your own IP
------------------

To retrieve your own IP address, simply have `''` as the input.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.ipinfo('')
    >>> g.latlng
    [45.413140, -75.656703]
    >>> g.ip
    '199.7.157.0'
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '199.7.157.0' --provider ipinfo | jq .

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `location`: (optional) `''` will return your current IP address's location.
- `method`: (default=geocode) Use the following:

  - geocode

References
~~~~~~~~~~

- `IpinfoIo <https://ipinfo.io>`_