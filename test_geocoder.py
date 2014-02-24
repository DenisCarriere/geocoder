import geocoder

location = 'Ottawa, Ontario'

# Providers
osm = geocoder.osm(location)
bing = geocoder.bing(location)
nokia = geocoder.nokia(location)
google = geocoder.google(location)
arcgis = geocoder.arcgis(location)
tomtom = geocoder.tomtom(location)
mapquest = geocoder.mapquest(location)

# Testing for [latlng]
def test_osm_latlng():
    assert hasattr(osm, 'latlng')

def test_bing_latlng():
    assert hasattr(bing, 'latlng')

def test_nokia_latlng():
    assert hasattr(nokia, 'latlng')

def test_google_latlng():
    assert hasattr(google, 'latlng')

def test_arcgis_latlng():
    assert hasattr(arcgis, 'latlng')

def test_tomtom_latlng():
    assert hasattr(tomtom, 'latlng')

def test_mapquest_latlng():
    assert hasattr(mapquest, 'latlng')

# Testing for [address]
def test_osm_address():
    assert hasattr(osm, 'address')

def test_bing_address():
    assert hasattr(bing, 'address')

def test_nokia_address():
    assert hasattr(nokia, 'address')

def test_google_address():
    assert hasattr(google, 'address')

def test_arcgis_address():
    assert hasattr(arcgis, 'address')

def test_tomtom_address():
    assert hasattr(tomtom, 'address')

def test_mapquest_address():
    assert hasattr(mapquest, 'address')


# Testing for [postal]
def test_osm_postal():
    assert hasattr(osm, 'postal')

def test_bing_postal():
    assert hasattr(bing, 'postal')

def test_nokia_postal():
    assert hasattr(nokia, 'postal')

def test_google_postal():
    assert hasattr(google, 'postal')

def test_arcgis_postal():
    assert hasattr(arcgis, 'postal')

def test_tomtom_postal():
    assert hasattr(tomtom, 'postal')

def test_mapquest_postal():
    assert hasattr(mapquest, 'postal')
