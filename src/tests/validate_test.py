import unittest
from util import validate_not_empty, validate_length, validate_key, validate

class TestValidate(unittest.TestCase):
    def test_validate_not_empty(self):
        params = ["kirja123", "kalle", "kallen kirja  ", "1999", ""]
        self.assertRaises(ValueError, validate_not_empty, params)

        params = ["kirja123", "kalle", "kallen kirja", "1999", "    "]
        self.assertRaises(ValueError, validate_not_empty, params)

    def test_validate_length(self):
        # Testing validation if a parameter is too short: 
        # length of author given is 1 but minimum length is set to 2
        params = ["kirja123", "k", "kallen kirja  ", "1999", "SKS"]
        self.assertRaisesRegex(ValueError, "Field too short", validate_length, params, 2, 255)

        # length of author given is 10 but maximum length is set to 8
        params = ["kirja123", "kallekalle", "kallen kirja  ", "1999", "SKS"]
        self.assertRaisesRegex(ValueError, "Field too long", validate_length, params)