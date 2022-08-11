from plover.system import english_stenotype

# cf. https://plover.readthedocs.io/en/4.0.0-dev8/api/system.html

KEYS = (
    'v-', 'D-', 'b-', 'ʃ-', 'S-', 'F-', 'G-', 'N-', 'B-', 'M-', '+-', 'L-',
    'Ä-', 'E-', 'A-', '~-',
    '-U', '-I', '-O', '-Ü',
    '-M', '-+', '-L', '-G', '-N', '-B', '-ʃ', '-S', '-F', '-n', '-D', '-s'
)

IMPLICIT_HYPHEN_KEYS = ('Ä-', 'E-', 'A-', '~-', '-U', '-I', '-O', '-Ü')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

# Type: str or None
UNDO_STROKE_STENO = 'I+NSD'

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'v-': 'q',
        'D-': 'a',
        'b-': 'z',
        'ʃ-': '2',
        'S-': 'w',
        'F-': 's',
        'G-': '3',
        'N-': 'e',
        'B-': 'd',
        'M-': '4',
        '+-': 'r',
        'L-': 'f',
        'Ä-': 'c',
        'E-': 'v',
        'A-': 'b',
        '~-': 'g',
        '-U': 'h',
        '-I': 'n',
        '-O': 'm',
        '-Ü': ',',
        '-M': '7',
        '-+': 'u',
        '-L': 'j',
        '-G': '8',
        '-N': 'i',
        '-B': 'k',
        '-ʃ': '9',
        '-S': 'o',
        '-F': 'l',
        '-n': 'p',
        '-D': ';',
        '-s': '/',
        'arpeggiate': 'space',
    },
}

DICTIONARIES_ROOT = 'asset:plover_palantype_DE:dictionaries'
DEFAULT_DICTIONARIES = ('palantype-DE.json', 'palantype-DE-extra.json', 'palantype-DE-numbers.json')
