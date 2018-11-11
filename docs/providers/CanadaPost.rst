CanadaPost
==========

The next generation of address finders, AddressComplete uses intelligent, fast
searching to improve data accuracy and relevancy. Simply start typing a business
name, address or Postal Code and AddressComplete will suggest results as you go.
Using Geocoder you can retrieve CanadaPost's geocoded data from AddressComplete API.

Geocoding (Postal Code)
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.canadapost('453 Booth Street, Ottawa', key='<API KEY>')
    >>> g.postal
    'K1R 7K9'
    >>> g.json
    ...

This provider may return multiple results by setting the parameter `maxRows` to the desired number (1 by default). You can access those results as described in the page ':doc:`/results`'.

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '453 Booth Street, Ottawa' --provider canadapost | jq .postal

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export CANADAPOST_API_KEY=<Secret API Key>

Parameters
----------

- `location`: Your search location you want geocoded.
- `key`: (optional) API Key from CanadaPost Address Complete.
- `language`: (default=en) Output language preference.
- `country`: (default=ca) Geofenced query by country.
- `maxRows`: (default=1) Max number of results to fetch
- `method`: (default=geocode) Use the following:

  - geocode

References
----------

- `AddressComplete API <https://www.canadapost.ca/pca/>`_
