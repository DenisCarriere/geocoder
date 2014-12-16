#!/usr/bin/python
# coding: utf8

import requests
import sys
import re


class Base(object):
    _exclude = ['parse', 'json', 'url', 'attributes', 'help', 'debug', 'short_name',
                'api', 'content', 'params', 'status_code', 'street_number', 'method',
                'api_key', 'ok', 'key', 'id', 'x', 'y', 'latlng', 'headers', 'timeout',
                'geometry', 'wkt','locality', 'province','rate_limited_get', 'osm',
                'route', 'properties','geojson',]
    _attributes = []
    error = None
    status_code = None
    headers = {}
    params = {}
    housenumber = ''
    address = ''
    lat = ''
    lng = ''
    street = ''
    city = ''
    state = ''
    postal = ''
    country = ''
    population = ''

    def __repr__(self):
        return "<[{0}] {1} - {2} [{3}]>".format(
            self.status, 
            self.provider.title(), 
            self.method.title(), 
            self.address
        )
    
    @staticmethod
    def rate_limited_get(url, **kwargs):
        return requests.get(url, **kwargs)

    def _connect(self, **kwargs):
        self.status_code = 'Unknown'
        self.timeout = kwargs.get('timeout', 5.0)
        self.proxies = kwargs.get('proxies', '')
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
            self.content = r.json()
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

    def _initialize(self, **kwargs):
        self._connect(url=self.url, params=self.params, **kwargs)
        self._parse(self.content)
        self._json()
        self.bbox

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
        print('## OSM Attributes')
        for key, value in self.osm.items():
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
        elif self.error:
            return self.error
        elif self.status_code == 404:
            return 'ERROR - URL Connection'
        elif not self.address:
            return 'ERROR - No results found'
        elif not bool(self.lng and self.lat):
            return 'ERROR - No Geometry'

    def _check_ip_address(self):
        expression = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        pattern = re.compile(expression)
        match = pattern.search(self.location)
        if match:
            self.location = match.group()
            return True
        else:
            self.error = 'ERROR - IP Address Invalid'
            return False

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

        # GeoJSON bbox
        self.westsouth = [west, south]
        self.eastnorth = [east, north]
        
        if bool(south and east and north and west):
            bbox = {
                'northeast': [north, east],
                'southwest': [south, west],
            }
            return bbox
        return {}

    @property
    def bbox(self):
        return {}

    @property
    def ok(self):
        if bool(self.lng and self.lat):
            return True
        else:
            return False

    @property
    def geometry(self):
        if self.ok:
            geometry = {
                'type': 'Point',
                'coordinates': [self.lng, self.lat],
            }
            return geometry
        return {}

    @property
    def osm(self):
        osm = dict()
        if self.ok:
            osm['x'] = self.x
            osm['y'] = self.y
            if self.housenumber:
                osm['addr:housenumber'] = self.housenumber
            if self.street:
                osm['addr:street'] = self.street
            if self.city:
                osm['addr:city'] = self.city
            if self.state:
                osm['addr:state'] = self.state
            if self.country:
                osm['addr:country'] = self.country
            if self.postal:
                osm['addr:postal'] = self.postal
            if self.population:
                osm['population'] = self.population
        return osm

    @property
    def properties(self):
        properties = self.json
        if self.ok:
            del properties['lat']
            del properties['lng']
        if self.bbox:
            del properties['bbox']
        return properties

    @property
    def geojson(self):
        feature = {
            'type': 'Feature',
            'geometry': self.geometry,
            'properties': self.properties,
        }
        if self.bbox:
            feature['bbox'] = self.westsouth + self.eastnorth
        return feature

    @property
    def wkt(self):
        if self.ok:
            return 'POINT({x} {y})'.format(x=self.x, y=self.y)
        return '' 

    @property
    def latlng(self):
        if self.ok:
            return [self.lat, self.lng]
        return []

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

