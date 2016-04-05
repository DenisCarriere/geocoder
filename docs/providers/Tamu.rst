Tamu
======


Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.tamu(
                us_address,
                city=us_city,
                state=us_state,
                zipcode=us_zipcode)
                key='<API KEY>')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'San Francisco, CA' --provider tamu --city San Francisco --state CA --zipcode 94105 

Environment Variables
----------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export TAMU_API_KEY=<Secret API Key>

Parameters
----------

- `location`: The street address of the location you want geocoded.
- `city`: The city of the location to geocode.
- `state`: The state of the location to geocode.
- `zipcode`: The zipcode of the location to geocode.
- `key`: use your own API Key from TomTom.
- `method`: (default=geocode) Use the following:

  - geocode

Census Fields
-------------

References
----------
- `Tamu Geocoding API <http://geoservices.tamu.edu/Services/Geocode/WebService/>`_
