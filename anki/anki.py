#!/usr/bin/python3

import requests
import json

URL = 'http://localhost:8765'


def post_json(action):
    return requests.post(URL, json=action)


def IsDeckCreated():
    req = {
        'action': 'deckNames',
        'version': 6
    }

    r = post_json(req)

    formattedJson = json.dumps(r.json())

    if 'Cli-dictionary' in formattedJson:
        return True
    else:
        return False


def changeProfile(name):
    json = {
        "action": "loadProfile",
        "params": {
            "name": name
        },
        "version": 6
    }

    r = post_json(json)
    return print(r.json())


def createDeck():
    json = {
        'action': 'createDeck',
        'version': 6,
        'params': {
            'deck': 'Cli-dictionary'
        }
    }

    r = post_json(json)
    return print(r.json())


def createSubDeck(lang):
    json = {
        'action': 'createDeck',
        'version': 6,
        'params': {
            'deck': f'Cli-dictionary::{lang}'
        }
    }

    r = post_json(json)
    return print(r.json())


def createCards():
    json = {
        'action': 'addNote',
        'version': 6,
        'params': {
            'note': {
                'deckName': 'Cli-dictionary',
                # "Basic" or "Basic (and reversed card)"
                'modelName': 'Basic',
                'fields': {
                    'Front': 'life',
                    'Back': 'meaning of life'
                }
            }
        }
    }

    r = post_json(json)
    return print(r.json())


if __name__ == '__main__':
    IsDeckCreated()
