import json

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)