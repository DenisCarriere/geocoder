#!/usr/bin/python
# coding: utf8
from __future__ import absolute_import
from geocoder.base import OneResult, MultipleResultsQuery

import logging
import io
import csv
import sys
import requests


PY2 = sys.version_info < (3, 0)
csv_io = io.BytesIO if PY2 else io.StringIO
csv_encode = (lambda input: input) if PY2 else (lambda input: input.encode('utf-8'))
csv_decode = (lambda input: input) if PY2 else (lambda input: input.decode('utf-8'))

LOGGER = logging.getLogger(__name__)


class USCensusBatchResult(OneResult):

    def __init__(self, content):
        self._content = content

        if self._content:
            self._coordinates = tuple(float(pos) for pos in content[1].split(','))

        # proceed with super.__init__
        super(USCensusBatchResult, self).__init__(content)

    @property
    def lat(self):
        if self._content:
            return self._coordinates[1]

    @property
    def lng(self):
        if self._content:
            return self._coordinates[0]

    @property
    def address(self):
        if self._content:
            return self._content[0]


class USCensusBatch(MultipleResultsQuery):
    """
    US Census Geocoder REST Services
    =======================
    The Census Geocoder is an address look-up tool that converts your address to an approximate coordinate (latitude/longitude) and returns information about the address range that includes the address and the census geography the address is within. The geocoder is available as a web interface and as an API (Representational State Transfer - REST - web-based service).

    API Reference
    -------------
    https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html

    """
    provider = 'uscensus'
    method = 'geocode'

    _URL = 'https://geocoding.geo.census.gov/geocoder/locations/addressbatch'
    _RESULT_CLASS = USCensusBatchResult
    _KEY_MANDATORY = False

    def generate_batch(self, locations):
        out = csv_io()
        writer = csv.writer(out)

        for idx, address in enumerate(locations):
            writer.writerow([idx, address, None, None, None])

        return csv_encode(out.getvalue())

    def _build_params(self, locations, provider_key, **kwargs):
        self.batch = self.generate_batch(locations)
        self.locations_length = len(locations)
        self.timeout = int(kwargs.get('timeout', '1800'))  # 30mn timeout, us census can be really slow with big batches
        self.benchmark = str(kwargs.get('benchmark', 4))

        return {
            'benchmark': (None, self.benchmark),
            'addressFile': ('addresses.csv', self.batch)
        }

    def _connect(self):
        self.status_code = 'Unknown'

        try:
            self.response = response = self.session.post(
                self.url,
                files=self.params,
                headers=self.headers,
                timeout=self.timeout,
                proxies=self.proxies
            )

            # check that response is ok
            self.status_code = response.status_code
            response.raise_for_status()

            return response.content

        except (requests.exceptions.RequestException, LookupError) as err:
            # store real status code and error
            self.error = u'ERROR - {}'.format(str(err))
            LOGGER.error("Status code %s from %s: %s",
                         self.status_code, self.url, self.error)

        return False

    def _adapt_results(self, response):
        result = csv_io(csv_decode(response))

        rows = {}
        for row in csv.reader(result):
            if row[2] == 'Match':
                rows[row[0]] = [row[4], row[5]]

        return rows

    def _parse_results(self, response):
        rows = self._adapt_results(response)

        # re looping through the results to give them back in their original order
        for idx in range(0, self.locations_length):
            self.add(self.one_result(rows.get(str(idx), None)))

        self.current_result = len(self) > 0 and self[0]


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    g = USCensusBatch(['4650 Silver Hill Road, Suitland, MD 20746', '42 Chapel Street, New Haven'], benchmark=9)
    g.debug()
