#!/usr/bin/python3
import os
import sys

import iterfzf as fzf

from args import Args
from config.words import words
from config.api import API as API_CONFIG
from config.languages import DEFAULT_LANG
from printer import Printer
from api import API

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

def get_results(word: str, lang: str, sy: bool, ex: bool) -> None:
	if lang in API_CONFIG.keys():
		url = API_CONFIG[lang] + word
		print_definition(url, sy, ex)
	else:
		Printer.lang_not_found()


def print_meanings(meaning, iter_num):
	partOfSpeech : str = meaning['partOfSpeech']

	text = '[bold][white]{}. {}[/white][/bold]'.format(iter_num, partOfSpeech.upper())
	Printer.default_print(text)

	definitions = meaning['definitions']

	for idx, definition in enumerate(definitions, 1):
		text = '\t[green]{}. {}[/green]'.format(idx, definition['definition'])
		Printer.default_print(text)


def print_definition(url, sy, ex):
	api = API(url)
	data = api.get_response()

	# print(data)

	meanings = data[0]['meanings']

	for index, meaning in enumerate(meanings, 1):
		print_meanings(meaning, index)

def main(word, args):
	lang = os.getenv('CLI_DICT_DEFAULT_LANG', DEFAULT_LANG)

	if word == '' or word == None:
		Printer.default_print("[red]Default argument 'word' is missing \n")

		Printer.default_print("How you should use: ")
		Printer.default_print("-> cli-dictionary [bold][white]<word>[/bold][/white] [white]<lang>[/white]")
		return
	#	word = fzf.iterfzf(words)

	synonyms = args['synonyms']
	examples = args['examples']

	lang = args['lang'] if args['lang'] != '' else lang
	lang = lang.upper()

	get_results(word, lang, synonyms, examples)

if __name__ == '__main__':
	parser = Args.get_parser()
	args = vars(parser.parse_args())
	word = args['word']
	main(word, args)
