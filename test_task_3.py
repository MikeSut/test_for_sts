import unittest
from task_3 import bracket_validator

class TestBracketValidator(unittest.TestCase):
    def test_values(self):
        self.assertEqual(bracket_validator("([{}])"), True)
        self.assertEqual(bracket_validator("(){}[]"), True)
        self.assertEqual(bracket_validator("(}"), False)
        self.assertEqual(bracket_validator("[(])"), False)
        self.assertEqual(bracket_validator("[({})](]"), False)
        self.assertRaises(ValueError, bracket_validator, "abc{)")
        self.assertRaises(ValueError, bracket_validator, "{1}")