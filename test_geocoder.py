import geocoder


if __name__ == '__main__':
    location = '1552 Payette dr., Ottawa Ontario'
    geocoders = ['osm', 'google', 'bing', 'nokia', 'mapquest', 'tomtom', 'esri']
    
    g = geocoder.mapquest(location)

    g.debug()