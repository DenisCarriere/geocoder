from base import Base


class Tomtom(Base):
    name = 'TomTom'
    url = 'https://api.tomtom.com/lbs/geocoding/geocode'
    key = '95kjrqtpzv39ujcxfyr57wz3'

    def __init__(self, location, key=''):
        self.location = location
        if not key:
            key = self.key
        self.json = dict()
        self.params = dict()
        self.params['key'] = key
        self.params['query'] = location
        self.params['format'] = 'json'
        self.params['maxResults'] = 1

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

    def country(self):
        return self.safe_format('geoResult-country')

    def city(self):
        return self.safe_format('geoResult-city')
