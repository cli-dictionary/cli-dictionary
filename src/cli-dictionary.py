#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys
import json
import requests
from args import Args
import threading
from argparse import ArgumentParser

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from anki import anki
from random import randint
from language import language

WORD_MEANING = []
WORD_EXAMPLES = []

# def get_parser():
# 	return Args()


def main(word, *args):
		word = word.encode('utf-8')

    # lang_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/default_lang.json'

    #with open(lang_file) as file:
		#    lang_json = json.load(file)
		#    default_lang = lang_json['default_lang']

		default_lang = 'en'

		lang = 'en'
		sy = ''  # synonyms
		ex = ''  # examples
		Anki = {}

		for arg in args:
				sy = arg[0]['synonyms']
				ex = arg[0]['examples']

				if arg[0]['lang_default'] != None:
						define_lang(arg[0]['lang_default'])
						return

				if arg[0]['lang'] == '':
						lang = default_lang
				else:
						lang = arg[0]['lang']

				Anki = {
						'profile': arg[0]['profile'],
						'card': arg[0]['card']
				}

				break

		# upper() because in list of language.py all the abbreviation are uppercased.
		lang = lang.upper()

		try:
				if lang in language:
						url = language[lang] + word.decode('utf-8')

						meaning(url)

						if ex:
								examples(url)
						if sy:
								synonyms(url)
						# if Anki['card'] is None:
						# 		pass
						# else:
						# 		get_anki(Anki['card'], lang, word, WORD_MEANING, profile=Anki['profile'])

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
		except TypeError:
				print("Sorry, We cannot find this word! Verify if you're typing the correct language.")
				return



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
            mean = f'{str(i)}. {m["definition"]}'

            WORD_MEANING.append(mean)
            print(mean)


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
            ex = f'{str(i)}. {e["example"]}'

            WORD_EXAMPLES.append(ex)
            print(ex)


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


def get_anki(card, lang, word, meaning, **kwargs):
    print('ANKI LOG ----------------------')

    profile = kwargs.get('profile')

    create_anki(lang)

    random_meaning = randint(0, len(meaning) - 1)

    if card is None:
        print('Oops! You should select a card type!')
        return
    elif profile is None:
        print(f'creating card type: "{card}", for current user.')

        if card in ['basic', 'basic-reverse']:
            anki.createCard(card, lang, word, meaning[random_meaning])
            return
        else: # cloze-card
            anki.createCard(card, lang, word, meaning[random_meaning], examples=WORD_EXAMPLES)
            return
    else:
        thread = threading.Thread(target=anki.changeProfile(profile))
        thread.start()

        # wait until change the profile
        thread.join()

        # Check if the new profile already have the deck
        create_anki(lang)

        print(f'changing profile to "{profile}" and adding card type: "{card}".')

        if card in ['basic', 'basic-reverse']:
            anki.createCard(card, lang, word, meaning[random_meaning])
            return
        else: # cloze-card
            anki.createCard(card, lang, word, meaning[random_meaning], examples=WORD_EXAMPLES)
            return


def create_anki(lang):
    if anki.IsDeckCreated() == False:
        anki.createDeck()

    if anki.IsSubDeckCreated(lang) == False:
        anki.createSubDeck(lang)


def define_lang(lang):
    lang_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/default_lang.json'

    with open(lang_file, 'r+') as file:
        json_data = json.load(file)
        stringfied = json.dumps(json_data)

        old_lang = json_data['default_lang']

        file.seek(0)
        file.truncate()

        file.write(stringfied.replace(old_lang, lang))

    return

if __name__ == '__main__':
		parser = Args.get_parser()
		args = vars(parser.parse_args())
		# main('apple', [args])
		main(sys.argv[1], [args])
