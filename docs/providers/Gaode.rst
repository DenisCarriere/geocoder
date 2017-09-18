Gaode
=====

Gaode(AMap) Maps Geocoding API is a free open the API, the default quota
one 2000 times / day.

This API only support china.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.gaode('方恒国际中心A座', key='<API KEY>')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '方恒国际中心A座' --provider gaode

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export GAODE_API_KEY=<Secret API Key>

Parameters
----------

- `location`: Your search location you want geocoded.
- `key`: Gaode API key.
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
----------

- `API Reference <http://lbs.amap.com/api/webservice/guide/api/georegeo>`_
- `Get Gaode key <http://lbs.amap.com/dev/>`_
