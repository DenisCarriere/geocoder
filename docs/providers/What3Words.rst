What3Words
==========

What3Words is a global grid of 57 trillion 3mx3m squares.
Each square has a 3 word address that can be communicated quickly,
easily and with no ambiguity.

**Addressing the world**

Everyone and everywhere now has an address

Examples
~~~~~~~~

Geocoding 3 Words
-----------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.w3w('embedded.fizzled.trial')
    >>> g.json
    ...

Reverse Geocoding
-----------------

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.w3w([45.15, -75.14], method='reverse')
    >>> g.json
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode 'embedded.fizzled.trial' --provider w3w
    $ geocode '45.15, -75.14' --provider w3w --method reverse

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

To make sure your API key is store safely on your computer, you can define that API key using your system's environment variables.

.. code-block:: bash

    $ export BING_API_KEY=<Secret API Key>

Parameters
~~~~~~~~~~

- `location`: Your search location you want geocoded.
- `key`: use your own API Key from Bing.
- `method`: (default=geocode) Use the following:

  - geocode
  - reverse

References
~~~~~~~~~~

- `API Reference <http://developer.what3words.com/>`_
- `Get W3W key <http://developer.what3words.com/api-register/>`_
