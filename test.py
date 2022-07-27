import unittest
from helpers import generate_short_id
from decouple import config
from validations import is_valid_url


class TestLinkShortener(unittest.TestCase):

    def test_short_id_length(self):
        SHORT_ID_LENGTH = int(config("SHORT_ID_LENGTH"))
        self.assertEqual(len(generate_short_id()), SHORT_ID_LENGTH)

    def test_short_id_space_occurrence(self):
        a_short_id = generate_short_id()
        self.assertEqual(a_short_id.replace(" ", ""), a_short_id)

    def test_url_validation(self):
        self.assertTrue(is_valid_url("http://google.com/123jdkfflff"))
        self.assertTrue(is_valid_url("facebook.com/meysamkermani"))
        self.assertTrue(is_valid_url("https://191.234.22.45/sdjjsfheonn"))


if __name__ == '__main__':
    unittest.main()