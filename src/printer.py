from config.languages import LANGUAGES
import rich

class Printer():
	@staticmethod
	def lang_not_found():
		print('select a valid language: ')

		for lang in LANGUAGES:
			print(f'{lang.name} - {lang.value}')

	def default_print(text: str):
		rich.print(text)
