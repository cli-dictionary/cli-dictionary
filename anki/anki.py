#!/usr/bin/python3

import requests
import json

URL = 'http://localhost:8765'


def action_post(action):
    return requests.post(URL, json=action)


def IsDeckCreated():
    req = {
        'action': 'deckNames',
        'version': 6
    }

    r = action_post(req)

    formattedJson = json.dumps(r.json())

    if 'Cli-dictionary' in formattedJson:
        return True
    else:
        return False


def IsSubDeckCreated(lang):
    req = {
        'action': 'deckNames',
        'version': 6
    }

    r = action_post(req)

    formattedJson = json.dumps(r.json())

    if f'Cli-dictionary::{lang}' in formattedJson:
        return True
    else:
        return False


def changeProfile(profile_name):
    json = {
        "action": "loadProfile",
        "params": {
            "name": profile_name
        },
        "version": 6
    }

    action_post(json)


def createDeck():
    json = {
        'action': 'createDeck',
        'version': 6,
        'params': {
            'deck': 'Cli-dictionary'
        }
    }

    action_post(json)


def createSubDeck(lang):
    json = {
        'action': 'createDeck',
        'version': 6,
        'params': {
            'deck': f'Cli-dictionary::{lang}'
        }
    }

    action_post(json)


def createCard(card_type, lang, word, meaning):
    if card_type in ['basic', 'basic-reverse']:
        json = {
            'action': 'addNote',
            'version': 6,
            'params': {
                'note': {
                    'deckName': f'Cli-dictionary::{lang}',
                    # Basic, Basic (and reversed card), Cloze
                    'modelName': 'Basic' if card_type == 'basic' else 'Basic (and reversed card)',
                    'fields': {
                        'Front': word,
                        'Back': meaning
                    }
                }
            }
        }

    elif card_type == 'cloze':
        json = {
            'action': 'addNote',
            'version': 6,
            'params': {
                'note': {
                    'deckName': f'Cli-dictionary::{lang}',
                    # Basic, Basic (and reversed card), Cloze
                    'modelName': 'Cloze',
                    'fields': {
                        'Text': f'test {{c1::{word}}}',
                        'Extra': meaning
                    }
                }
            }
        }

    else:
        print('Please insert a valid type: ')
        print(''' 
            List of types:
            - basic
            - basic-reverse
            - cloze
        ''')

    action_post(json)
