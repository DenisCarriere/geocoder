import geocoder

location = 'Canada'
ip = '74.125.226.99'

def test_entry_points():
    geocoder.ip
    geocoder.osm
    geocoder.bing
    geocoder.nokia
    geocoder.google
    geocoder.tomtom
    geocoder.reverse
    geocoder.mapquest

def test_google():
    g = geocoder.google(location)
    assert g.ok

def test_bing():
    ok = False
    for i in xrange(3):
        g = geocoder.bing(location)
        if g.ok:
            ok = True
    assert ok

def test_osm():
    g = geocoder.osm(location)
    assert g.ok

def test_tomtom():
    g = geocoder.tomtom(location)
    assert g.ok

def test_arcgis():
    g = geocoder.arcgis(location)
    assert g.ok

def test_mapquest():
    g = geocoder.mapquest(location)
    assert g.ok

def test_reverse():
    g = geocoder.ip(ip)
    assert g.ok
