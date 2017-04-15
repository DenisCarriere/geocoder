#!/usr/bin/python
# coding: utf8

import geocoder

address = 'The Happy Goat, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_google():
    g = geocoder.google(location, client=None)
    assert g.ok
    assert str(g.city) == city


def test_google_reverse():
    g = geocoder.google(ottawa, method='reverse')
    assert g.ok


def test_google_for_work():
    g = geocoder.google(location)
    assert g.ok
    assert str(g.city) == city


# def test_google_places():
#     g = geocoder.google(address, method='places')
#     assert g.ok


def test_google_timezone():
    g = geocoder.google(ottawa, method='timezone')
    assert g.ok


# def test_google_elevation():
#     g = geocoder.google(ottawa, method='elevation')
#     assert g.ok
