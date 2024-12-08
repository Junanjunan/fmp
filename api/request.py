import requests
from functools import wraps
from api_keys import api_key_list


class RequestFMP:
    """
    Class for requesting data from the Financial Modeling Prep API
    """
    active_api_keys = api_key_list
    inactive_api_keys = []

    @staticmethod
    def try_with_all_api_keys():
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                while RequestFMP.active_api_keys:
                    try:
                        return func(self, *args, **kwargs)
                    except Exception as e:
                        if not "Limit Reach" in str(e):
                            raise e
                        print("The api_key is inactive. Change to the next api_key.")
                        current_key = RequestFMP.active_api_keys[0]
                        if current_key in RequestFMP.active_api_keys:
                            RequestFMP.active_api_keys.remove(current_key)
                            RequestFMP.inactive_api_keys.append(current_key)
                        if not RequestFMP.active_api_keys:
                            raise Exception("All API keys are inactive")
            return wrapper
        return decorator

    def arrange_api_keys(self, inactive_api_key):
        self.active_api_keys.remove(inactive_api_key)
        self.inactive_api_keys.append(inactive_api_key)

    def get_api_url(self, url, params):
        """params is a dictionary of parameters to add to the URL"""
        if params:
            queries = '&'.join([f"{key}={value}" for key, value in params.items()])
            return f"{url}?{queries}&apikey={RequestFMP.active_api_keys[0]}"
        else:
            return f"{url}?apikey={RequestFMP.active_api_keys[0]}"

    def get_api_result(self, url, params=None):
        api_url = self.get_api_url(url, params)
        response = requests.get(api_url)
        if 'Error Message' in response.json():
            raise Exception(response.json()['Error Message'])
        return response.json()