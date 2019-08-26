Geocoder: Simple, Consistent
============================

Release v\ |version|. (:ref:`Installation <install>`)

Simple and consistent geocoding library written in Python.

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

It can be very difficult sometimes to parse a particular geocoding provider
since each one of them have their own JSON schema.

Here is a typical example of retrieving a Lat & Lng from Google using Python,
things shouldn't be this hard.

.. code-block:: python

    >>> import requests
    >>> url = 'https://maps.googleapis.com/maps/api/geocode/json'
    >>> params = {'sensor': 'false', 'address': 'Mountain View, CA'}
    >>> r = requests.get(url, params=params)
    >>> results = r.json()['results']
    >>> location = results[0]['geometry']['location']
    >>> location['lat'], location['lng']
    (37.3860517, -122.0838511)

Now lets use Geocoder to do the same task.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.latlng
    (37.3860517, -122.0838511)

Testimonials
------------

**Tobias Siebenlist**
    Geocoder: great geocoding library by @DenisCarriere.

**mcbetz**
    Very good companion for Geocoder. Glad to see Python getting more geo libraries for Non-GIS users.


API Documentation
-----------------

If you are looking for information on a specific function, class or method,
this part of the documentation is for you.

.. toctree::
    :maxdepth: 3

    api
    results
    wip_guide
    examples/QGISFieldCalculator.rst


Providers
---------

Detailed information about each individual provider that are within Geocoder.

.. toctree::
    :maxdepth: 2

    providers/ArcGIS.rst
    providers/Baidu.rst
    providers/Bing.rst
    providers/CanadaPost.rst
    providers/FreeGeoIP.rst
    providers/Gaode.rst
    providers/GeocodeFarm.rst
    providers/Geocoder-ca.rst
    providers/GeoNames.rst
    providers/GeoOttawa.rst
    providers/Google.rst
    providers/HERE.rst
    providers/IPInfo.rst
    providers/LocationIQ.rst
    providers/Mapbox.rst
    providers/MapQuest.rst
    providers/MaxMind.rst
    providers/OpenCage.rst
    providers/OpenStreetMap.rst
    providers/Tamu.rst
    providers/TomTom.rst
    providers/What3Words.rst
    providers/Yahoo.rst
    providers/Yandex.rst
    providers/TGOS.rst
    providers/IPFinder.rst


Contributor Guide
-----------------

If you want to contribute to the project, this part of the documentation is for
you.

.. toctree::
    :maxdepth: 1

    authors
