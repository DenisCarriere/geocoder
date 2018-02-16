# coding: utf8

import os
import geocoder
import requests_mock

address = 'The Happy Goat, Ottawa'
location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)


def test_opencage():
    """ Expected result :
        https://api.opencagedata.com/geocode/v1/json?q=Ottawa,Ontario&key=YOUR-API-KEY
    """
    g = geocoder.opencage(location)
    assert g.ok
    assert len(g) == 1
    assert g.country_code == 'ca'
    assert g.state == 'Ontario'
    assert g.state_code == 'ON'
    assert g.city == 'Ottawa'
    assert g.town == 'Ottawa'
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 23


def test_issue_292():
    g = geocoder.opencage('AirportClinic M - MediCare Flughafen München Medizinisches Zentrum', countrycode='DE', language='de', no_annotations=1)
    assert g.ok

def test_opencage_no_language_param():
    """ Expected result :
        https://api.opencagedata.com/geocode/v1/json=Ottawa,Ontario&key=YOUR-API-KEY
    """
    g = geocoder.opencage(location)
    assert 'language' not in g.url

def test_opencage_language_param():
    """ Expected result :
        https://api.opencagedata.com/geocode/v1/json=Ottawa,Ontario&key=YOUR-API-KEY&language=de
    """
    g = geocoder.opencage(location, language='de')
    assert 'language=de' in g.url.split('&')

def test_opencage_multi_result():
    g = geocoder.opencage(location, maxRows=5)
    assert len(g) > 1


def test_opencage_address():
    """ Expected result :
        https://api.opencagedata.com/geocode/v1/json?q=The+Happy+Goat,+Ottawa&key=YOUR-API-KEY
    """
    g = geocoder.opencage(address)
    assert g.ok
    assert g.country == 'Canada'
    assert g.state == 'Ontario'
    assert g.state_code == 'ON'
    assert g.city == 'Ottawa'
    assert g.street == 'Wilbrod Street'
    assert g.housenumber == '317'
    assert g.postal.startswith('K1N')
    assert (g.remaining_api_calls > 0 and g.remaining_api_calls != 999999)
    assert (g.limit_api_calls > 0 and g.remaining_api_calls != 999999)

def test_opencage_paid():
    # Paid API keys can be set to unlimited and have rate limit information ommitted from the response
    url = 'http://api.opencagedata.com/geocode/v1/json?query=The+Happy+Goat%2C+Ottawa&limit=1&key=' + os.environ.get('OPENCAGE_API_KEY')
    data_file = 'tests/results/opencagedata_paid.json'
    with requests_mock.Mocker() as mocker, open(data_file, 'r') as input:
        mocker.get(url, text=input.read())
        result = geocoder.opencage(address)
        assert result.ok
        osm_count, fields_count = result.debug()[0]
        assert osm_count >= 3
        assert fields_count >= 15
        assert result.remaining_api_calls == 999999
        assert result.limit_api_calls == 999999




def test_opencage_reverse():
    """ Expected result :
        https://api.opencagedata.com/geocode/v1/json?q=45.4215296,-75.6971930&key=YOUR-API-KEY
    """
    g = geocoder.opencage(ottawa, method='reverse')
    assert g.ok
