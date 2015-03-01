#!/usr/bin/python
# coding: utf8

from .base import Base
from .keys import w3w_key
from .w3w import W3W
from .location import Location


class W3WReverse(W3W, Base):
    """
    what3words
    ==========
    what3words is a global grid of 57 trillion 3mx3m squares.
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
    method = 'reverse'

    def __init__(self, location, **kwargs):
        self.url = 'http://api.what3words.com/position'
        location = Location(location)
        self.location = location.latlng
        self.params = {
            'position': self.location,
            'key': kwargs.get('key', w3w_key),
        }
        self._initialize(**kwargs)

    @property
    def ok(self):
        return bool(self.words)

if __name__ == '__main__':
    g = W3WReverse([45.15, -75.14])
    g.debug()
