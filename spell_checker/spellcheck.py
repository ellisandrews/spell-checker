import re

from flask import Blueprint

from spell_checker.utils import build_regex, get_letter_repeats


bp = Blueprint('spellcheck', __name__, url_prefix='/spellcheck')


@bp.route('/<query>')
def check_word(query):

    letter_repeats = get_letter_repeats(query)
    regex = build_regex(letter_repeats)
    pattern = re.compile(regex)

    # Sample words
    words = [
        'ballistae',
        'ballistic',
        'ballistically',
        'ballistician',
        'ballisticians',
        'ballistics',
        'ballo',
        'balloon',
        'ballooned',
        'ballooner',
        'ballooners',
        'ballooning',
        'balloonist'
    ]

    matches = [word for word in words if pattern.fullmatch(word)]

    return {
        "query": query,
        "regex": regex,
        "matches": matches
    }
