# -*- coding: utf-8 -*-

import re


class Base(object):
    """ Template for Source """
    json = dict()
    x = 0.0
    y = 0.0
    west = ''
    north = ''
    south = ''
    east = ''
    northeast = ''
    southwest = ''
    proxies = {}

    def __repr__(self):
        return "<{0} [{1}]>".format(self.name, self.location)

    def load(self, json, last=''):
        # DICTIONARY
        if isinstance(json,dict):
            for keys, values in json.items():
                # MAXMIND
                if 'geoname_id' in json:
                    names = json.get('names')
                    self.json[last] = names['en']

                # GOOGLE
                if keys == 'results':
                    if values:
                        self.load(values[0], keys)

                elif keys == 'address_components':
                    for item in values:
                        long_name = item.get('long_name')
                        all_types = item.get('types')
                        for types in all_types:
                            self.json[types] = long_name
                elif keys == 'types':
                    for item in values:
                        name = 'types_{0}'.format(item)
                        self.json[name] = True

                # LIST
                elif isinstance(values, list):
                    if len(values) == 1:
                        self.load(values[0], keys)
                    elif len(values) > 1:
                        for count, value in enumerate(values):
                            name = '{0}-{1}'.format(keys, count)
                            self.load(value, name)

                # DICTIONARY
                elif isinstance(values, dict):
                    self.load(values, keys)
                else:
                    if last:
                        name = '{0}-{1}'.format(last, keys)
                    else:
                        name = keys
                    self.json[name] = values
        # LIST
        elif isinstance(json,list):
            if json:
                self.load(json[0], last)
        # OTHER Formats
        else:
            self.json[last] = json

    def safe_postal(self, item):
        pattern = re.compile(r"[A-Z]{1}[0-9]{1}[A-Z]{1}[ ]?[0-9]{1}[A-Z]{1}[0-9]{1}([A-Z]{1}[0-9]{1}[A-Z]{1})?")
        if item:
            match = pattern.search(item)

            # Canada Pattern
            if match:
                return match.group()
            else:
                # United States Pattern
                pattern = re.compile(r'[0-9]{5}([0-9]{4})?')
                match = pattern.search(item)
                if match:
                    return match.group()
        return ''

    def safe_format(self, item):
        item = self.json.get(item)
        if item:
            return item

    def safe_coord(self, item):
        item = self.json.get(item)
        if item:
            try:
                return float(item)
            except:
                return 0.0
        else:
            return 0.0

    def safe_bbox(self, southwest, northeast):
        # South Latitude, West Longitude, North Latitude, East Longitude
        if bool(southwest and northeast):
            if isinstance(southwest[0], float):
                self.south = float(southwest[0])
                self.west = float(southwest[1])
                self.north = float(northeast[0])
                self.east = float(northeast[1])
                self.southwest = {'lat': self.south, 'lng': self.west}
                self.northeast = {'lat': self.north, 'lng': self.east}
                bbox = {'southwest': self.southwest, 'northeast': self.northeast}
                return bbox
        return ''

    def ok(self):
        return bool(self.lng() and self.lat())

    def status(self):
        if self.lng():
            return 'OK'
        else:
            return 'ERROR - No Geometry'

    def bbox(self):
        return ''

    def quality(self):
        return ''

    def postal(self):
        return ''

    def url(self):
        return self.url
