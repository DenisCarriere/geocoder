Access to geocoder results
==========================

Work In Progress
~~~~~~~~~~~~~~~~

As for now, Geocoder always returns one result: the best match according to the queried provider.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('Mountain View, CA')
    >>> g.latlng
    ['37.38605', '-122.08385']
    >>> g.country
    'United States'
    >>> g.json
    ...


A **Work** is **In Progress** to support multiple results (you will find which providers support this feature on the `README file <https://github.com/DenisCarriere/geocoder/blob/master/README.md>`_). 

Simply add *maxRows* in your query:

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('Mountain View, CA', maxRows=5)
    >>> for result in g:
    ...   print(result.address, result.latlng)
    ...
    Mountain View ['37.38605', '-122.08385']
    Mountain View Elementary School ['34.0271', '-117.59116']
    Best Western Plus Mountainview Inn and Suites ['51.79516', '-114.62793']
    Best Western Mountainview Inn ['49.3338', '-123.1446']
    Mountain View Post Office ['37.393', '-122.07774']


Extending without breaking
--------------------------

The objective is to allow access to multiple results, without breaking the lib, neither adding to much complexity.

- all existing API calls shoul continue to Work
- access to all restults should be easy

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('Mountain View, CA', maxRows=5)

    # API calls still work on best match
    >>> g.latlng
    ['37.38605', '-122.08385']
    >>> g.country
    'United States'
    >>> g.json
    ...

    # the returned object support __len__, __getitem__, __iter__
    >>> print(len(g))
    5
    >>> g[3].latlng
    ['49.3338', '-123.1446']
    >>> for result in g:
    ...   print(result.address, result.latlng)
    ...

Note that the API calls are done on the best match from the provider, but you can change this behaviour by explicitely setting the default result to your desired one with the method *set_default_result*:

.. code-block:: python

    >>> g.set_default_result(3)
    >>> g.latlng
    ['49.3338', '-123.1446']
    >>> g.address
    'Best Western Plus Mountainview Inn and Suites'


"Breaking" change
-----------------

The `geojson` property called on `g` will not apply to the best match anymore, as it would for all others providers and properties

e.g. provider not supporting multiple results:

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.google('Mountain View, CA')
    >>> g.geojson
    {
    'type':'Feature',
    'properties':{
        'address':'Mountain View, CA, USA',
        ...
    },
    'bbox':[...],
    'geometry':{...}
    }

Instead, the *geojson* property will apply to **all** results, therefore returning a *FeatureCollection* of all *Features*:

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('Mountain View, CA', maxRows=2)
    >>> g.geojson
    {
    'type':'FeatureCollection',
    'features':[
        {
            'type':'Feature',
            'properties':{
                'address':'Mountain View',
                ...
            },
            'geometry':{...}
        },
        {
            'type':'Feature',
            'properties':{
                'address':'Mountain View Elementary School',
                ...
            },
            'geometry':{...}
        }
    ]
    }

More ?
------

The returned object *g* is an `orderedset <http://orderedset.readthedocs.io/en/latest/index.html>`_  because you might be interested in the actual order of the results given back by the provider, e.g. when querying the its hierarchy:

.. code-block:: python

    >>> import geocoder
    >>> main = geocoder.geonames('Mountain View, CA')
    >>> g = geocoder.geonames(main.geonames_id, method='hierarchy')
    >>> for result in g:
    ...   print(result.address, result.latlng)
    ...
    Earth ['0', '0']
    North America ['46.07323', '-100.54688']
    United States ['39.76', '-98.5']
    California ['37.25022', '-119.75126']
    Santa Clara County ['37.23249', '-121.69627']
    Mountain View ['37.38605', '-122.08385']
