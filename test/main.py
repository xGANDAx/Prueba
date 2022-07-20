# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
from multiprocessing.sharedctypes import Value
from tkinter import W
from turtle import back
from colorama import init, Back
import requests

init()

def run():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    with open('json-joker.json', 'w') as dataFile:
        json.dump(r.json(), dataFile, indent=4)
    with open('json-joker.json') as dataFile:
        data = json.load(dataFile)
        print(Back.BLUE,data)     
        with open('joker.txt','w') as textFile:
            textFile.write(data["value"])
    return 1
