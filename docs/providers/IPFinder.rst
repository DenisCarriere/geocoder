IP Finder.io
==========

Use the ipfinder.io IP lookup API to quickly and simply integrate IP geolocation 
into your script or website. Save yourself the hassle of setting up local GeoIP 
libraries and having to remember to regularly update the data.

Geocoding (IP Address)
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.ipfinder('1.0.0.0')
    >>> g.status
    'OK'
    >>> g.city
    'South Brisbane'
    >>> g.json
    {'city': 'South Brisbane', 'continent_code': 'OC', 'continent_name': 'Oceania', 'country_code': 'AU', 'country_name': 'Australia', 'country_native_name': 'Australia', 'ip': '1.0.0.0', 'raw': {'status': 'ok', 'status_message': 'Query was successful', 'ip': '1.0.0.0', 'type': 'IPV4', 'continent_code': 'OC', 'continent_name': 'Oceania', 'country_code': 'AU', 'country_name': 'Australia', 'country_native_name': 'Australia', 'region_name': 'Queensland', 'city': 'South Brisbane'}, 'region_name': 'Queensland', 'status': 'ok', 'status_message': 'Query was successful', 'type': 'IPV4', 'ok': False}

    >>> # work with API KEY
    >>> import geocoder
    >>> g = geocoder.ipfinder('1.0.0.0',key='<key>')
    >>> g.json
    {'alpha3_code': 'AUS', 'calling_code': '61', 'capital': 'Canberra', 'city': 'South Brisbane', 'connection_asn': '13335', 'connection_domain': 'cloudflare.com', 'connection_organization': '  NOC', 'connection_type': 'Business', 'continent_code': 'OC', 'continent_name': 'Oceania', 'country_code': 'AU', 'country_flag': 'https://ipfinder.io/flag/aus.svg', 'country_flag_emoji': '🇦🇺', 'country_flag_emoji_unicode': 'U+1F1E6 U+1F1FA', 'country_name': 'Australia', 'country_native_name': 'Australia', 'currency_name': 'Australian dollar', 'currency_symbol': 'AUD', 'currency_symbol_native': '$', 'flag_png': 'https://ipfinder.io/flag/aus.png', 'ip': '1.0.0.0', 'is_proxy': True, 'languages_code': 'en', 'languages_name': 'English', 'languages_name_native': 'English', 'latitude': '-27.4748', 'longitude': '153.017', 'population': '23868800', 'proxy_type': 'Public proxy', 'raw': {'status': 'ok', 'status_message': 'Query was successful', 'ip': '1.0.0.0', 'type': 'IPV4', 'continent_code': 'OC', 'continent_name': 'Oceania', 'country_code': 'AU', 'country_name': 'Australia', 'country_native_name': 'Australia', 'region_name': 'Queensland', 'city': 'South Brisbane', 'latitude': '-27.4748', 'longitude': '153.017', 'location': {'capital': 'Canberra', 'country_flag': 'https://ipfinder.io/flag/aus.svg', 'flag_png': 'https://ipfinder.io/flag/aus.png', 'country_flag_emoji': '🇦🇺', 'country_flag_emoji_unicode': 'U+1F1E6 U+1F1FA', 'calling_code': '61', 'toplevel_domain': '.au', 'alpha3_code': 'AUS', 'population': '23868800', 'is_eu': False, 'is_ar': False}, 'time_zone': {'id': 'Australia/Lord_Howe', 'UTC': 'UTC+05:00', 'gmt_offset': 37800, 'current_time': '2019-08-27 03:20:40'}, 'currency': {'name': 'Australian dollar', 'symbol': 'AUD', 'symbol_native': '$'}, 'languages': {'code': 'en', 'name': 'English', 'name_native': 'English'}, 'connection': {'asn': '13335', 'organization': '  NOC', 'domain': 'cloudflare.com', 'type': 'Business'}, 'security': {'is_proxy': True, 'proxy_type': 'Public proxy', 'is_tor': None, 'is_spam': None, 'threat_level': 'High'}, 'header': {'total_user_agent': 0, 'list_user_agent': None}}, 'region_name': 'Queensland', 'status': 'ok', 'status_message': 'Query was successful', 'threat_level': 'High', 'time_zone_current_time': '2019-08-27 03:20:40', 'time_zone_gmt_offset': 37800, 'time_zone_id': 'Australia/Lord_Howe', 'time_zone_utc': 'UTC+05:00', 'toplevel_domain': '.au', 'type': 'IPV4', 'ok': False}

    ...

Geocode your own IP
~~~~~~~~~~~~~~~~~~~

To retrieve your own IP address, simply have `NULL`  as the input.

.. code-block:: python

    >>> import geocoder
    >>> g = geocoder.ipfinder()
    >>> g.status
    'OK'
    >>> g.ip
    '105.100.14.151'
    >>> g.json
    {'city': 'Ben ’Aknoûn', 'continent_code': 'AF', 'continent_name': 'Africa', 'country_code': 'DZ', 'country_name': 'Algeria', 'country_native_name': 'الجزائر', 'ip': '105.100.14.151', 'raw': {'status': 'ok', 'status_message': 'Query was successful', 'ip': '105.100.14.151', 'type': 'IPV4', 'continent_code': 'AF', 'continent_name': 'Africa', 'country_code': 'DZ', 'country_name': 'Algeria', 'country_native_name': 'الجزائر', 'region_name': 'Tipaza', 'city': 'Ben ’Aknoûn'}, 'region_name': 'Tipaza', 'status': 'ok', 'status_message': 'Query was successful', 'type': 'IPV4', 'ok': False}
    ...

Command Line Interface
----------------------

.. code-block:: bash

    $ geocode '1.0.0.0' --provider ipfinder | jq .
    $ # use API Key
    $ geocode '1.0.0.0' --provider ipfinder --key <key>  | jq . 


Parameters
----------

- `location`: Your search location you want geocoded.
- `location`: (optional) `NULL` will return your current IP address's location.
- `key`     :  API Key from IPFinder.
- `key`     : (optional)if left blank will use the `free` API KEY
- `method`  : (default=geocode) Use the following:

  - geocode

References
----------

- `IPFinder <https://ipfinder.io>`_
