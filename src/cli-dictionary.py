#!/usr/bin/python3
import json
import os
import sys

import iterfzf as fzf
import requests
import rich
from rich.console import Console

import configs.config as settings
from args import Args
from configs.words import words

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

def get_results(word, lang, sy: bool, ex: bool):
	if lang in settings.API.keys():
		url = settings.API[lang] + word
		print_definition(url, sy, ex)
	else:
		print_lang_not_found()


def get_response(url):
    header = {
        "Accept": "charset=utf-8",
        "Content-Type": "application/json"
    }
    response = requests.request('GET', url, headers=header)
    data = json.loads(response.text)
    return data


def print_meanings(meaning, iter_num):
    partOfSpeech : str = meaning['partOfSpeech']
    rich.print("[bold][white]{}. {}[/white][/bold]".format(iter_num, partOfSpeech.upper()))
    definitions = meaning['definitions']
    for idx, definition in enumerate(definitions, 1):
        rich.print("\t[green]{}. {}[/green]".format(idx, definition['definition']))


def print_definition(url, sy, ex):
	data = get_response(url)
	meanings = data[0]['meanings']
	for index, meaning in enumerate(meanings, 1):
			print_meanings(meaning, index)

def main(word, args):
	lang = os.getenv('CLI_DICT_DEFAULT_LANG', settings.DEFAULT_LANG)

	if word == '' or word == None:
		word = fzf.iterfzf(words)

	synonyms = args['synonyms']
	examples = args['examples']
	lang = args['lang'] if args['lang'] != '' else lang.upper()

	get_results(word, lang, synonyms, examples)

if __name__ == '__main__':
	parser = Args.get_parser()
	args = vars(parser.parse_args())
	word = args['word']
	main(word, args)
