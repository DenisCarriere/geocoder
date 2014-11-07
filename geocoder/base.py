#!/usr/bin/python
# coding: utf8

from __future__ import print_function
import requests
import sys


class Base(object):
    _base_parameter  = [':param ``location``: Your search location you want geocoded.']
    _base_reference = ['[GitHub Repo](https://github.com/DenisCarriere/geocoder)',
                       '[GitHub Wiki](https://github.com/DenisCarriere/geocoder/wiki)']
    _exclude = ['parse', 'json', 'url', 'attributes', 'help', 'debug', 'short_name',
                'api', 'content', 'params', 'status_code',
                'api_key', 'ok', 'key', 'id', 'x', 'y', 'latlng',
                'bbox', 'geometry', 'wkt','locality', 'province','street_number', 'rate_limited_get']
    _example = []
    _timeout = 5.0
    _error = None
    _headers = {}
    _attributes = []

    @staticmethod
    def rate_limited_get(*args, **kwargs):
        return requests.get(*args, **kwargs)

    def __repr__(self):
        return "<[{0}] {1} [{2}]>".format(self.status, self.provider, self.address)

    def debug(self):
        print('# Debug')
        print('## Connection')
        print('* URL: [{0}]({1})'.format(self.provider.title(), self.url))
        print('* Status: {0}'.format(self.status))
        print('* Status Code: {0}'.format(self.status_code))
        for key, value in self.params.items():
            print('* Parameter [{0}]: {1}'.format(key, value))
        print('')
        print('## JSON Attributes')
        for key, value in self.json.items():
            print('* {0}: {1}'.format(key, value))
        print('')
        print('## Provider\'s Attributes')
        if self.parse:
            for key, value in self.parse.items():
                if value:
                    try:
                        value = value.encode('utf-8')
                    except:
                        pass
                    print('* {0}: {1}'.format(key, value))
        else:
            print(self.content)

    def help(self):
        print('# {0}'.format(self.provider.title()))
        print('')
        print(self._description)
        print('Using Geocoder you can retrieve {0}\'s geocoded data from {1}.'.format(self.provider, self.api))
        print('')
        print('## Python Example')
        print('')
        print('```python')
        print('>>> import geocoder # pip install geocoder')
        if self._example:
            for line in self._example:
                print(line)
        else:
            print('>>> g = geocoder.{0}(\'<address>\')'.format(self.provider.lower()))
            print('>>> g.lat, g.lng')
            print('45.413140 -75.656703')
        print('...')
        print('```')
        print('')
        print('## Geocoder Attributes')
        print('')
        for attribute in self._attributes:
            print('* {0}'.format(attribute))
        print('')
        print('## Parameters')
        print('')
        for parameter in self._base_parameter + self._api_parameter:
            print('* {0}'.format(parameter))
        print('')

        print('## References')
        print('')
        for reference in self._base_reference + self._api_reference:
            print('* {0}'.format(reference))
        print('')

    def _json(self):
        for key in dir(self):
            if bool(not key.startswith('_') and key not in self._exclude):
                self._attributes.append(key)
                value = getattr(self, key)
                if value:
                    self.json[key] = value

    def _connect(self):
        self.content = None
        self.status_code = 404
        try:
            r = self.rate_limited_get(self.url, params=self.params, headers=self._headers, timeout=self._timeout)
            self.status_code = r.status_code
            self.url = r.url
            self.content = r.json()
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.error = 'ERROR - URL Connection'

        # Open JSON content from Request connection
        if self.status_code == 200:
            try:
                self.content = r.json()
            except:
                self.error = 'ERROR - JSON Corrupted'
                self.content = r.content

    def _parse(self, content, last=''):
        # DICTIONARY
        if isinstance(content, dict):
            for key, value in content.items():
                # NOKIA EXCEPTION
                if key == 'AdditionalData':
                    for item in value:
                        key = item.get('key')
                        value = item.get('value')
                        self.parse[key] = value

                # Only return the first result
                elif key == 'Items':
                    if value:
                        self._parse(value[0])

                # YAHOO EXCEPTION
                # Only return the first result
                elif key == 'Result':
                    if value:
                        # Value is a Dictionary
                        self._parse(value)

                # GOOGLE EXCEPTION 1 (For Reverse Geocoding)
                # Only return the first result
                elif key == 'results':
                    if value:
                        # Value is a List
                        self._parse(value[0])

                # GOOGLE EXCEPTION 2
                elif key == 'address_components':
                    for item in value:
                        short_name = item.get('short_name')
                        long_name = item.get('long_name')
                        all_types = item.get('types')
                        for types in all_types:
                            self.parse[types] = short_name
                            self.parse[types + '-long_name'] = long_name

                # GOOGLE EXCEPTION 3
                elif key == 'types':
                    self.parse['types'] = value[0]
                    for item in value:
                        name = 'types_{0}'.format(item)
                        self.parse[name] = True

                # MAXMIND EXCEPTION
                elif 'names' == key:
                    if 'en' in value:
                        name = value.get('en')
                        self.parse[last] = name

                # GEONAMES EXCEPTION
                elif 'geonames' == key:
                    self._parse(value)

                # STANDARD DICTIONARY
                elif isinstance(value, (list, dict)):
                    self._parse(value, key)
                else:
                    if last:
                        key = '{0}-{1}'.format(last, key)
                    self.parse[key] = value

        # LIST
        elif isinstance(content, list):
            if len(content) == 1:
                self._parse(content[0], last)
            elif len(content) > 1:
                for num, value in enumerate(content):

                    # BING EXCEPTION
                    if last not in ['geocodePoints']:
                        key = '{0}-{1}'.format(last, num)
                    else:
                        key = last
                    if isinstance(value, (list, dict)):
                        self._parse(value, key)
                    else:
                        self.parse[key] = value

        # STRING
        else:
            self.parse[last] = content

    @property
    def status(self):
        if self.ok:
            return 'OK'
        elif self._error:
            return self._error
        elif self.status_code == 404:
            return 'ERROR - URL Connection'
        elif not self.address:
            return 'ERROR - No results found'
        elif not bool(self.lng and self.lat):
            return 'ERROR - No Geometry'

    def _get_json_str(self, item):
        result = self.parse.get(item)
        try:
            return result.encode('utf-8')
        except:
            return str('')

    def _get_json_float(self, item):
        result = self.parse.get(item)
        try:
            return float(result)
        except:
            return 0.0

    def _get_json_int(self, item):
        result = self.parse.get(item)
        try:
            return int(result)
        except:
            return 0

    def _get_bbox(self, south, west, north, east):
        # South Latitude, West Longitude, North Latitude, East Longitude
        self.south = south
        self.west = west
        self.north = north
        self.east = east

        # Bounding Box Corners
        self.northeast = [north, east]
        self.northwest = [north, west]
        self.southwest = [south, west]
        self.southeast = [south, east]

        if bool(south and east and north and west):
            bbox = dict()
            bbox['northeast'] = [north, east]
            bbox['southwest'] = [south, west]
            return bbox
        return str('')

    @property
    def ok(self):
        if bool(self.lng and self.lat):
            return True
        else:
            return False

    @property
    def geometry(self):
        if self.ok:
            geometry = dict()
            geometry['type'] = 'Point'
            geometry['coordinates'] = [self.lng, self.lat]
            return geometry
        return dict()

    @property
    def wkt(self):
        if self.ok:
            return 'POINT({x} {y})'.format(x=self.x, y=self.y)
        return '' 

    @property
    def latlng(self):
        return [self.lat, self.lng]

    @property
    def y(self):
        return self.lat

    @property
    def x(self):
        return self.lng

    @property
    def locality(self):
        return self.city

    @property
    def province(self):
        return self.state

    @property
    def street_number(self):
        return self.housenumber
