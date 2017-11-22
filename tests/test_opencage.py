# coding: utf8

import geocoder

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


def test_opencage_reverse():
    """ Expected result :
        https://api.opencagedata.com/geocode/v1/json?q=45.4215296,-75.6971930&key=YOUR-API-KEY
    """
    g = geocoder.opencage(ottawa, method='reverse')
    assert g.ok
