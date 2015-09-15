#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import w3w_key


class W3W(Base):
    """
    What3Words
    ==========
    What3Words is a global grid of 57 trillion 3mx3m squares.
    Each square has a 3 word address that can be communicated quickly,
    easily and with no ambiguity.

    Addressing the world

    Everyone and everywhere now has an address

    Params
    ------
    :param location: Your search location you want geocoded.
    :param key: W3W API key.
    :param method: Chose a method (geocode, method)

    References
    ----------
    API Reference: http://developer.what3words.com/
    Get W3W key: http://developer.what3words.com/api-register/
    """
    provider = 'w3w'
    method = 'geocode'

    def __init__(self, location, **kwargs):
        self.url = 'https://api.what3words.com/w3w'
        self.location = location
        self.params = {
            'string': location,
            'key': self._get_api_key(w3w_key, **kwargs),
        }
        self._initialize(**kwargs)

    @property
    def lat(self):
        position = self.parse['position']
        if position:
            return position[0]

    @property
    def lng(self):
        position = self.parse['position']
        if position:
            return position[1]

    @property
    def language(self):
        return self.parse.get('language')

    @property
    def type(self):
        return self.parse.get('type')

    @property
    def words(self):
        return self.parse.get('words')

if __name__ == '__main__':
    g = W3W('embedded.fizzled.trial')
    g.debug()
