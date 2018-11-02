from __future__ import absolute_import

from geocoder.geonames import GeonamesQuery, GeonamesResult
from geocoder.location import Location


class GeonamesTimezoneResult(GeonamesResult):
    """ Get timezone information for given lat,lng"""

    @property
    def sunrise(self):
        return self.raw.get('sunrise')

    @property
    def gmt_offset(self):
        return self.raw.get('gmtOffset')

    @property
    def raw_offset(self):
        return self.raw.get('rawOffset')

    @property
    def dst_offest(self):
        return self.raw.get('dstOffset')

    @property
    def sunset(self):
        return self.raw.get('sunset')

    @property
    def timezone_id(self):
        return self.raw.get('timezoneId')

    @property
    def time(self):
        return self.raw.get('time')


class GeonamesTimezone(GeonamesQuery):
    """ Details:
        http://api.geonames.org/timezoneJSON?lat=47.01&lng=10.2
    """

    provider = 'geonames'
    method = 'timezone'

    _URL = 'http://api.geonames.org/timezoneJSON'
    _RESULT_CLASS = GeonamesTimezoneResult

    def _build_params(self, location, provider_key, **kwargs):
        """Will be overridden according to the targetted web service"""
        location = Location(location)
        return {
            'lat': location.latitude,
            'lng': location.longitude,
            'username': provider_key
        }

    def _adapt_results(self, json_response):
        # the returned JSON contains the object.
        # Need to wrap it into an array
        return [json_response]
