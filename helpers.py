import string
from random import choice
from decouple import config

SHORT_ID_LENGTH = int(config("SHORT_ID_LENGTH"))


def generate_short_id(num_of_chars: int = SHORT_ID_LENGTH) -> str:
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

