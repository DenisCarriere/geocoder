#!/usr/bin/python
# coding: utf8

import geocoder

import requests_mock

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)
place = 'rail station, Ottawa'


def test_google():
    urls = [
        # when testing locally
        'https://maps.googleapis.com/maps/api/geocode/json?language=&address=Ottawa,%20Ontario&bounds=&components=&region=&key=mock',
        # when building in Travis (secured connection implies ordered parameters)
        'https://maps.googleapis.com/maps/api/geocode/json?client=[secure]&latlng=45.4215296%2C+-75.697193&sensor=false&signature=iXbq6odmrYN0XgcfB5EPcgEvR-I%3D'
    ]
    data_file = 'tests/results/google.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        for url in urls:
            mocker.get(url, text=input.read())
        g = geocoder.google(location, client=None, key='mock')
        assert g.ok
        assert g.accuracy == 'APPROXIMATE'
        assert str(g.city) == city
        osm_count, fields_count = g.debug()[0]
        assert osm_count >= 3
        assert fields_count >= 15


def test_issue_294():
    g = geocoder.google("Cerro Torre Mountain")
    assert g.ok


def test_google_reverse():
    g = geocoder.google(ottawa, method='reverse')
    assert g.ok
    assert len(g) >= 10


def test_google_places():
    g = geocoder.google(place, method='places')
    assert g.ok
    assert g.address == '200 Tremblay Rd, Ottawa, ON K1G 3H5, Canada'


def test_google_timezone():
    url = 'https://maps.googleapis.com/maps/api/timezone/json?location=45.4215296%2C+-75.697193&timestamp=1500000000'
    data_file = 'tests/results/google_timezone.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.google(ottawa, method='timezone', timestamp=1500000000)
        assert g.ok


def test_google_elevation():
    url = 'https://maps.googleapis.com/maps/api/elevation/json?locations=45.4215296%2C+-75.697193'
    data_file = 'tests/results/google_elevation.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.google(ottawa, method='elevation')
        assert g.ok
