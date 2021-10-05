import json
def pprint(adict):
    """
    Pretty printing of dictionaries
    """
    print(json.dumps(adict, indent=4))
def get_coordinates(api_response):
    """
    A function that retrieves longitude
    and latitude of a location
    """
    location = api_response[0]["geometry"]["location"]
    return location