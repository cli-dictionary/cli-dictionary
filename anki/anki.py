#!/usr/bin/python3

import requests

# default url
URL = 'http://localhost:8765'


def teste():
    r = requests.post(URL, json=IsDeckCreated())
    print(r.json())


def IsDeckCreated():
    json = {
        'action': 'deckNames',
        'version': 6
    }

    return json


def changeProfile(name):
    json = {
        "action": "loadProfile",
        "params": {
            "name": name
        },
        "version": 6
    }
    return json


def createDeck():
    json = {
        'action': 'createDeck',
        'version': 6,
        'params': {
            'deck': 'Cli-dictionary'
        }
    }

    return json


def createSubDeck(lang):
    json = {
        'action': 'createDeck',
        'version': 6,
        'params': {
            'deck': f'Cli-dictionary::{lang}'
        }
    }

    return json


def createCards():
    json = {
        'action': 'addNote',
        'version': 6,
        'params': {
            'note': {
                'deckName': 'Cli-dictionary',
                'modelName': 'Basic',  # "Basic" or "Basic (and reversed card)"
                'fields': {
                    'Front': 'life',
                    'Back': 'meaning of life'
                }
            }
        }
    }

    return json


if __name__ == '__main__':
    teste()
