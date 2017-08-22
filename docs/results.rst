Access to geocoder results
==========================

[WIP] Multiple results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

If you would like to contribute and extend your favorite provider, please refer to the :ref:`Refactoring guide <wip_guide>`

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
- access to all results should be easy

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

The returned object *g* is a `MutableSequence (python >= 3.3) <https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence>`_ because you might be interested in the actual order of the results given back by the provider, e.g. when querying the its hierarchy:

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

.. _bbox:

BBox & Bounds
~~~~~~~~~~~~~

Overview
--------

Some Geocoder results will contain a BBox/Bounds of the geographical extent of the result.
There are two different widely adopted formats:

- `Bounds`: 
    An Object defined which was first implemented by **Google Maps API** and adopted by many other providers such as Leaflet.

    .. code-block:: python

        {
            northeast: [north, east],
            southwest: [south, west]
        }


- `BBox`:
    An Array of 4 numbers which follows the **GeoJSON** BBox specification.

    .. code-block:: python

        [west, south, east, north]

The major difference between both is the coordinates are flipped (LatLng => LngLat).

How to use 
----------

BBox or Bounds can be used in geocoding queries to limit the search to the given area. The two formats are accepted.

Let's look at a basic search for 'Paris'

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.geonames('Paris', maxRows=3, key='<USERNAME>')
    >>> print([(r.address, r.country, r.latlng) for r in g])
    [ ('Paris', 'France', ['48.85341', '2.3488']), 
      ('Paris', 'United States', ['33.66094', '-95.55551']), 
      ('Paris', 'Denmark', ['56.51417', '8.48996'])]

Now, if you are **not** interested in any of those matches, you might have an hard time to find yours. That's where proximity comes into play.

Let's assume for the sake of this example that you are seeking 'Paris' nearby [43.2, -80.3]. You just need to define your bbox, or your bounds, and use the 'proximity' parameter...


.. code-block:: python

    >>> bounds = {
            'southwest': [43.0, -80.5],
            'northeast': [43.5, -80.0]
        }
    >>> g = geocoder.geonames('Paris', proximity=bounds, key='<USERNAME>')
    >>> print([g.address, g.country, g.latlng])
    ['Paris', 'Canada', ['43.2001', '-80.38297']]

    # let's do the same with bounds
    >>> bbox = [-80.5, 43.0, -80.0, 43.5]
    >>> g = geocoder.geonames('Paris', proximity=bbox, key='<USERNAME>')
    >>> print([g.address, g.country, g.latlng])
    ['Paris', 'Canada', ['43.2001', '-80.38297']]

Actually, you can even just use a couple of (lat, lng) and the box will be created with a tolerance of 0.5 degrees in the four directions (west, south, east, north)

.. code-block:: python

    >>> latlng = [43.0, -80.0]
    >>> g = geocoder.geonames('Paris', proximity=latlng, key='<USERNAME>')
    >>> print([g.address, g.country, g.latlng])
    ['Paris', 'Canada', ['43.2001', '-80.38297']]


Compliant providers
-------------------

- :doc:`Google Places <providers/Google>`
- :doc:`Geonames <providers/GeoNames>`
- :doc:`Mapbox <providers/Mapbox>`

