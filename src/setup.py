from setuptools import setup, find_packages

setup (
	name='cli-dictionary',
	version='2.3.2',
	description='dictionary for command line, for now.',
	author='Ropoko',
	author_email='rodrigostramantinoli@gmail.com ',

	packages=find_packages(),
	install_requires=['requests'],
	scripts=['src/dictionary/cli-dictionary.py', 'src/anki/anki.py']
)
