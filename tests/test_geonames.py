# coding: utf8
import json
import pytest
import geocoder

import requests_mock

address = 'The Happy Goat, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


@pytest.fixture(scope='module')
def geonames_response(request):
    url = 'http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=1.0&username=mock&maxRows=1'
    data_file = 'tests/results/geonames.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        result = geocoder.geonames(location, key='mock')
    return result


@pytest.fixture(scope='module')
def paid_geonames_response(request):
    url = 'http://ws.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=1.0&username=mock&maxRows=1'
    data_file = 'tests/results/geonames.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        result = geocoder.geonames(
            location, url='http://ws.geonames.org/searchJSON', key='mock')
    return result


def test_geonames_query(geonames_response):
    assert geonames_response.ok
    assert repr(geonames_response) == '<[OK] Geonames - Geocode [Ottawa]>'
    assert len(geonames_response) == 1
    assert geonames_response.status_code == 200
    osm_count, fields_count = geonames_response.debug()[0]
    assert osm_count >= 2
    assert fields_count >= 16


def test_paid_geonames_url(paid_geonames_response):
    assert paid_geonames_response.ok
    assert repr(paid_geonames_response) == '<[OK] Geonames - Geocode [Ottawa]>'
    assert len(paid_geonames_response) == 1
    assert paid_geonames_response.status_code == 200
    osm_count, fields_count = paid_geonames_response.debug()[0]
    assert osm_count >= 2
    assert fields_count >= 16


def test_geonames_first_result(geonames_response):
    point = geonames_response[0]
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


def test_geonames_geojson(geonames_response):
    geojson_file = 'tests/results/geonames.geo.json'
    with open(geojson_file, 'r') as geojson_stream:
        expected_geo_json = json.load(geojson_stream)
        assert geonames_response.geojson == expected_geo_json


def test_geonames_delegation(geonames_response):
    # next calls are delegated to result
    assert geonames_response.geonames_id == 6094817
    assert geonames_response.lat == '45.41117'
    assert geonames_response.lng == '-75.69812'
    assert geonames_response.address == 'Ottawa'
    assert geonames_response.country == 'Canada'
    assert geonames_response.country_code == 'CA'
    assert geonames_response.state == 'Ontario'
    assert geonames_response.state_code == '08'
    assert geonames_response.description == 'capital of a political entity'
    assert geonames_response.class_description == 'city, village,...'
    assert geonames_response.feature_class == 'P'
    assert geonames_response.code == 'PPLC'
    assert geonames_response.population == 812129


def test_extra():
    url = 'http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=1.0&username=mock&maxRows=1&featureClass=A'
    data_file = 'tests/results/geonames_extra.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(location, key='mock', featureClass='A')
        assert g.ok
        assert g.geonames_id == 8581623
        assert g.lat == '45.41858'
        assert g.lng == '-75.69717'
        assert g.address == 'Ottawa'
        assert g.country == 'Canada'
        assert g.country_code == 'CA'
        assert g.description == 'second-order administrative division'
        assert g.class_description == 'country, state, region,...'
        assert g.feature_class == 'A'
        assert g.code == 'ADM2'


def test_details():
    url = 'http://api.geonames.org/getJSON?geonameId=6094817&username=mock&style=full'
    data_file = 'tests/results/geonames_details.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(6094817, method='details', key='mock')

        assert g.lat == "45.41117"
        assert g.lng == "-75.69812"
        assert g.geonames_id == 6094817
        assert g.address == "Ottawa"
        assert g.feature_class == "P"
        assert g.class_description == "city, village,..."
        assert g.code == "PPLC"
        assert g.description == "capital of a political entity"
        assert g.continent == "NA"
        assert g.country_geonames_id == "6251999"
        assert g.country_code == "CA"
        assert g.country == "Canada"
        assert g.state == "Ontario"
        assert g.state_code == "08"
        assert g.state_geonames_id == "6093943"
        assert g.admin2 == ""
        assert g.admin3 == ""
        assert g.admin4 == ""
        assert g.admin5 == ""
        assert g.population == 812129
        assert g.srtm3 == 71
        assert g.wikipedia == "en.wikipedia.org/wiki/Ottawa"
        assert g.timeZoneId == "America/Toronto"
        assert g.timeZoneName == "America/Toronto"
        assert g.rawOffset == -5
        assert g.dstOffset == -4
        assert g.bbox == {
            'northeast': [45.58753415000007, -75.07957784899992],
            'southwest': [44.962202955000066, -76.35400795899994]}


def test_children():
    url = 'http://api.geonames.org/childrenJSON?geonameId=6094817&username=mock'
    data_file = 'tests/results/geonames_children.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(6094817, method='children', key='mock')
        assert g.ok
        assert repr(g) == '<[OK] Geonames - Children #2 results>'
        assert len(g) == 2
        assert g.status_code == 200

        expected_names = ["Birch Manor", "Templeton-Est"]
        expected_geonames_id = [5901584, 6162703]
        assert expected_names == [res.address for res in g]
        assert expected_geonames_id == [res.geonames_id for res in g]


def test_children_delegation():
    url = 'http://api.geonames.org/childrenJSON?geonameId=6094817&username=mock'
    data_file = 'tests/results/geonames_children.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(6094817, method='children', key='mock')
        assert g.ok
        assert repr(g) == '<[OK] Geonames - Children #2 results>'

        # next calls are delegated to result
        assert g.address == "Birch Manor"
        assert g.geonames_id == 5901584

        g.set_default_result(1)
        assert g.address == "Templeton-Est"
        assert g.geonames_id == 6162703


def test_hierarchy():
    url = 'http://api.geonames.org/hierarchyJSON?geonameId=6094817&username=mock'
    data_file = 'tests/results/geonames_hierarchy.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(6094817, method='hierarchy', key='mock')
        assert g.ok
        assert repr(g) == '<[OK] Geonames - Hierarchy #5 results>'
        assert len(g) == 5
        assert g.status_code == 200

        expected_names = ["Earth", "North America",
                          "Canada", "Ontario", "Ottawa"]
        assert expected_names == [res.address for res in g]


def test_geocoding_with_proximity():
    # query google first to get a bbox
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
        google = geocoder.google(location, client=None, key='mock')
    # query geonames with bbox
    url = 'http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=1.0&username=mock&maxRows=1&east=-75.2465979&west=-76.3539158&north=45.5375801&south=44.962733'
    data_file = 'tests/results/geonames_proximity.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        g = geocoder.geonames(location, key='mock', proximity=google.bbox)
        assert g.ok
