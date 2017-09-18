#!/usr/bin/python
# coding: utf8
import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_osm():
    g = geocoder.osm(location)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count == 3
    assert fields_count == 21


def test_osm_reverse():
    g = geocoder.osm(ottawa, method='reverse')
    assert g.ok


def test_multi_results():
    g = geocoder.osm(location, maxRows='5')
    assert len(g) == 5

    expected_results = [
        'Ottawa, Ontario, Canada',
        'Ontario, Ottawa County, Oklahoma, United States of America',
    ]
    assert [result.address for result in g][:2] == expected_results
