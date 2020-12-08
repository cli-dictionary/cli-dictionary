import json, sys
from urllib.request import urlopen
from languages.language import language

def main():
    word_lang = str(input(''))

    word = word_lang.split(' ')[0].encode('utf-8')
    lang = word_lang.split(' ')[1].upper()

    if lang in language:
        url = language[lang] + '/' + word.decode('utf-8')
        meaning(url.encode('utf-8'))
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
    response = urlopen(url)
    data = json.loads(response.read())

    for obj in data:
        try:
            for i in range(10):
                if i == 0:
                    pass
                else:
                    print(
                        str(obj).split("definition':")[i].split('.')[0].replace(
                            "'",
                            str(i) + '. '))

        except IndexError as ex:
            break

if __name__ == '__main__':
    main()   
