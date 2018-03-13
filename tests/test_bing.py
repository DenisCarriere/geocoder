# coding: utf8
from builtins import str
import requests_mock
import geocoder

location = 'Ottawa, Ontario'
city = 'Ottawa'
ottawa = (45.4215296, -75.6971930)
locations_forward = ['Denver,CO', 'Boulder,CO']
locations_reverse = [[40.7943, -73.970859], [48.845580, 2.321807]]


def test_bing():
    g = geocoder.bing(location)
    assert g.ok
    assert g.city == city
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 12


def test_bing_details():
    details = {
        'adminDistrict': 'Ontario',
        'locality': 'Ottawa'
    }

    g = geocoder.bing(None, method='details', **details)
    assert g.ok
    assert g.city == city
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 12

    details = {
        'addressLine': '6912 Route 8',
        'adminDistrict': 'Northumberland',
        'countryRegion': 'CA',
        'locality': 'Ludlow'
    }

    g = geocoder.bing(None, method='details', **details)
    assert g.ok
    osm_count, fields_count = g.debug()[0]
    assert osm_count >= 3
    assert fields_count >= 12


def test_bing_reverse():
    g = geocoder.bing(ottawa, method='reverse')
    assert g.ok
    assert g.city == city



def test_bing_batch_forward():
    """ Data subnitted would be the following:
            Bing Spatial Data Services, 2.0
            Id,GeocodeRequest/Query,GeocodeResponse/Point/Latitude,GeocodeResponse/Point/Longitude
            0,"Denver,CO",,
            1,"Boulder,CO",,
    """
    url_submission = 'http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode?input=csv&key=test'
    url_check = 'http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/3bf1b729dddd498e9df45515cdb36130'
    url_result = 'http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/3bf1b729dddd498e9df45515cdb36130/output/succeeded'
    submission_file = 'tests/results/bing_batch_submission.json'
    confirmation_file = 'tests/results/bing_batch_confirmation.json'
    data_file = 'tests/results/bing_batch.csv'
    with requests_mock.Mocker() as mocker, \
            open(submission_file, 'rb') as submission_result, \
            open(confirmation_file, 'rb') as confirmation_result, \
            open(data_file, 'rb') as batch_result:
        mocker.post(url_submission, text=str(submission_result.read(), 'utf8'))
        mocker.get(url_check, text=str(confirmation_result.read(), 'utf8'))
        mocker.get(url_result, text=str(batch_result.read(), 'utf8'))
        g = geocoder.bing(locations_forward, key='test', method='batch')
        assert g.ok
        assert len(g) == 2
        expected_results = [
            [39.7400093078613, -104.99201965332],
            [40.015739440918, -105.279243469238]
        ]
        assert [result.latlng for result in g] == expected_results


def test_bing_batch_reverse():
    g = geocoder.bing(locations_reverse, method='batch_reverse')
    assert g.ok
    assert len(g) == 2
    assert [result.city for result in g] == ['New York', 'Paris']


def test_multi_results():
    g = geocoder.bing(location, maxRows=3)

    assert len(g) == 2
    assert g.city == city

    expected_results = [
        [45.4217796325684, -75.6911926269531],
        [45.2931327819824, -75.7756805419922]
    ]
    assert [result.latlng for result in g] == expected_results
