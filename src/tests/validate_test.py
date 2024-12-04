import unittest
import mock
from util import validate_not_empty, validate_length, validate_key, validate

class TestValidate(unittest.TestCase):
    def test_validate_not_empty(self):
        params = ["kirja123", "kalle", "kallen kirja  ", "1999", ""]
        self.assertRaises(ValueError, validate_not_empty, params)

        params = ["kirja123", "kalle", "kallen kirja", "1999", "    "]
        self.assertRaises(ValueError, validate_not_empty, params)

        params = ["kirja123", "kalle", "kallen kirja", "1999", "    "]

    def test_validate_too_short_parameter(self):
        # Testing validation if a parameter is too short: 
        # length of author given is 1 but minimum length is set to 2
        params = ["kirja123", "k", "kallen kirja", "1999", "SKS"]
        self.assertRaisesRegex(ValueError, "Field too short", validate_length, params, 2, 255)

    def test_validate_too_long_parameter(self):
        # length of author given is 10 but maximum length is set to 8
        params = ["kirja123", "kallekalle", "kallen kirja", "1999", "SKS"]
        self.assertRaisesRegex(ValueError, "Field too long", validate_length, params, 1, 8)

    @unittest.skip('Work in progress')
    def test_validate_key(self):
        with mock.patch('repositories.repository_manager.get_all_keys', return_value=["kirja123"]):
            key = "kirja123"
            self.assertRaisesRegex(ValueError, "Key already in use", validate_key, key)

    # @unittest.skip('Work in progress')
    def test_validate_works_with_correct_input(self):
        with mock.patch('util.validate_key', return_value=True):
            params = ["kirja123", "kalle", "kallen kirja", "1999", "SKS"]
            self.run(validate(params))
