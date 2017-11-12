#!/usr/bin/python
# coding: utf8

import geocoder
import requests_mock

location = 'New York City'
coordinates = [45.3, -75.4]


def test_geocodefarm():
    url = 'https://www.geocode.farm/v3/json/forward/?addr=New+York+City&lang=&country=&count=1'
    data_file = 'tests/results/geocodefarm.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        result = geocoder.geocodefarm(location)
        assert result.ok
        osm_count, fields_count = result.debug()[0]
        assert osm_count >= 3
        assert fields_count >= 15


def test_geocodefarm_reverse():
    url = 'https://www.geocode.farm/v3/json/reverse/?lat=45.3&lon=-75.4&lang=&country='
    data_file = 'tests/results/geocodefarm_reverse.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        result = geocoder.geocodefarm(coordinates, method='reverse')
        assert result.ok
