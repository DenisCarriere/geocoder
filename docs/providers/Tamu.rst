Tamu
====
The Texas A&M Geoservices Geocoding API provides output including Lat and Lon
and numerous census data values.

An API key linked to an account with Texas A&M is required.

Tamu's API differs from the other geocoders in this package in that it
requires the street address, city, state, and US zipcode to be passed in
separately, rather than as a single string.  Because of this requirement,
the "location", "city", "state", and "zipcode" parameters are all required
when using the Tamu provider.  The "location" parameter should contain only
the street address of the location.
 
Geocoding
~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.tamu(
                '595 Market St',
                city='San Francisco',
                state='California',
                zipcode='94105',
                key='demo')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '595 Market St' --provider tamu --city San Francisco --state CA --zipcode 94105 --key <Secret API Key>

Environment Variables
---------------------

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export TAMU_API_KEY=<Secret API Key>

Parameters
----------

- `location`: The street address of the location you want geocoded.
- `city`: The city of the location to geocode.
- `state`: The state of the location to geocode.
- `zipcode`: The zipcode of the location to geocode.
- `key`: use your own API Key from Tamu.
- `method`: (default=geocode) Use the following:

  - geocode

Census Output Fields
--------------------
Note: "FIPS" stands for "Federal Information Processing System"

- `census_block`: Census Block value for location
- `census_tract`: Census Tract value for location
- `census_county_fips`: Census County FIPS value
- `census_cbsa_fips`: Census Core Base Statistical Area FIPS value
- `census_mcd_fips`: Census Minor Civil Division FIPS value
- `census_msa_fips`: Census Metropolitan Statistical Area FIPS value
- `census_place_fips`: Census Place FIPS value
- `census_state_fips`: Census State FIPS value
- `census_year`: Census Year from which these values originated


References
----------
- `Tamu Geocoding API <http://geoservices.tamu.edu/Services/Geocode/WebService/>`_
