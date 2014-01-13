Geocoder
========

A simplistic Python Geocoder.

Geocoder is an Apache2 Licensed Geocoding library, written in Python.

.. code-block:: pycon
    >>> import geocoder
    >>> g = geocoder.google('1600 Amphitheatre Pkwy, Mountain View, CA')
    >>> g.latlng
    [37.4219985, -122.0839544]
    >>> g.postal
    94043
    >>> g.address
    1600 Amphitheatre Parkway, Mountain View, CA 94043, USA
    >>> g.bbox
    [(37.4206495197085, -122.0853033802915), (37.4233474802915, -122.0826054197085)]
    >>> g.quality
    ROOFTOP
    >>> g.x, g.y
    -122.0839544 37.4219985
    ...

Geocoding Services
------------------

- Google
- Bing
- Nokia
- Mapquest
- OSM
- ESRI
- Geolytica
- MaxMind

Installation
------------

To install Geocoder, simplpy:

.. code-block:: bash
    $ pip install geocoder


Documentation
-------------

Coming Soon...
