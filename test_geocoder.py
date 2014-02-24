import geocoder
import unittest


class RequestsTestCase(unittest.TestCase):

    def test_entry_points(self):
        geocoder.ip
        geocoder.osm
        geocoder.bing
        geocoder.nokia
        geocoder.google
        geocoder.tomtom
        geocoder.reverse
        geocoder.mapquest
