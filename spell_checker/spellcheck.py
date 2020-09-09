from flask import abort, Blueprint

from spell_checker import redis_client
from spell_checker.utils import build_regex, get_character_repeats, is_correct_format


bp = Blueprint('spellcheck', __name__, url_prefix='/spellcheck')


@bp.route('/<query>')
def check_word(query):

    # Convert the query string to standard format for processing (all lowercase letters)
    word = query.lower()

    # Pull the set of all dictionary words from redis
    dict_words = redis_client.smembers('spellcheck:dictionary')

    # First, look for an exactly correct match as that is easy to identify and immediately returnable
    if is_correct_format(query) and word in dict_words:
        return { 'correct': True, 'suggestions': [] }, 200

    # If there is not an exact match, go through the process of looking for possible matches in the dictionary

    # Construct a regex pattern with which to identify matches (per given criteria)
    pattern = build_regex(word)  
    
    # Search the set of dictionary words for possible matches using the regex pattern
    matches = [w for w in dict_words if pattern.fullmatch(w)]

    # If there are any dictionary word matches, consider the query "found" but incorrectly spelled. 
    # Otherwise, 404 not found.
    if matches:
        return { 'correct': False, 'suggestions': sorted(matches) }, 200
    else:
        abort(404)
