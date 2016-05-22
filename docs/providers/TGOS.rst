TGOS
====

TGOS Map is official map service of Taiwan. It use EPSG:3826 coordinate system.
Beause of different coordinate system, this project need "pyproj" to transform the coordinate.
It's HTTP request need session state, so "beautifulsoup4" is needed to extract "pagekey" field.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.tgos('台北市內湖區內湖路一段735號')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '台北市內湖區內湖路一段735號' --provider tgos

Parameters
----------

- `location`: Your search location you want geocoded.
- `method`: (default=geocode)
- `useoddeven`: (default=False)
- `sid`: (default=Unknown)
- `method`: (default=queryaddr)

References
----------

- `TGOS Maps API <http://api.tgos.nat.gov.tw/TGOS_MAP_API/Web/Default.aspx>`_
