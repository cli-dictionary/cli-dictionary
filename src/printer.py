from config.languages import LANGUAGES

class Printer():
	@staticmethod
	def lang_not_found():
		print('select a valid language: ')

		for lang in LANGUAGES:
			print(f'{lang.name} - {lang.value} \n')

	def definition():
		print('definition')
