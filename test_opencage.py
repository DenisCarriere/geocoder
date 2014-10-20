import geocoder


location = '36 Biscayne St, Kingston'

def test_opencage():
    g = geocoder.opencage(location)
    print g.help()

def test_nokia():
    g = geocoder.nokia(location)
    print g.debug()

if __name__ == '__main__':
    test_opencage()