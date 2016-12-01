#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
import time
from geocoder.base import Base
from geocoder.keys import google_key

# todo: Paging (pagetoken) is not fully supported since we only return the first result.  Need to return all results to the user so paging will make sense
# todo: Add support for missing results fields html_attributions, opening_hours, photos, scope, alt_ids, types [not just the first one]
# todo: Add support for nearbysearch and radarsearch variations of the Google Places API


class Places(Base):
    """
    Google Places API
    ====================
    The Google Places API Web Service allows you to query for place information on a variety of categories,
    such as: establishments, prominent points of interest, geographic locations, and more.
    You can search for places either by proximity or a text string.
    A Place Search returns a list of places along with summary information about each place; additional
    information is available via a Place Details query.

    At this time, only the "Text Search" is supported by this library.  "Text Search" can be used
    when you don't have pristine formatted addresses required by the regular Google Maps Geocoding API
    or when you want to do 'nearby' searches like 'restaurants near Sydney'.

    The Geocoding best practices reference indicates that when you have 'ambiguous queries in an automated system
    you would be better served using the Places API Text Search than the Maps Geocoding API
    https://developers.google.com/maps/documentation/geocoding/best-practices

    API Reference
    -------------
    https://developers.google.com/places/web-service/intro
    https://developers.google.com/places/web-service/search

    l = geocoder.google('Elm Plaza Shopping Center, Enfield, CT 06082', method='places')
    l = geocoder.google('food near white house', method='places')
    l = geocoder.google('1st and main', method='places')

    Parameters
    ----------
    :param query: Your search location or phrase you want geocoded.
    :param key: Your Google developers free key.

    :param location: (optional) lat,lng point around which results will be given preference
    :param radius: (optional) in meters, used with location
    :param language: (optional) 2-letter code of preferred language of returned address elements.
    :param minprice: (optional) 0 (most affordable) to 4 (most expensive)
    :param maxprice: (optional) 0 (most affordable) to 4 (most expensive)
    :param opennow: (optional) value is ignored. when present, closed places and places without opening hours will be omitted
    :param pagetoken: (optional) get next 20 results from previously run search.  when set, other criteria are ignored
    :param type: (optional) restrict results to one type of place
    """
    provider = 'google'
    method = 'places'

    def __init__(self, query, **kwargs):
        self.url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        self.location = query
        self.params = {
            # required
            'query': self.location,
            'key': kwargs.get('key', google_key),

            # optional
            'location': kwargs.get('location', ''),
            'radius': kwargs.get('radius', ''),
            'language': kwargs.get('language', ''),
            'minprice': kwargs.get('minprice', ''),
            'maxprice': kwargs.get('maxprice', ''),
            'type': kwargs.get('type', ''),
        }

        # optional, don't send unless needed
        if 'opennow' in kwargs:
            self.params['opennow'] = ''

        # optional, don't send unless needed
        if 'pagetoken' in kwargs:
            self.params['pagetoken'] = kwargs['pagetoken']

        self._initialize(**kwargs)

    def _exceptions(self):
        if self.parse['results']:
            self._build_tree(self.parse['results'][0])

    @property
    def lat(self):
        return self.parse['location'].get('lat')

    @property
    def lng(self):
        return self.parse['location'].get('lng')

    @property
    def id(self):
        return self.parse.get('id')

    @property
    def reference(self):
        return self.parse.get('reference')

    @property
    def place_id(self):
        return self.parse.get('place_id')

    @property
    def type(self):
        type = self.parse.get('types')
        if type:
            return type[0]

    @property
    def address(self):
        return self.parse.get('formatted_address')

    @property
    def icon(self):
        return self.parse.get('icon')

    @property
    def name(self):
        return self.parse.get('name')

    @property
    def vicinity(self):
        return self.parse.get('vicinity')

    @property
    def price_level(self):
        return self.parse.get('price_level')

    @property
    def rating(self):
        return self.parse.get('rating')

    @property
    def next_page_token(self):
        return self.parse.get('next_page_token')

    @property
    def query(self):
        return self.location

if __name__ == '__main__':
    g = Places('11 Wall Street, New York', method='places', key='<API KEY>')
    g.debug()
