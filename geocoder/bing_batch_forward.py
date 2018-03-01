#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import, print_function
from geocoder.base import OneResult
from geocoder.bing_batch import BingBatch
from geocoder.keys import bing_key
from geocoder.location import Location
import time
import io
import csv
import requests
import logging

class BingBatchForwardResult(OneResult):

    def __init__(self, content):
        self._content = content

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
        with io.StringIO() as output:
            print(u'\n', file=output)
            print(u'Bing Batch result\n', file=output)
            print(u'-----------\n', file=output)
            print(unicode(str(self._content), "utf-8"), file=output)

            if verbose:
                print(output.getvalue())

            return [None, None]


class BingBatchForward(BingBatch):
    """
    Bing Maps REST Services
    =======================
    The Bing™ Maps REST Services Application Programming Interface (API)
    provides a Representational State Transfer (REST) interface to
    perform tasks such as creating a static map with pushpins, geocoding
    an address, retrieving imagery metadata, or creating a route.

    API Reference
    -------------
    http://msdn.microsoft.com/en-us/library/ff701714.aspx

    Dataflow Reference
    ------------------
    https://msdn.microsoft.com/en-us/library/ff701733.aspx

    """
    method = 'batch'

    _RESULT_CLASS = BingBatchForwardResult

    def generate_batch(self, addresses):
        out = io.BytesIO()
        writer = csv.writer(out)
        writer.writerow(['Id', 'GeocodeRequest/Query', 'GeocodeResponse/Point/Latitude', 'GeocodeResponse/Point/Longitude'])
        
        for idx, address in enumerate(addresses):
            writer.writerow([idx, address, None, None])
        
        return "Bing Spatial Data Services, 2.0\n{}".format(out.getvalue())

    def _adapt_results(self, response):
        result = io.BytesIO(response)
        # Skipping first line with Bing header
        next(result)

        rows = {}
        for row in csv.DictReader(result):
            rows[row['Id']] = [row['GeocodeResponse/Point/Latitude'], row['GeocodeResponse/Point/Longitude']]

        return rows

if __name__ == '__main__':
    g = BingBatchForward(['Denver,CO', 'Boulder,CO'], key=None)
    g.debug()
