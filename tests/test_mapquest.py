#!/usr/bin/python
# coding: utf8
import requests_mock
import geocoder

location = 'Ottawa'
city = 'Ottawa'
ottawa = (45.50, -76.05)
locations = ['Denver,CO', 'Boulder,CO']

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

def test_mapquest_batch():
    url = 'http://www.mapquestapi.com/geocoding/v1/batch'
    data_file = 'tests/results/mapquest_batch.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.mapquest(locations, method='batch', timeout=10)
        assert g.ok
        expected_results = [
            [39.738453, -104.984853],
            [40.015831, -105.27927]
        ]

        assert [result.latlng for result in g] == expected_results


def test_multi_results():
    g = geocoder.mapquest(location, maxRows=3, timeout=10)
    assert len(g) == 3
