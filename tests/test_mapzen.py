# coding: utf8
import pytest

import geocoder

location = 'Ottawa'


def test_mapzen():
    with pytest.raises(DeprecationWarning) as e:
        g = geocoder.mapzen(location)


def test_mapzen_reverse():
    with pytest.raises(DeprecationWarning) as e:
        g = geocoder.mapzen("45.4049053 -75.7077965", method='reverse')


def test_multi_results():
    with pytest.raises(DeprecationWarning) as e:
        g = geocoder.mapzen(location, maxRows=3)
