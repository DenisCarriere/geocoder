#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import google_key
from geocoder.location import BBox

# todo: Paging (pagetoken) is not fully supported since we only return the first result.  Need to return all results to the user so paging will make sense
# todo: Add support for missing results fields html_attributions, opening_hours, photos, scope, alt_ids, types [not just the first one]
# todo: Add support for nearbysearch and radarsearch variations of the Google Places API


class PlacesResult(OneResult):

    def __init__(self, json_content):
        # flatten geometry
        geometry = json_content.get('geometry', {})
        self._location = geometry.get('location', {})
        json_content['northeast'] = geometry.get(
            'viewport', {}).get('northeast', {})
        json_content['southwest'] = geometry.get(
            'viewport', {}).get('southwest', {})

        # proceed with super.__init__
        super(PlacesResult, self).__init__(json_content)

    @property
    def lat(self):
        return self._location.get('lat')

    @property
    def lng(self):
        return self._location.get('lng')

    @property
    def id(self):
        return self.raw.get('id')

    @property
    def reference(self):
        return self.raw.get('reference')

    @property
    def place_id(self):
        return self.raw.get('place_id')

    @property
    def type(self):
        type = self.raw.get('types')
        if type:
            return type[0]

    @property
    def address(self):
        return self.raw.get('formatted_address')

    @property
    def icon(self):
        return self.raw.get('icon')

    @property
    def name(self):
        return self.raw.get('name')

    @property
    def vicinity(self):
        return self.raw.get('vicinity')

    @property
    def price_level(self):
        return self.raw.get('price_level')

    @property
    def rating(self):
        return self.raw.get('rating')


class PlacesQuery(MultipleResultsQuery):
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
    :param location: Your search location or phrase you want geocoded.
    :param key: Your Google developers free key.

    :param proximity: (optional) lat,lng point around which results will be given preference
    :param radius: (optional) in meters, used with proximity
    :param language: (optional) 2-letter code of preferred language of returned address elements.
    :param minprice: (optional) 0 (most affordable) to 4 (most expensive)
    :param maxprice: (optional) 0 (most affordable) to 4 (most expensive)
    :param opennow: (optional) value is ignored. when present, closed places and places without opening hours will be omitted
    :param pagetoken: (optional) get next 20 results from previously run search.  when set, other criteria are ignored
    :param type: (optional) restrict results to one type of place
    """
    provider = 'google'
    method = 'places'

    _URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    _RESULT_CLASS = PlacesResult
    _KEY = google_key

    def __init__(self, location, **kwargs):
        super(PlacesQuery, self).__init__(location, **kwargs)

        self.next_page_token = None

    def _build_params(self, location, provider_key, **kwargs):
        # handle specific case of proximity (aka 'location' for google)
        bbox = kwargs.get('proximity', '')
        if bbox:
            bbox = BBox.factory(bbox)
            # do not forget to convert bbox to google expectations...
            bbox = bbox.latlng

        # define all
        params = {
            # required
            'query': location,
            'key': provider_key,

            # optional
            'location': bbox,
            'radius': kwargs.get('radius', ''),
            'language': kwargs.get('language', ''),
            'minprice': kwargs.get('minprice', ''),
            'maxprice': kwargs.get('maxprice', ''),
            'type': kwargs.get('type', ''),
        }

        # optional, don't send unless needed
        if 'opennow' in kwargs:
            params['opennow'] = ''

        # optional, don't send unless needed
        if 'pagetoken' in kwargs:
            params['pagetoken'] = kwargs['pagetoken']

        return params

    def _parse_results(self, json_response):
        super(PlacesQuery, self)._parse_results(json_response)

        # store page token if any
        self.next_page_token = json_response.get('next_page_token')

    def _adapt_results(self, json_response):
        return json_response['results']

    @property
    def query(self):
        return self.location


if __name__ == '__main__':
    g = PlacesQuery('rail station, Ottawa')
    g.debug()
