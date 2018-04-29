import regex as re
ALEF = "\u0627"
ALEF_MADDA = "\u0622"
ALEF_HAMZA_ABOVE = "\u0623"
ALEF_HAMZA_BELOW = "\u0625"

WAW = "\u0648"
WAW_HAMZA = "\u0624"

YEH = "\u064A"
YEH_HAMZA = "\u0626"
DOTLESS_YEH = "\u0649"  # ALEF MAKSOURA

TEH_MARBOUTA = "\u0629"
HEH = "\u0647"

TATWEEL = "\u0640"

FATHATAN = "\u064B"
DAMMATAN = "\u064C"
KASRATAN = "\u064D"
FATHA = "\u064E"
DAMMA = "\u064F"
KASRA = "\u0650"
SHADDA = "\u0651"
SUKUN = "\u0652"

NORMALIZATION_RULES = {
    ALEF_MADDA: ALEF, ALEF_HAMZA_ABOVE: ALEF, ALEF_HAMZA_BELOW: ALEF,
    YEH_HAMZA: YEH, DOTLESS_YEH: YEH,
    TEH_MARBOUTA: HEH,
    WAW_HAMZA: WAW,
    TATWEEL: '', FATHATAN: '', DAMMATAN: '', KASRATAN: '', FATHA: '',
    DAMMA: '', KASRA: '', SHADDA: '', SUKUN: ''
}


def normalize(string):
    pattern = re.compile(r'\b(' + '|'.join(NORMALIZATION_RULES.keys()) + r')\b')
    result = pattern.sub(lambda x: NORMALIZATION_RULES[x.group()], string)
    return result
