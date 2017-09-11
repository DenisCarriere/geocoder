GeoOttawa
=========

This data was collected in the field using GPS software on handheld computers. Not all information has been verified for accuracy and therefore should only be used in an advisory capacity. Forestry Services reserves the right to revise the data pursuant to further inspection/review. If you find any errors or omissions, please report them to 3-1-1.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.ottawa('453 Booth Street')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '453 Booth Street' --provider ottawa

Parameters
----------

- `location`: Your search location you want geocoded.
- `maxRows`: (default=1) Max number of results to fetch
- `method`: (default=geocode) Use the following:

  - geocode

References
----------

- `GeoOttawa Map <http://maps.ottawa.ca/geoottawa/>`_



