from argparse import ArgumentParser
from pathlib import Path

from redis import StrictRedis


def populate(filepath: str, key: str, strict_redis: StrictRedis) -> None:
    """
    Read in a file of words (one per line) and add them to a redis set under a given key.
    
    Note: If the file of words to add is large, probably want to refactor to read/load in batches.
    """
    # Read the file contents
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Strip newline character from each line and ensure all are lowercase
    lines = [line.strip('\n').lower() for line in lines]

    # Add the words to the redis set under the specified key
    strict_redis.sadd(key, *lines)


if __name__ == '__main__':

    # Path to the given dictionary.txt file in this repository
    filepath = str(Path(__file__).parent.parent) + '/exercise/dictionary.txt'

    # Command line args
    a = ArgumentParser()
    a.add_argument('--db', default=0, type=int, help='Database of redis instance to populate')
    a.add_argument('--filepath', default=filepath, help='Path to the file of words to load')
    a.add_argument('--host', default='localhost', help='Hostname of the redis instance')
    a.add_argument('--key', default='spellcheck:dictionary', help='Key of redis database to populate')
    a.add_argument('--port', default=6379, type=int, help='Port of the redis instance')
    args = a.parse_args()

    # Connect to redis
    sr = StrictRedis(host=args.host, port=args.port, db=args.db)

    # Populate the redis database
    populate(args.filepath, args.key, sr)
