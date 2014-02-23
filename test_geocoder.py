import geocoder


def test(location, provider):
    g = geocoder.get(location, provider=provider)
    g.debug()

if __name__ == '__main__':
    location = 'New York City'
    geocoders = ['osm', 'google', 'bing', 'nokia', 'mapquest', 'tomtom', 'esri']
    #geocoders = ['esri']
    for name in geocoders:
        test(location, name)