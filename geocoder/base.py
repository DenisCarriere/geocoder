# -*- coding: utf-8 -*-

import re


class Base(object):
    """ Template for Source """
    json = dict()
    x = 0.0
    y = 0.0
    west = 0.0
    north = 0.0
    south = 0.0
    east = 0.0
        
    def __repr__(self):
        return "<{0} [{1}]>".format(self.name, self.location)

    def load(self, json, last=''):
        # DICTIONARY
        if type(json) == type(dict()):
            for keys, values in json.items():
                # MAXMIND
                if 'geoname_id' in json:
                    names = json.get('names')
                    self.json[last] = names['en']

                # GOOGLE
                if keys == 'address_components':
                    for item in values:
                        long_name = item.get('long_name')
                        all_types = item.get('types')
                        for types in all_types:
                            self.json[types] = long_name
                if keys == 'types':
                    for item in values:
                        name = 'types_{0}'.format(item)
                        self.json[name] = True

                # LIST
                elif type(values) == type(list()):
                    if len(values) == 1:
                        self.load(values[0], keys)
                    elif len(values) > 1:
                        count = 0
                        for value in values:
                            name = '{0}-{1}'.format(keys, count)
                            self.load(value, name)
                            count += 1
                # DICTIONARY
                elif type(values) == type(dict()):
                    self.load(values, keys)
                else:
                    if last:
                        name = last + '-' + keys
                    else:
                        name = keys
                    self.json[name] = values
        # LIST
        elif type(json) == type(list()):
            if json:
                self.load(json[0], last)
        # OTHER Formats
        else:
            self.json[last] = json

    def safe_postal(self, item):
        pattern = re.compile(r'[A-Z]{1}[0-9]{1}[A-Z]{1}[ ]?[0-9]{1}[A-Z]{1}[0-9]{1}([A-Z]{1}[0-9]{1}[A-Z]{1})?')
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
        if southwest:
            if southwest[0]:
                self.south = float(southwest[0]) 
                self.west = float(southwest[1])
                self.north = float(northeast[0])
                self.east = float(northeast[1])
                return [(self.south, self.west), (self.north, self.east)]
            else:
                return [(0.0, 0.0), (0.0, 0.0)]

    def ok(self):
        if self.lat():
            if self.lng():
                return True
            else:
                return False
        else:
            return False

    def status(self):
        if self.lng():
            return 'OK'
        else:
            return 'ERROR - No Geometry'

    def bbox(self):
        return [(0.0, 0.0), (0.0, 0.0)]

    def quality(self):
        return ''

    def postal(self):
        return ''