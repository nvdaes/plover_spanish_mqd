# vim: set fileencoding=utf-8 :

# #SPCTHVRIAEOcsthpr*ieao
KEYS = (
	# '#',
	'S-', 'P-', 'C-', 'T-', 'N-', 'V-', 'R-',
	'I-', 'A-',
	'-E', '-O',
	'-c', '-s', '-t', '-n', '-p', '-r',
	# '*',
	'-i', '-e', '-a', '-o',
	'*', '#'
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ''

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
	'Gemini PR': {
		'#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
		'S-': ('S1-', 'S2-'),
		'P-': 'T-',
		'C-': 'K-',
		'T-': 'P-',
		'N-': 'W-',
		'V-': 'H-',
		'R-': 'R-',
		'I-': 'A-',
		'A-': 'O-',
		'*': ('*1', '*2', '*3', '*4'),
		'-E': '-E',
		'-O': '-U',
		'-c': '-F',
		'-s': '-R',
		'-t': '-P',
		'-n': '-B',
		'-p': '-L',
		'-r': '-G',
		'-i': '-T',
		'-e': '-S',
		'-a': '-D',
		'-o': '-Z',
		'no-op': ('Fn', 'pwr', 'res1', 'res2'),
	},
	'Keyboard': {
		'#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
		'S-': ('a', 'q'),
		'P-': 'w',
		'C-': 's',
		'T-': 'e',
		'N-': 'd',
		'V-': 'r',
		'R-': 'f',
		'I-': 'c',
		'A-': 'v',
		'*': ('t', 'g', 'y', 'h'),
		'-E': 'n',
		'-O': 'm',
		'-c': 'u',
		'-s': 'j',
		'-t': 'i',
		'-n': 'k',
		'-p': 'o',
		'-r': 'l',
		'-i': 'p',
		'-e': ';',
		'-a': '[',
		'-o': '\'',
		'arpeggiate': 'space',
		# Suppress adjacent keys to prevent miss-strokes.
		'no-op': ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
	},
	'Passport': {
		'#': '#',
		'S-': ('S', 'C'),
		'P-': 'T',
		'C-': 'K',
		'T-': 'P',
		'N-': 'W',
		'V-': 'H',
		'R-': 'R',
		'I-': 'A',
		'A-': 'O',
		'*': ('~', '*'),
		'-E': 'E',
		'-O': 'U',
		'-c': 'F',
		'-s': 'Q',
		'-t': 'N',
		'-n': 'B',
		'-p': 'L',
		'-r': 'G',
		'-i': 'Y',
		'-e': 'X',
		'-a': 'D',
		'-o': 'Z',
		'no-op': ('!', '^', '+'),
	},
	'Stentura': {
		# '#': '#',
		'S-': 'S-',
		'P-': 'T-',
		'C-': 'K-',
		'T-': 'P-',
		'N-': 'W-',
		'V-': 'H-',
		'R-': 'R-',
		'I-': 'A-',
		'A-': 'O-',
		# '*': '*',
		'-E': '-E',
		'-O': '-U',
		'-c': '-F',
		'-s': '-R',
		'-t': '-P',
		'-n': '-B',
		'-p': '-L',
		'-r': '-G',
		'-i': '-T',
		'-e': '-S',
		'-a': '-D',
		'-o': '-Z',
		'*': '*',
		'#': '#',
		'no-op': '^',
	},
	'TX Bolt': {
		'#': '#',
		'S-': 'S-',
		'P-': 'T-',
		'C-': 'K-',
		'T-': 'P-',
		'N-': 'W-',
		'V-': 'H-',
		'R-': 'R-',
		'I-': 'A-',
		'A-': 'O-',
		'*': '*',
		'-E': '-E',
		'-O': '-U',
		'-c': '-F',
		'-s': '-R',
		'-t': '-P',
		'-n': '-B',
		'-p': '-L',
		'-r': '-G',
		'-i': '-T',
		'-e': '-S',
		'-a': '-D',
		'-o': '-Z',
	},
	'Treal': {
		'#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
		'S-': ('S1-', 'S2-'),
		'P-': 'T-',
		'C-': 'K-',
		'T-': 'P-',
		'N-': 'W-',
		'V-': 'H-',
		'R-': 'R-',
		'I-': 'A-',
		'A-': 'O-',
		'*': ('*1', '*2'),
		'-E': '-E',
		'-O': '-U',
		'-c': '-F',
		'-s': '-R',
		'-t': '-P',
		'-n': '-B',
		'-p': '-L',
		'-r': '-G',
		'-i': '-T',
		'-e': '-S',
		'-a': '-D',
		'-o': '-Z',
		'no-op': ('X1-', 'X2-', 'X3'),
	},
}

KEYMAPS['Stentura (Italian version)'] = KEYMAPS['Stentura']

DICTIONARIES_ROOT = 'asset:plover_spanish_mqd:dictionaries'
DEFAULT_DICTIONARIES = (
	'user_es.json', 'punctuation.json', 'initial.json', DICTIONARIES_ROOT + '/spanish_mqd.py'
)
