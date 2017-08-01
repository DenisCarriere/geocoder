#!/usr/bin/env python
# coding: utf8

import subprocess

import requests_mock


location = 'Ottawa, Ontario'


def test_cli_google():
    url = 'https://maps.googleapis.com/maps/api/geocode/json?language=&address=Ottawa,%20Ontario&bounds=&components=&region=&key=mock'
    data_file = 'tests/results/google.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        assert not subprocess.call(['geocode', location, '--provider', 'google', '--key', 'mock'])


def test_cli_osm():
    url = 'https://nominatim.openstreetmap.org/search?q=Ottawa%2C+Ontario&format=jsonv2&addressdetails=1&limit=1'
    data_file = 'tests/results/osm.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        assert not subprocess.call(['geocode', location, '--provider', 'osm'])
