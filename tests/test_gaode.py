# coding=utf-8
import geocoder

location = '兆维华灯大厦,北京'
city = '北京'
place = (39.9789660352, 116.497157786)


def test_gaode():
    """ Expected result :
        http://restapi.amap.com/v3/geocode/geo?address=兆维华灯大厦,北京&output=XML&key=<用户的key>
    """
    g = geocoder.gaode(location, key='0716e5809437f14e3dd0793a5c6d2b13')
    assert g.ok


def test_gaode_reverse():
    """ Expected result :
        http://restapi.amap.com/v3/geocode/regeo?output=xml&location=116.310003,39.991957&key=<用户的key>&radius=1000&extensions=all
    """
    g = geocoder.gaode(place, method='reverse', key='0716e5809437f14e3dd0793a5c6d2b13')
    assert g.ok
    assert g.country == u'中国'
    assert g.state == u'北京市'
    assert g.city == u'北京市'
    assert g.street == u'UBP东街'
