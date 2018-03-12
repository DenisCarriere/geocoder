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


class BingBatchForwardResult(BingBatchResult):

    @property
    def lat(self):
        coord = self._content
        if coord:
            return float(coord[0])

    @property
    def lng(self):
        coord = self._content
        if coord:
            return float(coord[1])

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


class BingBatchForward(BingBatch):
    method = 'batch'
    _RESULT_CLASS = BingBatchForwardResult

    def generate_batch(self, addresses):
        out = csv_io()
        writer = csv.writer(out)
        writer.writerow([
            'Id',
            'GeocodeRequest/Query',
            'GeocodeResponse/Point/Latitude',
            'GeocodeResponse/Point/Longitude'
        ])

        for idx, address in enumerate(addresses):
            writer.writerow([idx, address, None, None])

        return csv_encode("Bing Spatial Data Services, 2.0\n{}".format(out.getvalue()))

    def _adapt_results(self, response):
        result = csv_io(csv_decode(response))
        # Skipping first line with Bing header
        next(result)

        rows = {}
        for row in csv.DictReader(result):
            rows[row['Id']] = [row['GeocodeResponse/Point/Latitude'], row['GeocodeResponse/Point/Longitude']]

        return rows


if __name__ == '__main__':
    g = BingBatchForward(['Denver,CO', 'Boulder,CO'], key=None)
    g.debug()
