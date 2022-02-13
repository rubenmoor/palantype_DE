from plover.system import english_stenotype

# cf. https://plover.readthedocs.io/en/4.0.0-dev8/api/system.html

KEYS = (
    'S-', 'B-', 'G-', 'H-', 'D-', 'F-', 'M-', 'J-', 'W-', 'L-', 'N-', 'R-',
    'Ä-', 'E-', 'A-', '~-',
    '-U', '-I', '-O', '-Ü',
    '-+', '-L', '-M', '-G', '-N', '-B', '-F', '-S', '-ʃ', '-s', '-D', '-n'
)

IMPLICIT_HYPHEN_KEYS = ('R-', 'Ä-', 'E-', 'A-', '~-', '-U', '-I', '-O', '-Ü', '-+')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

# Type: str or None
UNDO_STROKE_STENO = 'ILNSD'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'S-': 'q',
        'B-': 'a',
        'G-': 'z',
        'H-': '2',
        'D-': 'w',
        'F-': 's',
        'M-': '3',
        'J-': 'e',
        'W-': 'd',
        'L-': '4',
        'N-': 'r',
        'R-': 'f',
        'Ä-': 'c',
        'E-': 'v',
        'A-': 'b',
        '~-': 'g',
        '-U': 'h',
        '-I': 'n',
        '-O': 'm',
        '-Ü': ',',
        '-+': '7',
        '-L': 'u',
        '-M': 'j',
        '-G': '8',
        '-N': 'i',
        '-B': 'k',
        '-F': '9',
        '-S': 'o',
        '-ʃ': 'l',
        '-s': 'p',
        '-D': ';',
        '-n': '/',
        'arpeggiate': 'space',
    },
}

DICTIONARIES_ROOT = 'asset:plover_palantype_DE:dictionaries'
DEFAULT_DICTIONARIES = ('palantype-DE.json', 'palantype-DE-extra.json', 'palantype-DE-numbers.json')
