import json, sys
from urllib.request import urlopen
from languages.language import language

def main():
    # receives word to find and the word's language
    # word_lang = str(input(''))

    # word = word_lang.split(' ')[0]
    # lang = word_lang.split(' ')[1]

    # url = ''
    
    print(language['EN'])

if __name__ == '__main__':
    main()   

# if lang.__eq__('en'):
#     url = 'https://api.dictionaryapi.dev/api/v2/entries/{0}/{1}'.format(
#         'en', word)
# elif lang.__eq__('pt'):
#     url = 'https://api.dictionaryapi.dev/api/v2/entries/{0}/{1}'.format('pt-BR', word)
# else:
#     print("""
#         select a valid language:
#         en <english>,
#         pt <portuguese>,
#         hi <hindi>, 
#         es <spanish>,
#         fr <french>,
#         ja <japanese>,
#         ru <russian>,
#         de <german>,
#         it <italian>,
#         ko <korean>,
#         zh <chinese>, 
#         ar <arabic>,
#         tr <turkish>
#     """)

#####################aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# response = urlopen(url)
# data = json.loads(response.read())

# for obj in data:
#     try:
#         for i in range(10):
#             if i == 0:
#                 pass
#             else:
#                 print(
#                     str(obj).split("definition':")[i].split('.')[0].replace(
#                         "'",
#                         str(i) + '. '))

#     except IndexError as ex:
#         break
