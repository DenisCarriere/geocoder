#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import

# geocoder imports
from geocoder.base import Base


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

    def __init__(self, location, **kwargs):
        # city, state, zip
        city = kwargs.get('city', '')
        state = kwargs.get('state', '')
        zipcode = kwargs.get('zipcode', '')
        if not bool(city and state and zipcode):
            raise ValueError("Provide city, state and zipcode")

        # API key
        key = kwargs.get('key', '')
        if not key:
            raise ValueError("Provide key")

        # note we do string formatting b/c apparently tamu endpoint is
        # sensitive to the order of parameters.
        self.url = 'https://geoservices.tamu.edu/Services/Geocode/WebService/'\
                   'GeocoderWebServiceHttpNonParsed_V04_01.aspx?'\
                   'streetAddress={addr}'\
                   '&city={city}'\
                   '&state={state}'\
                   '&zip={zipcode}'\
                   '&apikey={key}'\
                   '&format=json'\
                   '&census=true'\
                   '&censusYear=1990|2000|2010'\
                   '&notStore=false'\
                   '&verbose=true'\
                   '&version=4.01'.format(addr=location, **kwargs)

        self.location = location
        self.key = kwargs['key']
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

        if self.parse['CensusValues']:
            self._build_tree(self.parse.get('CensusValues'))

    @property
    def lat(self):
        geo = self.parse.get('OutputGeocode')
        if geo:
            lat = geo.get('Latitude')
            if lat:
                return float(lat)

    @property
    def lng(self):
        geo = self.parse.get('OutputGeocode')
        if geo:
            lng = geo.get('Longitude')
            if lng:
                return float(lng)

    @property
    def quality(self):
        geo = self.parse.get('OutputGeocode')
        if geo:
            return geo.get('MatchedLocationType')

    @property
    def accuracy(self):
        geo = self.parse.get('OutputGeocode')
        if geo:
            return geo.get('FeatureMatchingGeographyType')

    @property
    def confidence(self):
        geo = self.parse.get('OutputGeocode')
        if geo:
            return geo.get('MatchScore')

    @property
    def housenumber(self):
        matched_addr = self.parse.get('MatchedAddress')
        if matched_addr:
            return matched_addr.get('Number')

    @property
    def street(self):
        matched_addr = self.parse.get('MatchedAddress')
        if matched_addr:
            return ' '.join(
                [matched_addr.get('Name'), matched_addr.get('Suffix')])

    @property
    def address(self):
        return self.parse.get('InputAddress').get('StreetAddress')

    @property
    def city(self):
        matched_addr = self.parse.get('MatchedAddress')
        if matched_addr:
            return matched_addr.get('City')

    @property
    def state(self):
        matched_addr = self.parse.get('MatchedAddress')
        if matched_addr:
            return matched_addr.get('State')

    @property
    def postal(self):
        matched_addr = self.parse.get('MatchedAddress')
        if matched_addr:
            return matched_addr.get('Zip')

    @property
    def census_tract(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusTract')

    @property
    def census_block(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusBlock')

    @property
    def census_msa_fips(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusMsaFips')

    @property
    def census_mcd_fips(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusMcdFips')

    @property
    def census_metdiv_fips(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusMetDivFips')

    @property
    def census_place_fips(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusPlaceFips')

    @property
    def census_cbsa_fips(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusCbsaFips')

    @property
    def census_state_fips(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusStateFips')

    @property
    def census_county_fips(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusCountyFips')

    @property
    def census_year(self):
        census = self.parse.get('CensusValues')
        if census:
            return census[0].values()[0].get('CensusYear')


if __name__ == '__main__':
    g = Tamu(
        '595 Market Street',
        city="San Francisco",
        state="CA",
        zipcode="94105",
        key="demo")

    g.debug()
