#!/usr/bin/python3

from setuptools import setup

setup(
    name='cli-dictionary',
    version='2.3.2',
    description='cli-dictionary',
    packages = ['dictionary, anki'],
    author='Ropoko',
    author_email='rodrigostramantinoli@gmail.com ',
    scripts=['bin/cli-dictionary'],
)
