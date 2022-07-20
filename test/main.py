# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests

def run():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    with open('json-joker.json', 'w') as dataFile:
        json.dump(r.json(), dataFile, indent=4)
    return 1
