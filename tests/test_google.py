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
        assert str(g.city) == city


def test_google_reverse():
    g = geocoder.google(ottawa, method='reverse')
    assert g.ok
    assert len(g) == 10

    first_three_expected_addresses = [
        '100 Albert St, Ottawa, ON K1P 1A5, Canada',
        'Queen / Metcalfe, Ottawa, ON K1P 5T8, Canada',
        'Byward Market - Parliament Hill, Ottawa, ON, Canada',
        ]
    assert [result.address for result in g][:3] == first_three_expected_addresses


def test_google_places():
    g = geocoder.google(place, method='places')
    assert g.ok

    expected_addresses = [
        '200 Tremblay Rd, Ottawa, ON K1G 3H5, Canada',
        '3347 Fallowfield Rd, Barrhaven, ON K2J 5K9, Canada'
    ]
    assert [result.address for result in g] == expected_addresses


def test_google_timezone():
    g = geocoder.google(ottawa, method='timezone')
    assert g.ok


def test_google_elevation():
    g = geocoder.google(ottawa, method='elevation')
    assert g.ok
