#!/usr/bin/python
# coding: utf8

import geocoder
import requests_mock

us_address = '595 Market St'
us_city = 'San Francisco'
us_state = 'CA'
us_zipcode = '94105'
us_locations = ['4650 Silver Hill Road, Suitland, MD 20746', '42 Chapel Street, New Haven']

def test_uscensus():
    url = 'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address=595+Market+St+San+Francisco+CA+94105&benchmark=4&format=json'
    data_file = 'tests/results/uscensus.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.uscensus(' '.join([us_address, us_city, us_state, us_zipcode]), timeout=10)
        assert g.ok


def test_uscensus_reverse():
    url = 'https://geocoding.geo.census.gov/geocoder/geographies/coordinates?x=-77.016389&y=38.904722&benchmark=4&vintage=4&format=json'
    data_file = 'tests/results/uscensus_reverse.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.uscensus((38.904722, -77.016389), method='reverse', timeout=10)
        assert g.ok


def test_uscensus_reverse():
    url = 'https://geocoding.geo.census.gov/geocoder/locations/addressbatch'
    data_file = 'tests/results/uscensus_batch.csv'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.post(url, text=input.read())
        g = geocoder.uscensus(us_locations, benchmark=9, method='batch')
        assert g.ok
        expected_results = [
            [38.846638, -76.92681],
            [41.30435, -72.89422]
        ]

        assert [result.latlng for result in g] == expected_results
