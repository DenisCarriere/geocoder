# -*- coding: utf-8 -*-

from base import Base


class Mapquest(Base):
    name = 'MapQuest'
    url = 'http://www.mapquestapi.com/geocoding/v1/address'

    def __init__(self, location):
        self.location = location
        self.referer = 'http://www.mapquestapi.com/geocoding/'
        self.json = dict()
        self.params = dict()
        self.params['location'] = location
        self.params['inFormat'] = 'kvp'
        self.params['outFormat'] = 'json'
        self.params['maxResults'] = 1
        self.params['thumbMaps'] = 'false'
        self.params['key'] = 'Kmjtd|luua2qu7n9,7a=o5-lzbgq'

    def lat(self):
        return self.safe_coord('latLng-lat')

    def lng(self):
        return self.safe_coord('latLng-lng')

    def address(self):
        # No single line address exists for Mapquest :(
        return self.location

    def quality(self):
        return self.safe_format('locations-geocodeQuality')

    def postal(self):
        return self.safe_format('locations-postalCode')

    def city(self):
        return self.safe_format('locations-adminArea5')

    def country(self):
        return self.safe_format('locations-adminArea1')
