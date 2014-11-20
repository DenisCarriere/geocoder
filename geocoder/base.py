#!/usr/bin/python
# coding: utf8

from __future__ import print_function
import requests
import sys


class Base(object):
    _exclude = ['parse', 'json', 'url', 'attributes', 'help', 'debug', 'short_name',
                'api', 'content', 'params', 'status_code', 'street_number', 'method',
                'api_key', 'ok', 'key', 'id', 'x', 'y', 'latlng', 'headers', 'timeout',
                'bbox', 'geometry', 'wkt','locality', 'province','rate_limited_get']
    _error = None
    _attributes = []

    def __repr__(self):
        return "<[{0}] {1} - {2} [{3}]>".format(self.status, self.provider, self.method, self.address)
    
    @staticmethod
    def rate_limited_get(url, **kwargs):
        return requests.get(url, **kwargs)

    def _connect(self, **kwargs):
        self.status_code = None
        self.params = kwargs.get('url', '')
        self.params = kwargs.get('params', {})
        self.headers = kwargs.get('headers', {})
        self.timeout = kwargs.get('timeout', 5.0)
        self.proxies = kwargs.get('proxies', '')

        # Connect to URL
        try:
            r = self.rate_limited_get(
                self.url, 
                params=self.params, 
                headers=self.headers, 
                timeout=self.timeout,
                proxies=self.proxies
            )
            self.status_code = r.status_code
            self.url = r.url
        except KeyboardInterrupt:
            sys.exit()
        except:
            self.status_code = 404
            self.error = 'ERROR - URL Connection'

        # Open JSON content from Request connection
        if self.status_code == 200:
            try:
                self.content = r.json()
            except:
                self.status_code = 400
                self.error = 'ERROR - JSON Corrupted'
                self.content = r.content

    def debug(self):
        print('# Debug')
        print('## Connection')
        print('* URL: [{0}]({1})'.format(self.provider.title(), self.url))
        print('* Status: {0}'.format(self.status))
        print('* Status Code: {0}'.format(self.status_code))
        for key, value in self.params.items():
            print('* Parameter [{0}]: {1}'.format(key, value))
        for key, value in self.headers.items():
            print('* Headers [{0}]: {1}'.format(key, value))
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

    def _json(self):
        for key in dir(self):
            if bool(not key.startswith('_') and key not in self._exclude):
                self._attributes.append(key)
                value = getattr(self, key)
                if value:
                    self.json[key] = value



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
        geometry = dict()
        if self.ok:
            geometry['type'] = 'Point'
            geometry['coordinates'] = [self.lng, self.lat]
        return geometry

    @property
    def osm(self):
        osm = dict()
        if self.ok:
            osm['addr:housenumber'] = self.housenumber
            osm['addr:street'] = self.street
            osm['addr:city'] = self.city
            osm['addr:country'] = self.country
            osm['addr:postal'] = self.postal
        return osm

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

    @property
    def route(self):
        return self.street
