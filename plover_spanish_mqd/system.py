# vim: set fileencoding=utf-8 :

# SPCTNVRIAEOcstnprieao*#
KEYS = (
    # '#',
    'S-', 'P-', 'C-', 'T-', 'N-', 'V-', 'R-',
    'I-', 'A-',
    '-E', '-O',
    '-c', '-s', '-t', '-n', '-p', '-r',
    #'*',
    '-i', '-e', '-a', '-o',
    '*', '#'
)

IMPLICIT_HYPHEN_KEYS = KEYS

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'S-'        : ('a', 'q'),
        'P-'        : 'w',
        'C-'        : 's',
        'T-'        : 'e',
        'N-'        : 'd',
        'V-'        : 'r',
        'R-'        : 'f',
        'I-'        : 'c',
        'A-'        : 'v',
        '-E'        : 'n',
        '-O'        : 'm',
        '-c'        : 'u',
        '-s'        : 'j',
        '-t'        : 'i',
        '-n'        : 'k',
        '-p'        : 'o',
        '-r'        : 'l',
        '-i'        : 'p',
        '-e'        : ';',
        '-a'        : '[',
        '-o'        : '\'',
        '*'         : ('t', 'g', 'y', 'h'),
		      '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Stentura': {
        'S-'   : 'S-',
        'P-'   : 'T-',
        'C-'   : 'K-',
        'T-'   : 'P-',
        'N-'   : 'W-',
        'V-'   : 'H-',
        'R-'   : 'R-',
        'I-'   : 'A-',
        'A-'   : 'O-',
        '-E'   : '-E',
        '-O'   : '-U',
        '-c'   : '-F',
        '-s'   : '-R',
        '-t'   : '-P',
        '-n'   : '-B',
        '-p'   : '-L',
        '-r'   : '-G',
        '-i'   : '-T',
        '-e'   : '-S',
        '-a'   : '-D',
        '-o'   : '-Z',
        '*'    : '*',
        '#'    : '#',
        'no-op': '^'
    },
}

KEYMAPS['Stentura (Italian version)'] = KEYMAPS['Stentura']

DICTIONARIES_ROOT = 'asset:plover_spanish_mqd:dictionaries'
DEFAULT_DICTIONARIES = ('spanish_mqd_single.py', 'spanish_mqd_double.py', 'user.json')
