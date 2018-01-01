#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import, print_function
from builtins import str

import requests
import sys
import json
import six
import logging
from io import StringIO
from collections import OrderedDict

is_python2 = sys.version_info < (3, 0)

if is_python2:
    # python 2.7
    from urlparse import urlparse

    class MutableSequence(object):
        def index(self, v, **kwargs): return self._list.index(v, **kwargs) # noqa
        def count(self, v): return self._list.count(v) # noqa
        def pop(self, i=-1): return self._list.pop(i) # noqa
        def remove(self, v): self._list.remove(v) # noqa
        def __iter__(self): return iter(self._list) # noqa
        def __contains__(self, v): return self._list.__contains__(v) # noqa
        def __eq__(self, other): return self._list == other # noqa
else:
    # python >3.3
    from collections.abc import MutableSequence
    from urllib.parse import urlparse

from geocoder.distance import Distance # noqa

LOGGER = logging.getLogger(__name__)


class OneResult(object):
    """ Container for one (JSON) object returned by the various web services"""

    _TO_EXCLUDE = ['parse', 'json', 'url', 'fieldnames', 'help', 'debug',
                   'short_name', 'api', 'content', 'params',
                   'street_number', 'api_key', 'key', 'id', 'x', 'y',
                   'latlng', 'headers', 'timeout', 'wkt', 'locality',
                   'province', 'rate_limited_get', 'osm', 'route', 'schema',
                   'properties', 'geojson', 'tree', 'error', 'proxies', 'road',
                   'xy', 'northeast', 'northwest', 'southeast', 'southwest',
                   'road_long', 'city_long', 'state_long', 'country_long',
                   'postal_town_long', 'province_long', 'road_long',
                   'street_long', 'interpolated', 'method', 'geometry', 'session']

    def __init__(self, json_content):

        self.raw = json_content

        # attributes required to compute bbox
        self.northeast = []
        self.northwest = []
        self.southeast = []
        self.southwest = []

        # attributes returned in JSON format
        self.fieldnames = []
        self.json = {}
        self._parse_json_with_fieldnames()

    # Essential attributes for Quality Control
    @property                        # noqa
    def lat(self): return ''         # noqa

    @property                        # noqa
    def lng(self): return ''         # noqa

    @property                        # noqa
    def accuracy(self): return ''    # noqa

    @property                        # noqa
    def quality(self): return ''     # noqa

    # Bounding Box attributes
    @property                        # noqa
    def bbox(self): return {}        # noqa

    # Essential attributes for Street Address
    @property                        # noqa
    def address(self): return ''     # noqa

    @property                        # noqa
    def housenumber(self): return ''  # noqa

    @property                        # noqa
    def street(self): return ''      # noqa

    @property                        # noqa
    def city(self): return ''        # noqa

    @property                        # noqa
    def state(self): return ''       # noqa

    @property                        # noqa
    def country(self): return ''     # noqa

    @property                        # noqa
    def postal(self): return ''      # noqa

    def __repr__(self):
        """ Display [address] if available; [lat,lng] otherwise"""
        if self.address:
            return u'[{0}]'.format(six.text_type(self.address))
        else:
            return u'[{0},{1}]'.format(self.lat, self.lng)

    def _parse_json_with_fieldnames(self):
        """ Parse the raw JSON with all attributes/methods defined in the class, except for the
            ones defined starting with '_' or flagged in cls._TO_EXCLUDE.

            The final result is stored in self.json
        """
        for key in dir(self):
            if not key.startswith('_') and key not in self._TO_EXCLUDE:
                self.fieldnames.append(key)
                value = getattr(self, key)
                if value:
                    self.json[key] = value
        # Add OK attribute even if value is "False"
        self.json['ok'] = self.ok

    @property
    def ok(self):
        return bool(self.lng and self.lat)

    @property
    def status(self):
        if self.ok:
            return 'OK'
        if not self.address:
            return 'ERROR - No results found'
        return 'ERROR - No Geometry'

    def debug(self, verbose=True):
        with StringIO() as output:
            print(u'\n', file=output)
            print(u'From provider\n', file=output)
            print(u'-----------\n', file=output)
            print(str(json.dumps(self.raw, indent=4)), file=output)
            print(u'\n', file=output)
            print(u'Cleaned json\n', file=output)
            print(u'-----------\n', file=output)
            print(str(json.dumps(self.json, indent=4)), file=output)
            print(u'\n', file=output)
            print(u'OSM Quality\n', file=output)
            print(u'-----------\n', file=output)
            osm_count = 0
            for key in self.osm:
                if 'addr:' in key:
                    if self.json.get(key.replace('addr:', '')):
                        print(u'- [x] {0}\n'.format(key), file=output)
                        osm_count += 1
                    else:
                        print(u'- [ ] {0}\n'.format(key), file=output)
            print(u'({0}/{1})\n'.format(osm_count, len(self.osm) - 2), file=output)
            print(u'\n', file=output)
            print(u'Fieldnames\n', file=output)
            print(u'----------\n', file=output)
            fields_count = 0
            for fieldname in self.fieldnames:
                if self.json.get(fieldname):
                    print(u'- [x] {0}\n'.format(fieldname), file=output)
                    fields_count += 1
                else:
                    print(u'- [ ] {0}\n'.format(fieldname), file=output)
            print(u'({0}/{1})\n'.format(fields_count, len(self.fieldnames)), file=output)

            # print in verbose mode
            if verbose:
                print(output.getvalue())

            # return stats
            return [osm_count, fields_count]

    def _get_bbox(self, south, west, north, east):
        if all([south, east, north, west]):
            # South Latitude, West Longitude, North Latitude, East Longitude
            self.south = float(south)
            self.west = float(west)
            self.north = float(north)
            self.east = float(east)

            # Bounding Box Corners
            self.northeast = [self.north, self.east]
            self.northwest = [self.north, self.west]
            self.southwest = [self.south, self.west]
            self.southeast = [self.south, self.east]

            # GeoJSON bbox
            self.westsouth = [self.west, self.south]
            self.eastnorth = [self.east, self.north]

            return dict(northeast=self.northeast, southwest=self.southwest)
        return {}

    @property
    def confidence(self):
        if self.bbox:
            # Units are measured in Kilometers
            distance = Distance(self.northeast, self.southwest, units='km')
            for score, maximum in [(10, 0.25),
                                   (9, 0.5),
                                   (8, 1),
                                   (7, 5),
                                   (6, 7.5),
                                   (5, 10),
                                   (4, 15),
                                   (3, 20),
                                   (2, 25)]:
                if distance < maximum:
                    return score
                if distance >= 25:
                    return 1
        # Cannot determine score
        return 0

    @property
    def geometry(self):
        if self.ok:
            return {
                'type': 'Point',
                'coordinates': [self.x, self.y]}
        return {}

    @property
    def osm(self):
        osm = dict()
        if self.ok:
            osm['x'] = self.x
            osm['y'] = self.y
            if self.housenumber:
                osm['addr:housenumber'] = self.housenumber
            if self.road:
                osm['addr:street'] = self.road
            if self.city:
                osm['addr:city'] = self.city
            if self.state:
                osm['addr:state'] = self.state
            if self.country:
                osm['addr:country'] = self.country
            if self.postal:
                osm['addr:postal'] = self.postal
            if hasattr(self, 'population'):
                if self.population:
                    osm['population'] = self.population
        return osm

    @property
    def geojson(self):
        feature = {
            'type': 'Feature',
            'properties': self.json,
        }
        if self.bbox:
            feature['bbox'] = [self.west, self.south, self.east, self.north]
            feature['properties']['bbox'] = feature['bbox']
        if self.geometry:
            feature['geometry'] = self.geometry
        return feature

    @property
    def wkt(self):
        if self.ok:
            return 'POINT({x} {y})'.format(x=self.x, y=self.y)
        return ''

    @property
    def xy(self):
        if self.ok:
            return [self.lng, self.lat]
        return []

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
    def road(self):
        return self.street

    @property
    def route(self):
        return self.street


class MultipleResultsQuery(MutableSequence):
    """ Will replace the Base class to support multiple results, with the following differences :

        - split class into 2 parts :
            - OneResult to actually store a (JSON) object from provider
            - MultipleResultsQuery to manage the query

        - class variables moved into instance
        - remaining class variables are names with convention: _CAPITALS
        - self.url derived from class var cls.URL, which must be a valid URL
        - self.timeout has default value from class var cls.TIMEOUT
    """

    _URL = None
    _RESULT_CLASS = None
    _KEY = None
    _KEY_MANDATORY = True
    _TIMEOUT = 5.0

    @staticmethod
    def _is_valid_url(url):
        """ Helper function to validate that URLs are well formed, i.e that it contains a valid
            protocol and a valid domain. It does not actually check if the URL exists
        """
        try:
            parsed = urlparse(url)
            mandatory_parts = [parsed.scheme, parsed.netloc]
            return all(mandatory_parts)
        except:
            return False

    @classmethod
    def _is_valid_result_class(cls):
        return issubclass(cls._RESULT_CLASS, OneResult)

    @classmethod
    def _get_api_key(cls, key=None):
        # Retrieves API Key from method argument first, then from Environment variables
        key = key or cls._KEY

        # raise exception if not valid key found
        if not key and cls._KEY_MANDATORY:
            raise ValueError('Provide API Key')

        return key

    def __init__(self, location, **kwargs):
        super(MultipleResultsQuery, self).__init__()
        self._list = []

        # check validity of _URL
        if not self._is_valid_url(self._URL):
            raise ValueError("Subclass must define a valid URL. Got %s", self._URL)
        # override with kwargs IF given AND not empty string
        self.url = kwargs.get('url', self._URL) or self._URL
        # double check url, just in case it has been overwritten by kwargs
        if not self._is_valid_url(self.url):
            raise ValueError("url not valid. Got %s", self.url)

        # check validity of Result class
        if not self._is_valid_result_class():
            raise ValueError(
                "Subclass must define _RESULT_CLASS from 'OneResult'. Got %s", self._RESULT_CLASS)
        self.one_result = self._RESULT_CLASS

        # check validity of provider key
        provider_key = self._get_api_key(kwargs.pop('key', ''))

        # point to geocode, as a string or coordinates
        self.location = location

        # set attributes to manage query
        self.encoding = kwargs.get('encoding', 'utf-8')
        self.timeout = kwargs.get('timeout', self._TIMEOUT)
        self.proxies = kwargs.get('proxies', '')
        self.session = kwargs.get('session', requests.Session())
        # headers can be overriden in _build_headers
        self.headers = self._build_headers(provider_key, **kwargs).copy()
        self.headers.update(kwargs.get('headers', {}))
        # params can be overriden in _build_params
        # it is an OrderedDict in order to preserve the order of the url query parameters
        self.params = OrderedDict(self._build_params(location, provider_key, **kwargs))
        self.params.update(kwargs.get('params', {}))

        # results of query (set by _connect)
        self.status_code = None
        self.response = None
        self.error = False

        # pointer to result where to delegates calls
        self.current_result = None

        # hook for children class to finalize their setup before the query
        self._before_initialize(location, **kwargs)

        # query and parse results
        self._initialize()

    def __getitem__(self, key):
        return self._list[key]

    def __setitem__(self, key, value):
        self._list[key] = value

    def __delitem__(self, key):
        del self._list[key]

    def __len__(self):
        return len(self._list)

    def insert(self, index, value):
        self._list.insert(index, value)

    def add(self, value):
        self._list.append(value)

    def __repr__(self):
        base_repr = u'<[{0}] {1} - {2} {{0}}>'.format(
            self.status,
            self.provider.title(),
            self.method.title()
        )
        if len(self) == 0:
            return base_repr.format(u'[empty]')
        elif len(self) == 1:
            return base_repr.format(repr(self[0]))
        else:
            return base_repr.format(u'#%s results' % len(self))

    def _build_headers(self, provider_key, **kwargs):
        """Will be overridden according to the targetted web service"""
        return {}

    def _build_params(self, location, provider_key, **kwargs):
        """Will be overridden according to the targetted web service"""
        return {}

    def _before_initialize(self, location, **kwargs):
        """Can be overridden to finalize setup before the query"""
        pass

    def _initialize(self):
        # query URL and get valid JSON (also stored in self.json)
        json_response = self._connect()

        # catch errors
        has_error = self._catch_errors(
            json_response) if json_response else True

        # creates instances for results
        if not has_error:
            self._parse_results(json_response)

    def _connect(self):
        """ - Query self.url (validated cls._URL)
            - Analyse reponse and set status, errors accordingly
            - On success:

                 returns the content of the response as a JSON object
                 This object will be passed to self._parse_json_response
        """
        self.status_code = 'Unknown'

        try:
            # make request and get response
            self.response = response = self.rate_limited_get(
                self.url,
                params=self.params,
                headers=self.headers,
                timeout=self.timeout,
                proxies=self.proxies
            )

            # check that response is ok
            self.status_code = response.status_code
            response.raise_for_status()

            # rely on json method to get non-empty well formatted JSON
            json_response = response.json()
            self.url = response.url
            LOGGER.info("Requested %s", self.url)

        except requests.exceptions.RequestException as err:
            # store real status code and error
            self.error = u'ERROR - {}'.format(str(err))
            LOGGER.error("Status code %s from %s: %s",
                         self.status_code, self.url, self.error)

            # return False
            return False

        # return response within its JSON format
        return json_response

    def rate_limited_get(self, url, **kwargs):
        """ By default, simply wraps a session.get request"""
        return self.session.get(url, **kwargs)

    def _adapt_results(self, json_response):
        """ Allow children classes to format json_response into an array of objects
            OVERRIDE TO FETCH the correct array of objects when necessary
        """
        return json_response

    def _parse_results(self, json_response):
        """ Creates instances of self.one_result (validated cls._RESULT_CLASS)
            from JSON results retrieved by self._connect

            params: array of objects (dictionnaries)
        """
        for json_dict in self._adapt_results(json_response):
            self.add(self.one_result(json_dict))

        # set default result to use for delegation
        self.current_result = len(self) > 0 and self[0]

    def _catch_errors(self, json_response):
        """ Checks the JSON returned from the provider and flag errors if necessary"""
        return self.error

    @property
    def ok(self):
        return len(self) > 0

    @property
    def status(self):
        if self.ok:
            return 'OK'
        elif self.error:
            return self.error
        elif len(self) == 0:
            return 'ERROR - No results found'
        else:
            return 'ERROR - Unhandled Exception'

    @property
    def geojson(self):
        geojson_results = [result.geojson for result in self]
        features = {
            'type': 'FeatureCollection',
            'features': geojson_results
        }
        return features

    def debug(self, verbose=True):
        with StringIO() as output:
            print(u'===\n', file=output)
            print(str(repr(self)), file=output)
            print(u'===\n', file=output)
            print(u'\n', file=output)
            print(u'#res: {}\n'.format(len(self)), file=output)
            print(u'code: {}\n'.format(self.status_code), file=output)
            print(u'url:  {}\n'.format(self.url), file=output)

            stats = []

            if self.ok:
                for index, result in enumerate(self):
                    print(u'\n', file=output)
                    print(u'Details for result #{}\n'.format(index + 1), file=output)
                    print(u'---\n', file=output)
                    stats.append(result.debug())
            else:
                print(self.status, file=output)

            if verbose:
                print(output.getvalue())

            return stats

    # Delegation to current result
    def set_default_result(self, index):
        """ change the result used to delegate the calls to. The provided index should be in the
            range of results, otherwise it will raise an exception
        """
        self.current_result = self[index]

    def __getattr__(self, name):
        """ Called when an attribute lookup has not found the attribute in the usual places (i.e.
            it is not an instance attribute nor is it found in the class tree for self). name is
            the attribute name. This method should return the (computed) attribute value or raise
            an AttributeError exception.

            Note that if the attribute is found through the normal mechanism, __getattr__() is not called.
        """
        if not self.ok:
            return None

        if self.current_result is None:
            raise AttributeError("%s not found on %s, and current_result is None".format(
                name, self.__class__.__name__
            ))
        return getattr(self.current_result, name)
