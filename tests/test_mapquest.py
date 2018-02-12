#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa'
city = 'Ottawa'
ottawa = (45.50, -76.05)

winnetka = 'Winnetka'
winnetka_bbox = [-118.604794,34.172684,-118.500938,34.236144]


def test_mapquest():
    g = geocoder.mapquest(location, timeout=10)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 10


def test_mapquest_with_bbox():
    g = geocoder.mapquest(winnetka, bbox=winnetka_bbox)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 2
    assert fields_count >= 11

    for result in g:
        assert (result.lng >= winnetka_bbox[0]) and (result.lng <= winnetka_bbox[2])
        assert (result.lat >= winnetka_bbox[1]) and (result.lat <= winnetka_bbox[3])

def test_mapquest_reverse():
    g = geocoder.mapquest(ottawa, method='reverse', timeout=10)
    assert g.ok


def test_multi_results():
    g = geocoder.mapquest(location, maxRows=3, timeout=10)
    assert len(g) == 3
