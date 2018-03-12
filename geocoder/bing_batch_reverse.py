#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import, print_function
from geocoder.bing_batch import BingBatch, BingBatchResult

import io
import csv
import sys

PY2 = sys.version_info < (3, 0)
csv_io = io.BytesIO if PY2 else io.StringIO
csv_encode = (lambda input: input) if PY2 else (lambda input: input.encode('utf-8'))
csv_decode = (lambda input: input) if PY2 else (lambda input: input.decode('utf-8'))


class BingBatchReverseResult(BingBatchResult):

    @property
    def address(self):
        address = self._content
        if address:
            return address[0]

    @property
    def city(self):
        city = self._content
        if city:
            return city[1]

    @property
    def postal(self):
        postal = self._content
        if postal:
            return postal[2]

    @property
    def state(self):
        state = self._content
        if state:
            return state[3]

    @property
    def country(self):
        country = self._content
        if country:
            return country[4]

    @property
    def ok(self):
        return bool(self._content)

    def debug(self, verbose=True):
        with csv_io() as output:
            print('\n', file=output)
            print('Bing Batch result\n', file=output)
            print('-----------\n', file=output)
            print(self._content, file=output)

            if verbose:
                print(output.getvalue())

            return [None, None]


class BingBatchReverse(BingBatch):

    method = 'batch_reverse'
    _RESULT_CLASS = BingBatchReverseResult

    def generate_batch(self, locations):
        out = csv_io()
        writer = csv.writer(out)
        writer.writerow([
            'Id',
            'ReverseGeocodeRequest/Location/Latitude',
            'ReverseGeocodeRequest/Location/Longitude',
            'GeocodeResponse/Address/FormattedAddress',
            'GeocodeResponse/Address/Locality',
            'GeocodeResponse/Address/PostalCode',
            'GeocodeResponse/Address/AdminDistrict',
            'GeocodeResponse/Address/CountryRegion'
        ])

        for idx, location in enumerate(locations):
            writer.writerow([idx, location[0], location[1], None, None, None, None, None])

        return csv_encode("Bing Spatial Data Services, 2.0\n{}".format(out.getvalue()))

    def _adapt_results(self, response):
        # print(type(response))
        result = csv_io(csv_decode(response))
        # Skipping first line with Bing header
        next(result)

        rows = {}
        for row in csv.DictReader(result):
            rows[row['Id']] = [
                row['GeocodeResponse/Address/FormattedAddress'],
                row['GeocodeResponse/Address/Locality'],
                row['GeocodeResponse/Address/PostalCode'],
                row['GeocodeResponse/Address/AdminDistrict'],
                row['GeocodeResponse/Address/CountryRegion']
            ]

        return rows


if __name__ == '__main__':
    g = BingBatchReverse([(40.7943, -73.970859), (48.845580, 2.321807)], key=None)
    g.debug()
