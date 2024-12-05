import requests
from api_keys import api_key_list


class RequestFMP:
    """
    Class for requesting data from the Financial Modeling Prep API
    """
    active_api_keys = api_key_list
    inactive_api_keys = []

    def __init__(self):
        self.api_key = self.active_api_keys[0]

    def arrange_api_keys(self, inactive_api_key):
        self.active_api_keys.remove(inactive_api_key)
        self.inactive_api_keys.append(inactive_api_key)

    def get_api_url(self, url):
        return f"{url}?apikey={self.api_key}"

    def get_api_result(self, url):
        api_url = self.get_api_url(url)
        response = requests.get(api_url)
        return response.json()