#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
ottawa = (45.4215296, -75.6971930)


def test_here():
    g = geocoder.here(location)
    assert g.ok


def test_here_reverse():
    g = geocoder.here(ottawa, method='reverse')
    assert g.ok
