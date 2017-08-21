from __future__ import absolute_import

from geocoder.geonames import GeonamesQuery, GeonamesResult


class GeonamesFullResult(GeonamesResult):
    """ Get more information for given geonames_id, e.g timzone and administrative hierarchy"""

    @property
    def continent(self):
        return self.raw.get('continentCode', "")

    @property
    def country_geonames_id(self):
        return self.raw.get('countryId', 0)

    @property
    def state_geonames_id(self):
        return self.raw.get('adminId1', 0)

    @property
    def admin2(self):
        return self.raw.get('adminName2', "")

    @property
    def admin2_geonames_id(self):
        return self.raw.get('adminId2', "")

    @property
    def admin3(self):
        return self.raw.get('adminName3', "")

    @property
    def admin3_geonames_id(self):
        return self.raw.get('adminId3', "")

    @property
    def admin4(self):
        return self.raw.get('adminName4', "")

    @property
    def admin4_geonames_id(self):
        return self.raw.get('adminId4', "")

    @property
    def admin5(self):
        return self.raw.get('adminName5', "")

    @property
    def admin5_geonames_id(self):
        return self.raw.get('adminId5', "")

    @property
    def srtm3(self):
        return self.raw.get('srtm3', 0)

    @property
    def wikipedia(self):
        return self.raw.get('wikipediaURL', "")

    @property
    def timeZoneId(self):
        timezone = self.raw.get('timezone')
        if timezone:
            return timezone.get('timeZoneId')

    @property
    def timeZoneName(self):
        timezone = self.raw.get('timezone')
        if timezone:
            return timezone.get('timeZoneId')

    @property
    def rawOffset(self):
        timezone = self.raw.get('timezone')
        if timezone:
            return timezone.get('gmtOffset')

    @property
    def dstOffset(self):
        timezone = self.raw.get('timezone')
        if timezone:
            return timezone.get('dstOffset')

    @property
    def bbox(self):
        bbox = self.raw.get('bbox', {})
        south = bbox.get('south')
        west = bbox.get('west')
        north = bbox.get('north')
        east = bbox.get('east')
        return self._get_bbox(south, west, north, east)


class GeonamesDetails(GeonamesQuery):
    """ Details:
        http://api.geonames.org/getJSON?geonameId=6094817&style=full
    """

    provider = 'geonames'
    method = 'details'

    _URL = 'http://api.geonames.org/getJSON'
    _RESULT_CLASS = GeonamesFullResult

    def _build_params(self, location, provider_key, **kwargs):
        """Will be overridden according to the targetted web service"""
        return {
            'geonameId': location,
            'username': provider_key,
            'style': 'full'
        }

    def _adapt_results(self, json_response):
        # the returned JSON contains the object.
        # Need to wrap it into an array
        return [json_response]


if __name__ == '__main__':
    c = GeonamesDetails(6094817)
    c.debug()
