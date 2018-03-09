#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import, print_function
from geocoder.bing_batch import BingBatch, BingBatchResult
import io
import csv


class BingBatchReverseResult(BingBatchResult):

    @property
    def address(self):
        coord = self._content
        if coord:
            return coord[0]

    @property
    def city(self):
        coord = self._content
        if coord:
            return coord[1]

    @property
    def postal(self):
        coord = self._content
        if coord:
            return coord[2]

    @property
    def state(self):
        coord = self._content
        if coord:
            return coord[3]

    @property
    def country(self):
        coord = self._content
        if coord:
            return coord[4]

    @property
    def ok(self):
        return bool(self._content)


class BingBatchReverse(BingBatch):

    method = 'batch_reverse'

    _RESULT_CLASS = BingBatchReverseResult

    def generate_batch(self, locations):
        out = io.BytesIO()
        writer = csv.writer(out)
        writer.writerow([
            'Id',
            'ReverseGeocodeRequest/Location/Latitude',
            'ReverseGeocodeRequest/Location/Longitude',
            'GeocodeResponse/Address/FormattedAddress',
            'GeocodeResponse/Address/Locality',
            'GeocodeResponse/Address/PostalCode',
            'GeocodeResponse/Address/AdminDistrict',
            'GeocodeResponse/Address/CountryRegion',
        ])

        for idx, location in enumerate(locations):
            writer.writerow([idx, location[0], location[1], None, None, None, None, None])

        return "Bing Spatial Data Services, 2.0\n{}".format(out.getvalue())

    def _adapt_results(self, response):
        result = io.BytesIO(response)
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
    g = BingBatchReverse((40.7943, -73.970859), (48.845580, 2.321807), key=None)
    g.debug()
