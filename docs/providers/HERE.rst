HERE
====

Send a request to the geocode endpoint to find an address using a combination of
country, state, county, city, postal code, district, street and house number.
Using Geocoder you can retrieve geocoded data from the HERE Geocoder REST API.

Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.here('Espoo, Finland')
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

A bounding box can be supplied as an array of the form [minX, minY, maxX, maxY] to restrict results.

.. code-block:: python

    >>> import geocoder
    >>> bbox = [-118.604794, 34.172684, -118.500938, 34.236144]
    >>> g = geocoder.here("Winnetka", bbox=bbox)
    >>> g.address
    "Winnetka, CA, United States"
    >>> g = geocoder.here("Winnetka")
    >>> g.address
    "Winnetka, IL, United States"
    ...

Please refer to :ref:`this section <bbox>` for more details.
Reverse Geocoding
~~~~~~~~~~~~~~~~~

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
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export HERE_APP_ID=<Secret APP ID>
    $ export HERE_APP_CODE=<Secret APP Code>

Parameters
----------

- `location`: Your search location you want geocoded.
- `app_code`: (optional) use your own Application Code from HERE.
- `app_id`: (optional) use your own Application ID from HERE.
- `bbox`: Search within a bounding box [minX, minY, maxX, maxY]. Pass as an array.
- `maxRows`: (default=1) Max number of results to fetch
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
----------

- `HERE Geocoder REST API <https://developer.here.com/rest-apis/documentation/geocoder>`_
