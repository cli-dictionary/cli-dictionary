from argparse import ArgumentParser

class Args():
	@staticmethod
	def get_parser():
		parser = ArgumentParser(
			prog='cli-dictionary',
			description='welcome to cli-dictionary, never use a browser again to get a word meaning ;)'
		)

		parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.3.1')

		# positional args
		parser.add_argument('word', type=str, help='the word to be searched.', default=None, nargs='?')
		parser.add_argument('lang', type=str, help='the language of the requested word.', nargs='?', default='')

		# optional args
		parser.add_argument('-s', '--synonyms', action='store_true', help='display the synonyms of the requested word.')
		parser.add_argument('-e', '--examples', action='store_true', help='display a phrase using the requested word.')
		parser.add_argument('--lang-default', default=None, help='Define the default language to search the words.')

		# Anki
		group_anki = parser.add_argument_group('Anki-Flashcards')
		group_anki.add_argument('--profile', help='select the profile', type=str)
		group_anki.add_argument('--card', help='select the type of card', choices=['basic', 'basic-reverse', 'cloze'])

		return parser
