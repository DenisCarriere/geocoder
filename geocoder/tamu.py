#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import
from geocoder.base import Base
from geocoder.keys import tamu_key


class Tamu(Base):
    """
    TAMU Geocoding Services
    =======================

    Params
    ------
    :param location: The street address of the location you want geocoded.
    :param city: The city of the location to geocode.
    :param state: The state of the location to geocode.
    :param zipcode: The zipcode of the location to geocode.
    :param key: The API key (use API key "demo" for testing).

    API Reference
    -------------
    https://geoservices.tamu.edu/Services/Geocode/WebService
    """
    provider = 'tamu'
    method = 'geocode'

    def __init__(
            self, location, censusYears=('1990', '2000', '2010'), **kwargs):

        # city, state, zip
        city = kwargs.get('city', '')
        state = kwargs.get('state', '')
        zipcode = kwargs.get('zipcode', '')
        if not bool(city and state and zipcode):
            raise ValueError("Provide city, state and zipcode")

        # API key
        key = kwargs.get('key', tamu_key)
        if not key:
            raise ValueError("Provide key")
        self.key = key

        self.location = location
        self.url = 'https://geoservices.tamu.edu/Services/Geocode/WebService' \
                   '/GeocoderWebServiceHttpNonParsed_V04_01.aspx'
        self.params = {
            'streetAddress': location,
            'city': city,
            'state': state,
            'zip': zipcode,
            'apikey': key,
            'format': 'json',
            'census': 'true',
            'censusYear': '|'.join(censusYears),
            'notStore': 'false',
            'verbose': 'true',
            'version': '4.01'
        }
        self._initialize(**kwargs)

    def _catch_errors(self):
        exception_occured = self.parse.get('ExceptionOccured')
        status_code = self.parse.get('QueryStatusCodeValue')
        exception = self.parse.get('Exception')

        if (exception_occured == 'True' or
                status_code != "200" or
                exception):

            self.error = exception

        if status_code == "401" or status_code == "470":
            self.error = \
                "Tamu returned status_code {0}.  Is API key {1} valid?".\
                format(status_code, self.key)
#            raise Exception(self.error)

    def _exceptions(self):
        # Build initial Tree with results
        if self.parse['OutputGeocodes']:
            self._build_tree(self.parse.get('OutputGeocodes')[0])
            self._build_tree(self.parse.get('OutputGeocode'))
            self._build_tree(self.parse.get('ReferenceFeature'))

        if self.parse['CensusValues']:
            self._build_tree(self.parse.get('CensusValues')[0]['CensusValue1'])

    @property
    def lat(self):
        lat = self.parse.get('Latitude')
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = self.parse.get('Longitude')
        if lng:
            return float(lng)

    @property
    def quality(self):
        return self.parse.get('MatchedLocationType')

    @property
    def accuracy(self):
        return self.parse.get('FeatureMatchingGeographyType')

    @property
    def confidence(self):
        return self.parse.get('MatchScore')

    @property
    def housenumber(self):
        return self.parse.get('Number')

    @property
    def street(self):
        name = self.parse.get('Name', '')
        suffix = self.parse.get('Suffix', '')
        return ' '.join([name, suffix]).strip()

    @property
    def address(self):
        return ' '.join([
            self.parse.get('Number', ''),
            self.parse.get('Name', ''),
            self.parse.get('Suffix', ''),
            self.parse.get('City', ''),
            self.parse.get('State', ''),
            self.parse.get('Zip', '')])

    @property
    def city(self):
        return self.parse.get('City')

    @property
    def state(self):
        return self.parse.get('State')

    @property
    def postal(self):
        return self.parse.get('Zip')

    @property
    def census_tract(self):
        return self.parse.get('CensusTract')

    @property
    def census_block(self):
        return self.parse.get('CensusBlock')

    @property
    def census_msa_fips(self):
        return self.parse.get('CensusMsaFips')

    @property
    def census_mcd_fips(self):
        return self.parse.get('CensusMcdFips')

    @property
    def census_metdiv_fips(self):
        return self.parse.get('CensusMetDivFips')

    @property
    def census_place_fips(self):
        return self.parse.get('CensusPlaceFips')

    @property
    def census_cbsa_fips(self):
        return self.parse.get('CensusCbsaFips')

    @property
    def census_state_fips(self):
        return self.parse.get('CensusStateFips')

    @property
    def census_county_fips(self):
        return self.parse.get('CensusCountyFips')

    @property
    def census_year(self):
        return self.parse.get('CensusYear')


if __name__ == '__main__':
    g = Tamu(
        '595 Market Street',
        city="San Francisco",
        state="CA",
        zipcode="94105")

    g.debug()
