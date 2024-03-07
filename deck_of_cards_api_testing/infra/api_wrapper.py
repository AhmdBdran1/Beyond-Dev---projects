import json
import os

import requests


def read_config(file_path):  # open the config file for read
    script_directory = os.path.dirname(os.path.realpath(__file__))
    absolute_path = os.path.join(script_directory, file_path)
    with open(absolute_path, 'r') as f:
        config = json.load(f)
    return config


class APIWrapper:

    def __init__(self):
        self.response = None
        self.my_request = requests
        config_file = '../config.json'
        config = read_config(config_file)
        self.url = config['url']

    def api_get_request(self, endpoints):
        self.response = self.my_request.get(self.url + endpoints)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
