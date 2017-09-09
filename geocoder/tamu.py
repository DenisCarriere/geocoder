#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

import logging

from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import tamu_key


class TamuResult(OneResult):

    def __init__(self, json_content):
        self.output_geocode = json_content.get('OutputGeocode', {})
        self.parsed_address = json_content.get('ParsedAddress', {})
        self.reference_feature = json_content.get('ReferenceFeature', {})
        self.census_value = json_content.get('CensusValues', [{}])[0].get('CensusValue1', {})
        super(TamuResult, self).__init__(json_content)

    @property
    def lat(self):
        lat = self.output_geocode.get('Latitude')
        if lat:
            return float(lat)

    @property
    def lng(self):
        lng = self.output_geocode.get('Longitude')
        if lng:
            return float(lng)

    @property
    def quality(self):
        return self.output_geocode.get('MatchedLocationType')

    @property
    def accuracy(self):
        return self.output_geocode.get('FeatureMatchingGeographyType')

    @property
    def confidence(self):
        return self.output_geocode.get('MatchScore')

    @property
    def housenumber(self):
        return self.parsed_address.get('Number')

    @property
    def street(self):
        name = self.parsed_address.get('Name', '')
        suffix = self.parsed_address.get('Suffix', '')
        return ' '.join([name, suffix]).strip()

    @property
    def address(self):
        return ' '.join([
            self.parsed_address.get('Number', ''),
            self.parsed_address.get('Name', ''),
            self.parsed_address.get('Suffix', ''),
            self.parsed_address.get('City', ''),
            self.parsed_address.get('State', ''),
            self.parsed_address.get('Zip', '')])

    @property
    def city(self):
        return self.parsed_address.get('City')

    @property
    def state(self):
        return self.parsed_address.get('State')

    @property
    def postal(self):
        return self.parsed_address.get('Zip')

    @property
    def census_tract(self):
        return self.census_value.get('CensusTract')

    @property
    def census_block(self):
        return self.census_value.get('CensusBlock')

    @property
    def census_msa_fips(self):
        return self.census_value.get('CensusMsaFips')

    @property
    def census_mcd_fips(self):
        return self.census_value.get('CensusMcdFips')

    @property
    def census_metdiv_fips(self):
        return self.census_value.get('CensusMetDivFips')

    @property
    def census_place_fips(self):
        return self.census_value.get('CensusPlaceFips')

    @property
    def census_cbsa_fips(self):
        return self.census_value.get('CensusCbsaFips')

    @property
    def census_state_fips(self):
        return self.census_value.get('CensusStateFips')

    @property
    def census_county_fips(self):
        return self.census_value.get('CensusCountyFips')

    @property
    def census_year(self):
        return self.census_value.get('CensusYear')


class TamuQuery(MultipleResultsQuery):
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
    CENSUSYEARS = ['1990', '2000', '2010']

    _URL = 'https://geoservices.tamu.edu/Services/Geocode/WebService' \
           '/GeocoderWebServiceHttpNonParsed_V04_01.aspx'
    _RESULT_CLASS = TamuResult
    _KEY = tamu_key

    def _build_params(self, location, provider_key, **kwargs):
        # city, state, zip
        city = kwargs.get('city', '')
        state = kwargs.get('state', '')
        zipcode = kwargs.get('zipcode', '')
        return {
            'streetAddress': location,
            'city': city,
            'state': state,
            'zip': zipcode,
            'apikey': provider_key,
            'format': 'json',
            'census': 'true',
            'censusYear': '|'.join(self.CENSUSYEARS),
            'notStore': 'false',
            'verbose': 'true',
            'version': '4.01'
        }

    def _catch_errors(self, json_response):
        exception_occured = json_response.get('ExceptionOccured')
        status_code = json_response.get('QueryStatusCodeValue')
        exception = json_response.get('Exception')

        if exception_occured == 'True' or status_code != '200' or exception:
            self.error = exception

        if status_code == '401' or status_code == '470':
            self.error = u'Tamu returned status_code {0}.  Is API key {1} valid?'.format(status_code, self.key)

        return self.error

    def _adapt_results(self, json_response):
        return json_response['OutputGeocodes']


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = TamuQuery(
        '595 Market Street',
        city='San Francisco',
        state='CA',
        zipcode='94105')

    g.debug()
