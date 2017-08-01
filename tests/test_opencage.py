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
    assert g.country == 'ca'
    assert g.state == 'Ontario'
    assert g.state_code == 'ON'
    assert g.city == 'Ottawa'
    assert g.town == 'Ottawa'


def test_opencage_address():
    """ Expected result :
        https://api.opencagedata.com/geocode/v1/json?q=The+Happy+Goat,+Ottawa&key=YOUR-API-KEY
    """
    g = geocoder.opencage(address)
    assert g.ok
    assert g.country == 'ca'
    assert g.state == 'Ontario'
    assert g.state_code == 'ON'
    assert g.city == 'Ottawa'
    assert g.street == 'Wilbrod Street'
    assert g.housenumber == '317'
    assert g.postal == 'K1N 6K4'


def test_opencage_reverse():
    """ Expected result :
        https://api.opencagedata.com/geocode/v1/json?q=45.4215296,-75.6971930&key=YOUR-API-KEY
    """
    g = geocoder.opencage(ottawa, method='reverse')
    assert g.ok
    assert g.country == 'ca'
    assert g.state == 'Ontario'
    assert g.state_code == 'ON'
    assert g.city == 'Ottawa'
    assert g.street == 'O\'Connor Street'
    assert g.housenumber == '45'
