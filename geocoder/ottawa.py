#!/usr/bin/python
# coding: utf8

from .base import Base


class Ottawa(Base):
    """
    Ottawa ArcGIS REST Services
    ===========================
    Geocoding is the process of assigning a location, usually in the form of coordinate
    values (points), to an address by comparing the descriptive location elements in the
    address to those present in the reference material. Addresses come in many forms,
    ranging from the common address format of a house number followed by the street name
    and succeeding information to other location descriptions such as postal zone
    or census tract. An address includes any type of information that distinguishes a place. 

    API Reference
    -------------
    http://maps.ottawa.ca/ArcGIS/rest/services/compositeLocator/GeocodeServer/findAddressCandidates

    OSM Quality (0/6)
    -----------------
    [ ] addr:housenumber
    [ ] addr:street
    [ ] addr:city
    [ ] addr:state
    [ ] addr:country
    [ ] addr:postal
    """
    provider = 'ottawa'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'http://maps.ottawa.ca/ArcGIS/rest/services/'
        self.url += 'compositeLocator/GeocodeServer/findAddressCandidates'
        self.location = location
        self.json = dict()
        self.parse = dict()
        self.content = None
        self.params = {
            'SingleLine': location.replace(', Ottawa, ON',''),
            'f': 'json',
            'outSR': 4326,
        } 
        self._initialize(**kwargs)

    @property
    def lat(self):
        return self._get_json_float('location-y')

    @property
    def lng(self):
        return self._get_json_float('location-x')

    @property
    def address(self):
        return self._get_json_str('address')

    @property
    def housenumber(self):
        return ''

    @property
    def street(self):
        return ''

    @property
    def city(self):
        return ''

    @property
    def state(self):
        return ''

    @property
    def country(self):
        return ''

    @property
    def quality(self):
        return ''

    @property
    def accuracy(self):
        return self._get_json_int('score')

    @property
    def postal(self):
        return ''

if __name__ == '__main__':
    g = Ottawa('1552 Payette dr.')
    g.debug()