Python Geocoder
===============

|version| |build|

A simplistic Python Geocoder.

Geocoder is an Apache2 Licensed Geocoding library, written in Python.

.. code:: python
        >>> import geocoder
        >>> g = geocoder.google('Moscone Center')
        >>> g.latlng
        (37.784173, -122.401557)
        >>> g.city
        'San Francisco'
        ...

Installation
------------

You can install, upgrade, uninstall Geocoder with these commands:

.. code:: bash

        $ pip install geocoder
        $ pip install --upgrade geocoder
        $ pip uninstall geocoder


.. |version| image:: https://badge.fury.io/py/geocoder.png
   :target: http://badge.fury.io/py/geocoder
.. |build| image:: https://travis-ci.org/DenisCarriere/geocoder.png?branch=master
   :target: https://travis-ci.org/DenisCarriere/geocoder