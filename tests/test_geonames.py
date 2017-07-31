# coding: utf8

import geocoder

import requests_mock

address = 'The Happy Goat, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_geonames():
    url = 'http://api.geonames.org/searchJSON?q=Ottawa%2C+Ontario&fuzzy=0.8&username=mock&maxRows=1'
    text = """{
  "totalResultsCount": 142,
  "geonames": [{
    "adminCode1": "08",
    "lng": "-75.69812",
    "geonameId": 6094817,
    "toponymName": "Ottawa",
    "countryId": "6251999",
    "fcl": "P",
    "population": 812129,
    "countryCode": "CA",
    "name": "Ottawa",
    "fclName": "city, village,...",
    "countryName": "Canada",
    "fcodeName": "capital of a political entity",
    "adminName1": "Ontario",
    "lat": "45.41117",
    "fcode": "PPLC"
  }]
}"""
    with requests_mock.Mocker() as mocker:
        mocker.get(url, text=text)
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
    text = """{
  "totalResultsCount": 2,
  "geonames": [
    {
      "adminCode1": "10",
      "lng": "-75.76583",
      "geonameId": 5901584,
      "toponymName": "Birch Manor",
      "countryId": "6251999",
      "fcl": "P",
      "population": 0,
      "countryCode": "CA",
      "name": "Birch Manor",
      "fclName": "city, village,...",
      "countryName": "Canada",
      "fcodeName": "section of populated place",
      "adminName1": "Quebec",
      "lat": "45.42472",
      "fcode": "PPLX"
    },
    {
      "adminCode1": "10",
      "lng": "-75.58833",
      "geonameId": 6162703,
      "toponymName": "Templeton-Est",
      "countryId": "6251999",
      "fcl": "P",
      "population": 0,
      "countryCode": "CA",
      "name": "Templeton-Est",
      "fclName": "city, village,...",
      "countryName": "Canada",
      "fcodeName": "section of populated place",
      "adminName1": "Quebec",
      "lat": "45.49389",
      "fcode": "PPLX"
    }
  ]
}"""
    with requests_mock.Mocker() as mocker:
        mocker.get(url, text=text)
        g = geocoder.geonames(6094817, method='children', username='mock')
        assert g.ok
        assert len(g.parse['geonames']) == 2
        expected_names = set(("Birch Manor", "Templeton-Est"))
        results = set([res['toponymName'] for res in g.parse['geonames']])
        assert expected_names == results


def test_hierarchy():
    url = 'http://api.geonames.org/hierarchyJSON?geonameId=6094817&username=mock'
    text = """{"geonames": [
  {
    "lng": "0",
    "geonameId": 6295630,
    "name": "Earth",
    "fclName": "parks,area, ...",
    "toponymName": "Earth",
    "fcodeName": "area",
    "adminName1": "",
    "lat": "0",
    "fcl": "L",
    "fcode": "AREA",
    "population": 6814400000
  },
  {
    "lng": "-100.54688",
    "geonameId": 6255149,
    "name": "North America",
    "fclName": "parks,area, ...",
    "toponymName": "North America",
    "fcodeName": "continent",
    "adminName1": "",
    "lat": "46.07323",
    "fcl": "L",
    "fcode": "CONT",
    "population": 0
  },
  {
    "adminCode1": "00",
    "lng": "-113.64258",
    "geonameId": 6251999,
    "toponymName": "Canada",
    "countryId": "6251999",
    "fcl": "A",
    "population": 33679000,
    "countryCode": "CA",
    "name": "Canada",
    "fclName": "country, state, region,...",
    "countryName": "Canada",
    "fcodeName": "independent political entity",
    "adminName1": "",
    "lat": "60.10867",
    "fcode": "PCLI"
  },
  {
    "adminCode1": "08",
    "lng": "-84.49983",
    "geonameId": 6093943,
    "toponymName": "Ontario",
    "countryId": "6251999",
    "fcl": "A",
    "population": 12861940,
    "countryCode": "CA",
    "name": "Ontario",
    "fclName": "country, state, region,...",
    "countryName": "Canada",
    "fcodeName": "first-order administrative division",
    "adminName1": "Ontario",
    "lat": "49.25014",
    "fcode": "ADM1"
  },
  {
    "adminCode1": "08",
    "lng": "-75.69812",
    "geonameId": 6094817,
    "toponymName": "Ottawa",
    "countryId": "6251999",
    "fcl": "P",
    "population": 812129,
    "countryCode": "CA",
    "name": "Ottawa",
    "fclName": "city, village,...",
    "countryName": "Canada",
    "fcodeName": "capital of a political entity",
    "adminName1": "Ontario",
    "lat": "45.41117",
    "fcode": "PPLC"
  }
]}"""
    with requests_mock.Mocker() as mocker:
        mocker.get(url, text=text)
    g = geocoder.geonames(6094817, method='hierarchy', username='mock')
    assert g.ok
    assert len(g.parse['geonames']) == 5
    expected_names = set(
        ("Earth", "North America", "Canada", "Ontario", "Ottawa"))
    results = set([res['toponymName'] for res in g.parse['geonames']])
    assert expected_names == results
