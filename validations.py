import validators
from urllib.parse import urlparse


def is_valid_url(string: str) -> bool:
    """ Checks if the URL is a valid one. """
    parsed_url = urlparse(string)
    if not bool(parsed_url.scheme):
        string = f"http://{string}"
        return validators.url(string)
    else:
        return validators.url(string)

