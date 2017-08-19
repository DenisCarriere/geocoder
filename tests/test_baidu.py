# coding=utf-8
import geocoder

address = 'The Happy Goat, Ottawa'
location = '兆维华灯大厦,北京'
city = '北京'
place = (39.9789660352, 116.497157786)


def test_baidu():
    """ Expected result :
        http://api.map.baidu.com/geocoder/v2/?callback=renderOption&output=json&address=百度大厦&city=北京市&ak=<Your API Key>
    """
    g = geocoder.baidu(location)
    assert g.ok


def test_baidu_reverse():
    """ Expected result :
        http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=39.9789660352,116.497157786&output=json&pois=1&ak=<Your API Key>
    """
    g = geocoder.baidu(place, method='reverse')
    assert g.ok
    assert g.country == '中国'
    assert g.state == '北京市'
    assert g.city == '北京市'
    assert g.street == u'酒仙桥路'
