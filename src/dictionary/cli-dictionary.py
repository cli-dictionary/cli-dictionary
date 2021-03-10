#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import requests
import argparse
import threading
from random import randint
from language import language
#from src.dictionary import language
#from ..anki import anki


def get_parser():
    parser = argparse.ArgumentParser(
        prog='cli-dictionary', description='welcome to cli-dictionary, never use a browser again to get a word meaning ;)')
    parser.add_argument('word', type=str, help='the word to be searched.')
    parser.add_argument(
        'lang', type=str, help='the language of the requested word.')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 2.3.1')
    parser.add_argument('-s', '--synonyms', action='store_true',
                        help='display the synonyms of the requested word.')
    parser.add_argument('-e', '--examples', action='store_true',
                        help='display a phrase using the requested word.')

    group_anki = parser.add_argument_group('Anki-Flashcards')
    group_anki.add_argument(
        '--profile', help='select the profile', type=str)
    group_anki.add_argument(
        '--card', help='select the type of card', choices=['basic', 'basic-reverse', 'cloze'])

    return parser


def main(word, lang, *args):
    word = word.encode('utf-8')

    sy = ''  # synonyms
    ex = ''  # examples
    Anki = {}

    for arg in args:
        sy = arg[0]['synonyms']
        ex = arg[0]['examples']

        Anki = {
            'profile': arg[0]['profile'],
            'card': arg[0]['card']
        }

        break

    # upper() because in list of language.py all the abbreviation are uppercased.
    lang = lang.upper()

    if lang in language:
        url = language[lang] + word.decode('utf-8')

        meaning(url)

        if sy:
            synonyms(url)
        if ex:
            examples(url)

    else:
        print("""
           select a valid language:
           en <english> | pt <portuguese>
           hi <hindi>   | es <spanish>
           fr <french>  | ja <japanese>
           ru <russian> | de <german>
           it <italian> | ko <korean>
           zh <chinese> | ar <arabic>
           tr <turkish>
       """)

    if Anki['profile'] == None and Anki['card'] == None:
        pass
    else:
        get_anki(profile=Anki['profile'], card=Anki['card'], lang=lang, word=word.decode('utf-8'), meaning=WORD_MEANING)


def meaning(url):
    header = {
        "Accept": "charset=utf-8"
    }

    response = requests.request('GET', url, headers=header)

    data = json.loads(response.text.encode('utf-8'))

    for obj in data:

        meanings = obj['meanings'][0]['definitions']

        print('DEFINITIONS ----------------------')

        i = 0

        for m in meanings:
            i += 1
            print(f'{str(i)}. {m["definition"]}')


def examples(url):
    header = {
        "Accept": "charset=utf-8"
    }

    response = requests.request('GET', url, headers=header)

    data = json.loads(response.text.encode('utf-8'))

    for obj in data:

        examples = obj['meanings'][0]['definitions']

        print('EXAMPLES ----------------------')

        i = 0

        for e in examples:
            i += 1
            print(f'{str(i)}. {e["example"]}')


def synonyms(url):
    try:
        header = {
            "Accept": "charset=utf-8"
        }

        response = requests.request('GET', url, headers=header)

        data = json.loads(response.text.encode('utf-8'))

        for obj in data:

            synonyms = obj['meanings'][0]['definitions']

            print('SYNONYMS ----------------------')

            i = 0

            for s in synonyms:
                array_synonyms = s['synonyms']
                for s_array in array_synonyms:
                    i += 1
                    if i == 11:
                        return
                    else:
                        print(f'{str(i)}. {s_array}')
    except KeyError:
        return



def get_anki(**kwargs):
    print('ANKI LOG ----------------------')
    # anki
    profile = kwargs.get('profile')
    card = kwargs.get('card')

    # dictionary info
    lang = kwargs.get('lang')
    word = kwargs.get('word')
    meaning = kwargs.get('meaning')

    len_meaning = len(meaning) - 1
    rand_number = randint(0, len_meaning)

    create_anki(lang=lang)

    if profile == None:
        print(f'creating card type: "{card}", for current user.')
        anki.createCard(card, lang, word, meaning[0])
        return
    elif card == None:
        print('Oops! You should select a card type!')
        return
    else:
        thread = threading.Thread(target=anki.changeProfile(profile))
        thread.start()

        # wait until change the profile
        thread.join()

        # check if this new profile have the deck and subdecks
        create_anki(lang=lang)

        anki.createCard(card, lang, word, meaning[rand_number])
        print(
            f'changing profile to "{profile}" and adding card type: "{card}".')
        return


def create_anki(**kwargs):
    if anki.IsDeckCreated() == False:
        anki.createDeck()

    elif anki.IsSubDeckCreated(kwargs.get('lang')) == False:
        anki.createSubDeck(kwargs.get('lang'))


if __name__ == '__main__':
    parser = get_parser()
    args = vars(parser.parse_args())
    main(sys.argv[1], sys.argv[2], [args])
    #main('vie', 'fr', [args])
