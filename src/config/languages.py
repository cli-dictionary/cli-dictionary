import enum

class LANGUAGES(enum.Enum):
	EN = 'English'
	PT = 'Portuguese'
	HI = 'Hindi'
	ES = 'Spanish'
	FR = 'French'
	JA = 'Japanese'
	RU = 'Russian'
	DE = 'German'
	IT = 'Italian'
	KO = 'Korean'
	ZH = 'Chinese (simplified)'
	AR = 'Arabic'
	TR = 'Turkish'

DEFAULT_LANG = LANGUAGES.EN.name
