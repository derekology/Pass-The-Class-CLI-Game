"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from character_management.manage_character import make_character


class TestMakeCharacter(TestCase):
    @patch("builtins.input", side_effect=["Name"])
    def test_make_character_with_a_one_word_name(self, _):
        expected = {"Name": "Name", "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5,
                    "Luck": 1, "Strength": 1, "Level": 1}
        actual = make_character()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Test Name"])
    def test_make_character_with_a_name_containing_space(self, _):
        expected = {"Name": "Test Name", "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5,
                    "Luck": 1, "Strength": 1, "Level": 1}
        actual = make_character()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["1314"])
    def test_make_character_with_a_name_containing_number(self, _):
        expected = {"Name": "1314", "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5,
                    "Luck": 1, "Strength": 1, "Level": 1}
        actual = make_character()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["?Name!"])
    def test_make_character_with_a_name_containing_punctuation(self, _):
        expected = {"Name": "?Name!", "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5,
                    "Luck": 1, "Strength": 1, "Level": 1}
        actual = make_character()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["HaX0R321!"])
    def test_make_character_with_a_mixed_character_name(self, _):
        expected = {"Name": "HaX0R321!", "X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5,
                    "Luck": 1, "Strength": 1, "Level": 1}
        actual = make_character()
        self.assertEqual(expected, actual)
