#!/usr/bin/env python
# coding: utf8
"""
Unit tests for cli functionality
"""

# --- Imports

import subprocess

import geocoder

# --- Constants

_CLI_EX = './geocoder/cli.py'  # CLI executable path


us_address = '595 Market St'
us_city = 'San Francisco'
us_state = 'CA'
us_zipcode = '94105'

location = ' '.join([us_address, us_city, us_state, us_zipcode])


# --- CLI tests.  Each shell call should have return code 0 if successfull.

def test_cli_default():
    # default provider cli test
    assert not subprocess.call(['python', _CLI_EX, location])
