TGOS
====

TGOS Map is official map service of Taiwan.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.tgos('台北市內湖區內湖路一段735號', key='<API KEY>')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '台北市內湖區內湖路一段735號' --provider tgos

Parameters
----------

- `location`: Your search location you want geocoded.
- `key`: Use your own API Key from TGOS.
- `method`: (default=geocode) Use the following:

  - geocode

- `language`: (default=taiwan) Use the following:

  - taiwan
  - english
  - chinese

References
----------

- `TGOS Maps API <http://api.tgos.nat.gov.tw/TGOS_MAP_API/Web/Default.aspx>`_
