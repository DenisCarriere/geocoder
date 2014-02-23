import geocoder


if __name__ == '__main__':
    location = 'Ottawa Ontario'
    g = geocoder.mapquest(location)
    g.debug()
