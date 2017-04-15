#!/usr/bin/python
# coding: utf8

import pytest
from requests.packages.urllib3.exceptions import TimeoutError
import geocoder


us_address = '595 Market St'
us_city = 'San Francisco'
us_state = 'CA'
us_zipcode = '94105'

# @pytest.mark.xfail(raises=TimeoutError)
# def test_uscensus():
#     g = geocoder.uscensus(' '.join([us_address, us_city, us_state, us_zipcode]))
#     assert g.ok
#     assert g.city == us_city.upper()


# @pytest.mark.xfail(raises=TimeoutError)
# def test_uscensus_reverse():
#     g = geocoder.uscensus((38.904722, -77.016389), method='reverse')
#     assert g.ok
