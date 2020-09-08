import re

from flask import Blueprint

from spell_checker.utils import build_regex, get_character_repeats, is_correct_format


bp = Blueprint('spellcheck', __name__, url_prefix='/spellcheck')


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


@bp.route('/<query>')
def check_word(query):

    # Convert the query string to standard format (all lowercase letters)
    standardized_query = query.lower()

    # First, look for an exactly correct match as that is easy to identify
    if is_correct_format(query) and standardized_query in words:
        return {
            "status": 200,
            "body": {
                "correct": True,
                "suggestions": []
            }
        }

    # If there is not an exact match, go through the process of looking for possible matches in the dictionary provided
    character_repeats = get_character_repeats(standardized_query)
    regex = build_regex(character_repeats)
    pattern = re.compile(regex)

    matches = [word for word in words if pattern.fullmatch(word)]

    return {
        "query": query,
        "regex": regex,
        "matches": matches
    }
