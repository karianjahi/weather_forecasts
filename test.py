"""
Testing the application
"""
import  unittest
from main import CurrentTemperature
class TestMain(unittest.TestCase):
    """
    Testing the main.py
    """
    def test_empty_args(self, class_repr=False):
        """
        args should have at least one member
        """
        obj = CurrentTemperature()
        with self.assertRaises(Exception) as context:
            if class_repr:
                print(obj)
            else:
                obj.raise_error_if_args_empty()
            self.assertTrue("Not a single location given " in context.exception)
    def test_non_strings(self, class_repr=False):
        """
        only lists of strings are allowed
        in our main class
        """
        obj = CurrentTemperature(25.1, 214.5, 194, {"spiced": "students"})
        with self.assertRaises(Exception) as context:
            if class_repr:
                print(obj)
            else:
                obj.raise_error_if_args_not_strings()
            self.assertTrue("Arguments must be lists of strings " in context.exception)
    def test_class_representation(self):
        """
        Test class representation
        """
        self.test_empty_args(class_repr=True)
        self.test_non_strings(class_repr=True)
        obj = CurrentTemperature("Berlin", "Stuttgart", "Flensburg")
        self.assertEqual(str(obj), "Berlin Stuttgart Flensburg")
    def test_get_geocodes(self):
        """
        Test geocode extraction from API
        """
        obj_with_args = CurrentTemperature("Berlin",
                                           "Stuttgart",
                                           "Dresden",
                                           "Karlsruhe",
                                           "Freiburg")
        places = ["Berlin", "Stuttgart", "Dresden", "Karlsruhe", "Freiburg"]
        lats = [52.5, 48.8, 51.1, 49.0, 48.0]
        lons = [13.4, 9.2, 13.7, 8.4, 7.8]
        geocode_dict = obj_with_args.get_geo_codes()
        for place, lon, lat in zip(places, lons, lats):
            self.assertEqual(round(geocode_dict[place]["lng"], 1), lon)
            self.assertEqual(round(geocode_dict[place]["lat"], 1), lat)
        obj_without_args = CurrentTemperature()
        with self.assertRaises(Exception) as context:
            obj_without_args.get_geo_codes()
            self.assertTrue("No argument(s)" in context.exception)
            