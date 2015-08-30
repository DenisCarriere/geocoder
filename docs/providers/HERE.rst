HERE
====

Send a request to the geocode endpoint to find an address using a combination of
country, state, county, city, postal code, district, street and house number.
Using Geocoder you can retrieve geocoded data from the HERE Geocoder REST API.

Examples
~~~~~~~~

Basic Geocoding
---------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.here('Espoo, Finland')
    >>> g.json
    ...

Reverse Geocoding
-----------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google([45.15, -75.14], method='reverse')
    >>> g.json
    ...

Using API Key
-------------

If you want to use your own `app_id` & `app_code`, you must register an app 
at the `HERE Developer <https://developer.here.com/geocoder>`_.

.. code-block:: python

    >>> g = geocoder.here('Espoo, Finland',
                           app_id='<YOUR APP ID>',
                           app_code='<YOUR APP CODE>')


Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'Espoo, Finland' --provider here
    $ geocode '45.15, -75.14' --provider here --method reverse

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export APP_ID=<Secret APP ID>
    $ export APP_CODE=<Secret APP Code>

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `app_code`: (optional) use your own Application Code from HERE.
- `app_id`: (optional) use your own Application ID from HERE.
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
~~~~~~~~~~

- `HERE Geocoder REST API <https://developer.here.com/rest-apis/documentation/geocoder>`_
