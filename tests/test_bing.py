# coding: utf8

import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)
locations_forward = ['Denver,CO', 'Boulder,CO']
locations_reverse = [[40.7943, -73.970859], [48.845580, 2.321807]]

def test_bing():
    g = geocoder.bing(location)
    assert g.ok
    assert g.city == city
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 12


def test_bing_details():
    details = {
        'adminDistrict': 'Ontario',
        'locality': 'Ottawa'
    }

    g = geocoder.bing(None, method='details', **details)
    assert g.ok
    assert g.city == city
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 12

    details = {
        'addressLine': '6912 Route 8',
        'adminDistrict': 'Northumberland',
        'countryRegion': 'CA',
        'locality': 'Ludlow'
    }

    g = geocoder.bing(None, method='details', **details)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 12


def test_bing_reverse():
    g = geocoder.bing(ottawa, method='reverse')
    assert g.ok
    assert g.city == city


def test_bing_batch_forward():
    g = geocoder.bing(locations_forward, method='batch')
    assert g.ok
    assert len(g) == 2
    expected_results = [
        [39.7400093078613, -104.99201965332],
        [40.015739440918, -105.279243469238]
    ]

    assert [result.latlng for result in g] == expected_results


def test_bing_batch_reverse():
    g = geocoder.bing(locations_reverse, method='batch_reverse')
    assert g.ok
    assert len(g) == 2
    assert [result.city for result in g] == ['New York', 'Paris']


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
