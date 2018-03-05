#!/usr/bin/python
# coding: utf8

from __future__ import absolute_import, print_function
from geocoder.base import OneResult, MultipleResultsQuery
from geocoder.keys import bing_key

import time
import io
import requests
import logging
import sys

PY2 = sys.version_info < (3, 0)
csv_io = io.BytesIO if PY2 else io.StringIO

LOGGER = logging.getLogger(__name__)


class BingBatchResult(OneResult):

    def __init__(self, content):
        self._content = content

    @property
    def lat(self):
        coord = self._content
        if coord:
            return coord[0]

    @property
    def lng(self):
        coord = self._content
        if coord:
            return coord[1]

    def debug(self, verbose=True):
        with csv_io() as output:
            print('\n', file=output)
            print('{} result\n'.format(self.__class__.__name__), file=output)
            print('-----------\n', file=output)
            print(self._content, file=output)

            if verbose:
                print(output.getvalue())

            return [None, None]


class BingBatch(MultipleResultsQuery):
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
    provider = 'bing'

    _URL = u'http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode'
    _BATCH_TIMEOUT = 60
    _BATCH_WAIT = 5

    _RESULT_CLASS = BingBatchResult
    _KEY = bing_key

    def extract_resource_id(self, response):
        for rs in response['resourceSets']:
            for resource in rs['resources']:
                if 'id' in resource:
                    return resource['id']

        raise LookupError('No job ID returned from Bing batch call')

    def is_job_done(self, job_id):
        url = u'http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/{}'.format(job_id)
        response = self.session.get(
            url,
            params={'key': self.provider_key},
            timeout=self.timeout,
            proxies=self.proxies
        )

        for rs in response.json()['resourceSets']:
            for resource in rs['resources']:
                if resource['id'] == job_id:
                    if resource['status'] == 'Aborted':
                        raise LookupError('Bing job aborted')
                    return resource['status'] == 'Completed'

        raise LookupError('Job ID not found in Bing answer - something is wrong')

    def get_job_result(self, job_id):
        url = u'http://spatial.virtualearth.net/REST/v1/Dataflows/Geocode/{}/output/succeeded'.format(job_id)
        response = self.session.get(
            url,
            params={'key': self.provider_key},
            timeout=self.timeout,
            proxies=self.proxies
        )

        return response.content

    def _build_params(self, locations, provider_key, **kwargs):
        self.batch = self.generate_batch(locations)
        self.locations_length = len(locations)
        self.provider_key = provider_key
        self._BATCH_TIMEOUT = kwargs.get('timeout', 60)

        return {
            'input': 'csv',
            'key': provider_key
        }

    def _build_headers(self, provider_key, **kwargs):
        return {'Content-Type': 'text/plain'}

    def _connect(self):
        self.status_code = 'Unknown'

        try:
            self.response = response = self.session.post(
                self.url,
                data=self.batch,
                params=self.params,
                headers=self.headers,
                timeout=self.timeout,
                proxies=self.proxies
            )

            # check that response is ok
            self.status_code = response.status_code
            response.raise_for_status()

            # rely on json method to get non-empty well formatted JSON
            json_response = response.json()
            self.url = response.url
            LOGGER.info("Requested %s", self.url)

            # get the resource/job id
            resource_id = self.extract_resource_id(json_response)
            elapsed = 0

            # try for _BATCH_TIMEOUT seconds to retrieve the results of that job
            while (elapsed < self._BATCH_TIMEOUT):
                if self.is_job_done(resource_id):
                    return self.get_job_result(resource_id)

                elapsed = elapsed + self._BATCH_WAIT
                time.sleep(self._BATCH_WAIT)

            LOGGER.error("Job was not finished in time.")

        except (requests.exceptions.RequestException, LookupError) as err:
            # store real status code and error
            self.error = u'ERROR - {}'.format(str(err))
            LOGGER.error("Status code %s from %s: %s",
                         self.status_code, self.url, self.error)

        return False

    def _parse_results(self, response):
        rows = self._adapt_results(response)

        # re looping through the results to give them back in their original order
        for idx in range(0, self.locations_length):
            self.add(self.one_result(rows.get(str(idx), None)))

        self.current_result = len(self) > 0 and self[0]
