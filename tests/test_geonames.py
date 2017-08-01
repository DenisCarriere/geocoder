# coding: utf8

import json
import geocoder

import requests_mock

address = 'The Happy Goat, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_geonames():
    url = 'http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=0.8&username=mock&maxRows=1'
    data_file = 'tests/results/geonames.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(location, username='mock')
        assert g.ok
        assert g.country == 'Canada'
        assert g.country_code == 'CA'
        assert g.state == 'Ontario'
        assert g.state_code == '08'
        assert g.description == 'capital of a political entity'
        assert g.class_description == 'city, village,...'
        assert g.feature_class == 'P'
        assert g.code == 'PPLC'
        assert g.geonames_id == 6094817


def test_children():
    url = 'http://api.geonames.org/childrenJSON?geonameId=6094817&username=mock'
    data_file = 'tests/results/geonames_children.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(6094817, method='children', username='mock')
        assert g.ok
        assert len(g.parse['geonames']) == 2
        expected_names = set(("Birch Manor", "Templeton-Est"))
        results = set([res['toponymName'] for res in g.parse['geonames']])
        assert expected_names == results


def test_hierarchy():
    url = 'http://api.geonames.org/hierarchyJSON?geonameId=6094817&username=mock'
    data_file = 'tests/results/geonames_hierarchy.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
    g = geocoder.geonames(6094817, method='hierarchy', username='mock')
    assert g.ok
    assert len(g.parse['geonames']) == 5
    expected_names = set(
        ("Earth", "North America", "Canada", "Ontario", "Ottawa"))
    results = set([res['toponymName'] for res in g.parse['geonames']])
    assert expected_names == results
