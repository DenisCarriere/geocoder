from base import Base


class Tomtom(Base):
    name = 'TomTom'
    url = 'https://api.tomtom.com/lbs/geocoding/geocode'

    def __init__(self, location, key):
        self.location = location
        self.json = dict()
        self.params = dict()
        self.params['key'] = key
        self.params['query'] = location
        self.params['format'] = 'json'
        self.params['maxResults'] = 1
        if not key:
            self.help_key()

    def lat(self):
        return self.safe_coord('geoResult-latitude')

    def lng(self):
        return self.safe_coord('geoResult-longitude')

    def address(self):
        return self.safe_format('geoResult-formattedAddress')

    def quality(self):
        return self.safe_format('geoResult-type')

    def postal(self):
        return self.safe_format('geoResult-postcode')

    def city(self):
        return self.safe_format('geoResult-city')

    def state(self):
        return self.safe_format('geoResult-state')

    def country(self):
        return self.safe_format('geoResult-country')

    def help_key(self):
        print '<ERROR> Please provide a Key paramater when using TomTom'
        print '>>> import geocoder'
        print '>>> key = "XXXX"'
        print '>>> g = geocoder.tomtom(<location>, key=key)'
        print ''
        print 'How to get a Key?'
        print '-----------------'
        print 'http://developer.tomtom.com/products/geocoding_api'