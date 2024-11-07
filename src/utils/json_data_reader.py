# scripts/json_data_reader.py

import json

class JSONDataReader:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = None
        self.load_json()

    def load_json(self):
        try:
            with open(self.json_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The JSON file '{self.json_file}' does not exist.")
        except json.JSONDecodeError:
            raise ValueError(f"The JSON file '{self.json_file}' is not valid JSON.")

    # we load the json file everytime we access the attribute, then if the attribute is updated in json file, we don't need to re-import this model to get the updated attribute
    def get(self, attribute_name):
        if self.data is None:
            self.load_json()
        return self.data.get(attribute_name, None)

    def get_nested(self, *keys):
        """Access nested dictionary keys."""
        data = self.data
        for key in keys:
            data = data.get(key, None)
            if data is None:
                return None
        return data

    # this allow to get the attribute from instance of this class, without calling the get method
    def __getattr__(self, item):
        if self.data is not None:
            return self.data.get(item)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{item}'")
