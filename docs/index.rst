.. Geocoder documentation master file, created by
   sphinx-quickstart on Fri Jul 31 14:40:36 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Geocoder: Simple GeoJSON
========================

Release v\ |version|. (:ref:`Installation <install>`)

Simple and consistent geocoding library written in Python.

.. image:: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
   :target: https://travis-ci.org/DenisCarriere/geocoder

.. image:: https://coveralls.io/repos/DenisCarriere/geocoder/badge.png
   :target: https://coveralls.io/r/DenisCarriere/geocoder

Many online providers such as Google & Bing have geocoding services,
these providers do not include Python libraries and have different
JSON responses between each other.

.. image:: http://i.imgur.com/vUJKCGl.png
   :width: 570
   :height: 340
   :alt: Geocoding Providers


Consistant JSON & GeoJSON responses from various providers.

.. code-block:: python

    >>> g = geocoder.google('New York City')
    >>> g.latlng
    [40.7127837, -74.0059413]
    >>> g.geojson
    >>> g.json
    ...


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


Providers
~~~~~~~~~

.. csv-table::
    :header: Provider, Optimal, Access
    :widths: 20, 15, 15

    :ref:`ArcGIS <ArcGIS>`, World
    :ref:`Baidu <Baidu>`, China, API key
    :ref:`Bing <Bing>`, World, API key
    :ref:`CanadaPost <CanadaPost>`, Canada, API key
    :ref:`FreeGeoIP <FreeGeoIP>`, World
    :ref:`Geocoder.ca <Geocoder-ca>`, North America, Rate Limit
    :ref:`GeoNames <GeoNames>`, World, Username
    :ref:`GeoOttawa <GeoOttawa>`, Ottawa
    :ref:`Google <Google>`, World, Rate Limit
    :ref:`HERE <HERE>`, World, API key
    :ref:`Mapbox <Mapbox>`, World, API key
    :ref:`MapQuest <MapQuest>`, World, API key
    :ref:`MaxMind <MaxMind>`, World
    :ref:`OpenCage <OpenCage>`, World, API key
    :ref:`OpenStreetMap <OpenStreetMap>`, World
    :ref:`TomTom <TomTom>`, World, API key
    :ref:`What3Words <What3Words>`, World, API key
    :ref:`Yahoo <Yahoo>`, World
    :ref:`Yandex <Yandex>`, Russia


Contributor Guide
-----------------

If you want to contribute to the project, this part of the documentation is for
you.

.. toctree::
   :maxdepth: 1

   authors

