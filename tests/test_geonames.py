# coding: utf8

import geocoder

import requests_mock

address = 'The Happy Goat, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_geonames_for_one_result():
    url = 'http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=0.8&username=mock&maxRows=1'
    data_file = 'tests/results/geonames.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(location, username='mock')
        assert g.ok
        assert repr(g) == '<[OK] Geonames - Geocode [Ottawa]>'
        assert len(g) == 1
        assert g.status_code == 200
        assert g.url == 'http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=0.8&username=mock&maxRows=1'

        point = g.pop()
        assert point.ok
        assert point.geonames_id == 6094817
        assert point.lat == '45.41117'
        assert point.lng == '-75.69812'
        assert point.address == 'Ottawa'
        assert point.country == 'Canada'
        assert point.country_code == 'CA'
        assert point.state == 'Ontario'
        assert point.state_code == '08'
        assert point.description == 'capital of a political entity'
        assert point.class_description == 'city, village,...'
        assert point.feature_class == 'P'
        assert point.code == 'PPLC'
        assert point.population == 812129


def test_geonames_delegation():
    url = 'http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=0.8&username=mock&maxRows=1'
    data_file = 'tests/results/geonames.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(location, username='mock')
        assert g.ok
        assert repr(g) == '<[OK] Geonames - Geocode [Ottawa]>'

        # next calls are delegated to result
        assert g.geonames_id == 6094817
        assert g.lat == '45.41117'
        assert g.lng == '-75.69812'
        assert g.address == 'Ottawa'
        assert g.country == 'Canada'
        assert g.country_code == 'CA'
        assert g.state == 'Ontario'
        assert g.state_code == '08'
        assert g.description == 'capital of a political entity'
        assert g.class_description == 'city, village,...'
        assert g.feature_class == 'P'
        assert g.code == 'PPLC'
        assert g.population == 812129

def test_children():
    url = 'http://api.geonames.org/childrenJSON?geonameId=6094817&username=mock'
    data_file = 'tests/results/geonames_children.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(6094817, method='children', username='mock')
        assert g.ok
        assert repr(g) == '<[OK] Geonames - Children #2 results>'
        assert len(g) == 2
        assert g.status_code == 200
        assert g.url == url

        expected_names = ["Birch Manor", "Templeton-Est"]
        expected_geonames_id = [5901584, 6162703]
        assert expected_names == [res.address for res in g]
        assert expected_geonames_id == [res.geonames_id for res in g]

def test_children_delegation():
    url = 'http://api.geonames.org/childrenJSON?geonameId=6094817&username=mock'
    data_file = 'tests/results/geonames_children.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(6094817, method='children', username='mock')
        assert g.ok
        assert repr(g) == '<[OK] Geonames - Children #2 results>'

        # next calls are delegated to result
        assert g.address == "Birch Manor"
        assert g.geonames_id == 5901584

        g.expose_result(1)
        assert g.address == "Templeton-Est"
        assert g.geonames_id == 6162703

def test_hierarchy():
    url = 'http://api.geonames.org/hierarchyJSON?geonameId=6094817&username=mock'
    data_file = 'tests/results/geonames_hierarchy.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
    g = geocoder.geonames(6094817, method='hierarchy', username='mock')
    assert g.ok
    assert repr(g) == '<[OK] Geonames - Hierarchy #5 results>'
    assert len(g) == 5
    assert g.status_code == 200
    assert g.url == url

    expected_names = ["Earth", "North America", "Canada", "Ontario", "Ottawa"]
    assert expected_names == [res.address for res in g]
