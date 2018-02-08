#!/usr/bin/python
# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)

winnetka = 'Winnetka'
winnetka_bbox = [-118.604794,34.172684,-118.500938,34.236144]


def test_mapbox():
    g = geocoder.mapbox(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 2
    assert fields_count >= 11


def test_mapbox_with_proximity():
    g = geocoder.mapbox(location, proximity=ottawa)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 2
    assert fields_count >= 11


def test_mapbox_with_bbox():
    g = geocoder.mapbox(winnetka, bbox=winnetka_bbox)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 2
    assert fields_count >= 11

    for result in g:
        assert (result.lng >= winnetka_bbox[0]) and (result.lng <= winnetka_bbox[2])
        assert (result.lat >= winnetka_bbox[1]) and (result.lat <= winnetka_bbox[3])


def test_mapbox_reverse():
    g = geocoder.mapbox(ottawa, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.mapbox(location)
    assert len(g) == 5
