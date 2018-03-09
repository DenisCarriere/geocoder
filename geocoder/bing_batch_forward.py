#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import, print_function
from geocoder.bing_batch import BingBatchResult, BingBatch


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


class BingBatchForward(BingBatch):

    method = 'batch'

    _RESULT_CLASS = BingBatchForwardResult


if __name__ == '__main__':
    g = BingBatchForward(['Denver,CO', 'Boulder,CO'], key=None)
    g.debug()
