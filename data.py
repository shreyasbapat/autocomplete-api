from flask import json


class Data:
    def __init__(self, data):
        self.data = data

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

