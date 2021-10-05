"""
This piece of code reads temperature data from
a website and creates a map
"""
import os
import googlemaps
import utils
API_KEY = os.getenv("GOOGLE_GEOCODING_API")
class CurrentTemperature:
    """
    Current temperature class
    """
    def __init__(self, *args):
        """
        We want the constructor class to allow
        for a list of places whose current
        temperature we want to know
        """
        self.places = args
    def raise_error_if_args_empty(self):
        """
        Args should not be empty
        """
        if self.places == ():
            raise Exception("At least one location should be provided at __init__")
    def raise_error_if_args_not_strings(self):
        """
        Error if arguments not list of strings
        """
        for item in self.places:
            if not isinstance(item, str):
                raise Exception(f'{item} is not a string')
    def __repr__(self):
        """
        Class representation
        """
        self.raise_error_if_args_empty()
        self.raise_error_if_args_not_strings()
        my_places = ""
        for place in self.places:
            my_places = my_places + place + " "
        return my_places.strip()
    def get_geo_codes(self):
        """
        Here we need to get lon and lat
        for each of the places given
        """
        geocodes = {}
        if len(self.places) == 0:
            self.__repr__()
        else:
            for place in self.places:
                api_response = googlemaps.Client(API_KEY).geocode(place)
                geocodes[place] = utils.get_coordinates(api_response)
        print(geocodes)
        return geocodes
    