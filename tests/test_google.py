#!/usr/bin/python
# coding: utf8

import geocoder

import requests_mock

address = 'The Happy Goat, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_google():
    url = 'https://maps.googleapis.com/maps/api/geocode/json?language=&address=Ottawa,%20Ontario&bounds=&components=&region=&key=mock'
    data_file = 'tests/results/google.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.google(location, client=None, key='mock')
        assert g.ok
        assert str(g.city) == city


def test_google_reverse():
    url = 'https://maps.googleapis.com/maps/api/geocode/json?language=&latlng=45.4215296%2C+-75.697193&sensor=false&key=mock'
    data_file = 'tests/results/google_reverse.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.google(ottawa, method='reverse', key='mock')
        assert g.ok


def test_google_for_work():
    # FIXME from ebreton: what difference with test_google() ?
    url = 'https://maps.googleapis.com/maps/api/geocode/json?language=&address=Ottawa%2C+Ontario&bounds=&components=&region=&key=mock'
    data_file = 'tests/results/google.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.google(location, key='mock')
        assert g.ok
        assert str(g.city) == city


# def test_google_places():
#     g = geocoder.google(address, method='places')
#     assert g.ok


def test_google_timezone():
    url = 'https://maps.googleapis.com/maps/api/timezone/json?location=45.4215296%2C+-75.697193&timestamp=1501571979.087397'
    data_file = 'tests/results/google_timezone.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.google(ottawa, method='timezone', timestamp=1501571979.087397)
        assert g.ok


# def test_google_elevation():
#     g = geocoder.google(ottawa, method='elevation')
#     assert g.ok
