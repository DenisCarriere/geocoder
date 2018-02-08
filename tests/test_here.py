#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
ottawa = (45.4215296, -75.6971930)

winnetka = 'Winnetka'
winnetka_bbox = [-118.604794,34.172684,-118.500938,34.236144]


def test_here():
    g = geocoder.here(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 4
    assert fields_count >= 13


def test_here_with_bbox():
    g = geocoder.here(winnetka, bbox=winnetka_bbox)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 2
    assert fields_count >= 11

    for result in g:
        assert (result.lng >= winnetka_bbox[0]) and (result.lng <= winnetka_bbox[2])
        assert (result.lat >= winnetka_bbox[1]) and (result.lat <= winnetka_bbox[3])


def test_here_reverse():
    g = geocoder.here(ottawa, method='reverse')
    assert g.ok
