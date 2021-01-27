# -*- coding: utf-8 -*-

import sys
import json
import requests
import argparse
from language import language
#from dictionary.language import language

def main(word, lang):
    word = word.encode('utf-8')

    # upper() because in list of language.py all the abbreviation are uppercased.
    lang = lang.upper()

    if lang in language:
       url = language[lang] + word.decode('utf-8')
       meaning(url)
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

def meaning(url):
    header = {
        "Accept": "charset=utf-8"
    }

    response = requests.request('GET', url, headers=header)
    
    data = json.loads(response.text.encode('utf-8'))

    for obj in data:
        try:
            meanings = obj['meanings'][0]['definitions']
           
            print('DEFINITIONS ----------------------')
            
            for definition in meanings:
                print("- " +  definition['definition'])

            
            print('EXAMPLES ----------------------')

            for example in meanings:
                print("- " + example['example'])

            print('SYNONYMS ----------------------')

            i = 0

            for synonym in meanings:
                i = i + 1
                print('- ' + synonym['synonyms'][i])
                

        except (IndexError, TypeError):
            print('sorry, we could not find the word you are looking for :(')
            break

        except KeyError:
            break

def get_parser():
    parser = argparse.ArgumentParser(prog='cli-dictionary', description='the fastest way to find a word meaning.')
    parser.add_argument('word', type=str, help='the word to be searched.')
    parser.add_argument('lang', type=str, help='the language of the requested word.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.3.1')
    parser.add_argument('-s', '--synonyms', help='display the synonyms of the requested word.', action='store_const', const=42)
    parser.add_argument('-x', '--examples', help='display a phrase using the requested word.', action='store_const', const=42)
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = vars(parser.parse_args())
    main(sys.argv[1], sys.argv[2])
