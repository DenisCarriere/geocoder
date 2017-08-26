#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

from geocoder.w3w import W3WResult, W3WQuery


class W3WReverseResult(W3WResult):

    @property
    def ok(self):
        return bool(self.words)


class W3WReverse(W3WQuery):
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

    _URL = 'https://api.what3words.com/v2/reverse'
    _RESULT_CLASS = W3WReverseResult

    def _build_params(self, location, provider_key, **kwargs):
        return {
            'coords': location,
            'key': provider_key,
        }


if __name__ == '__main__':
    g = W3WReverse([45.15, -75.14])
    g.debug()
