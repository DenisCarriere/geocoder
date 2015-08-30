Baidu
=====

Baidu Maps Geocoding API is a free open the API, the default quota
one million times / day.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder # pip install geocoder
    >>> g = geocoder.baidu('中国', key='<API KEY>')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '中国' --provider baidu

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export BAIDU_API_KEY=<Secret API Key>

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `key`: Baidu API key.
- `method`: (default=geocode) Use the following:

  - geocode

References
~~~~~~~~~~

- `API Reference <http://developer.baidu.com/map/index.php?title=webapi/guide/webservice-geocoding>`_
- `Get Baidu key <http://lbsyun.baidu.com/apiconsole/key>`_
