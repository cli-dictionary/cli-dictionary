import enum

class LANGUAGES(enum.Enum):
    EN = "EN"
    PT = "PT"
    HI = "HI"
    ES = "ES"
    FR = "FR"
    JA = "JA"
    RU = "RU"
    DE = "DE"
    IT = "IT"
    KO = "KO"
    ZH = "ZH"
    AR = "AR"
    TR = "TR"


API = {
    LANGUAGES.EN.value: "https://api.dictionaryapi.dev/api/v2/entries/en/",
    LANGUAGES.PT.value: "https://api.dictionaryapi.dev/api/v2/entries/pt-BR/",
    LANGUAGES.HI.value: "https://api.dictionaryapi.dev/api/v2/entries/hi/",
    LANGUAGES.ES.value: "https://api.dictionaryapi.dev/api/v2/entries/es/",
    LANGUAGES.FR.value: "https://api.dictionaryapi.dev/api/v2/entries/fr/",
    LANGUAGES.JA.value: "https://api.dictionaryapi.dev/api/v2/entries/ja/",
    LANGUAGES.RU.value: "https://api.dictionaryapi.dev/api/v2/entries/ru/",
    LANGUAGES.DE.value: "https://api.dictionaryapi.dev/api/v2/entries/de/",
    LANGUAGES.IT.value: "https://api.dictionaryapi.dev/api/v2/entries/it/",
    LANGUAGES.KO.value: "https://api.dictionaryapi.dev/api/v2/entries/ko/",
    LANGUAGES.ZH.value: "https://api.dictionaryapi.dev/api/v2/entries/zh-CN/",
    LANGUAGES.AR.value: "https://api.dictionaryapi.dev/api/v2/entries/ar/",
    LANGUAGES.TR.value: "https://api.dictionaryapi.dev/api/v2/entries/tr/"
}

DEFAULT_LANG = LANGUAGES.EN.value