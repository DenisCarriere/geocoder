# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_bing():
    g = geocoder.bing(location)
    assert g.ok
    assert g.city == city
    osm_count, fields_count = g.debug()[0]
    assert osm_count == 3
    assert fields_count == 12


def test_bing_reverse():
    g = geocoder.bing(ottawa, method='reverse')
    assert g.ok
    assert g.city == city


def test_multi_results():
    g = geocoder.bing(location, maxRows=3)
    assert len(g) == 3
    assert g.city == city

    expected_results = [
        [45.4217796325684, -75.6911926269531],
        [45.2931327819824, -75.7756805419922],
        [36.9871711730957, -94.7606735229492],
    ]
    assert [result.latlng for result in g] == expected_results
