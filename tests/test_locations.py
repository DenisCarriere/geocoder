import pytest

from geocoder.location import BBox


class TestBBox(object):

    def test_factory_bounds_dict(self):
        bbox = BBox.factory({'southwest': [43.0, -80.5], 'northeast': ["43.6", "-80.0"]})
        assert bbox.latlng == [43.3, -80.25]

    def test_factory_bbox_dict(self):
        bbox = BBox.factory({'bbox': [-80.5, "43.0", "-80.0", 43.6]})
        assert bbox.latlng == [43.3, -80.25]

    def test_factory_latlng_dict(self):
        bbox = BBox.factory({'lat': 43.0, 'lng': "-80.0"})
        assert BBox.DEGREES_TOLERANCE == 0.5
        assert bbox.south == 42.5
        assert bbox.north == 43.5
        assert bbox.west == -80.5
        assert bbox.east == -79.5
        assert bbox.latlng == [43.0, -80.0]

    def test_factory_coordinates_dict(self):
        bbox = BBox.factory({'south': "43.0", 'west': -80.5, 'north': "43.6", 'east': -80.0})
        assert bbox.latlng == [43.3, -80.25]

    def test_factory_error_dict(self):
        with pytest.raises(ValueError):
            BBox.factory({'dummy': 43.0})

    def test_factory_bounds_list(self):
        bbox = BBox.factory([-80.5, "43.0", "-80.0", 43.6])
        assert bbox.latlng == [43.3, -80.25]

    def test_factory_latlng_list(self):
        bbox = BBox.factory(["-80.0", "43.0"])
        assert bbox.latlng == [-80.0, 43.0]

    def test_factory_error_list(self):
        with pytest.raises(ValueError):
            BBox.factory([1, 2, 3])

    def test_side_attributes(self):
        bbox = BBox.factory([-80.0, 43.0])
        assert bbox.lat == -80.0
        assert bbox.lng == 43.0
        assert bbox.latitude == -80.0
        assert bbox.longitude == 43.0
        assert bbox.latlng == [-80.0, 43.0]
        assert bbox.xy == [43.0, -80.0]

    def test_dict_output(self):
        bbox = BBox.factory({'bbox': [-80.5, 43.0, -80.0, 43.6]})
        assert bbox.as_dict == {
            'northeast': [43.6, -80.0],
            'southwest': [43.0, -80.5]
        }
