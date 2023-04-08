"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from combat_management.manage_foes import escape_from_foe


class TestEscapeFromFoe(TestCase):
    def test_escape_from_foe_with_non_dictionary_character(self):
        test_character = "String"
        with self.assertRaises(TypeError):
            escape_from_foe(character=test_character)

    def test_escape_from_foe_with_dictionary_missing_luck(self):
        test_character = {}
        with self.assertRaises(KeyError):
            escape_from_foe(character=test_character)

    def test_escape_from_foe_with_non_integer_luck(self):
        test_character = {"Luck": "0"}
        with self.assertRaises(ValueError):
            escape_from_foe(character=test_character)

    def test_escape_from_foe_with_negative_luck(self):
        test_character = {"Luck": -1}
        with self.assertRaises(ValueError):
            escape_from_foe(character=test_character)

    @patch("random.random", side_effect=[0.0])
    def test_escape_from_foe_with_lowest_random_and_character_of_zero_luck(self, _):
        test_character = {"Luck": 0}
        actual = escape_from_foe(character=test_character)
        self.assertTrue(actual)

    @patch("random.random", side_effect=[0.5])
    def test_escape_from_foe_with_middle_random_and_character_of_zero_luck(self, _):
        test_character = {"Luck": 0}
        actual = escape_from_foe(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[1.0])
    def test_escape_from_foe_with_highest_random_and_character_of_zero_luck(self, _):
        test_character = {"Luck": 0}
        actual = escape_from_foe(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[0.0])
    def test_escape_from_foe_with_lowest_random_and_character_of_one_luck(self, _):
        test_character = {"Luck": 1}
        actual = escape_from_foe(character=test_character)
        self.assertTrue(actual)

    @patch("random.random", side_effect=[0.5])
    def test_escape_from_foe_with_middle_random_and_character_of_one_luck(self, _):
        test_character = {"Luck": 1}
        actual = escape_from_foe(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[1.0])
    def test_escape_from_foe_with_highest_random_and_character_of_one_luck(self, _):
        test_character = {"Luck": 1}
        actual = escape_from_foe(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[0.0])
    def test_escape_from_foe_with_lowest_random_and_character_of_high_luck(self, _):
        test_character = {"Luck": 10}
        actual = escape_from_foe(character=test_character)
        self.assertTrue(actual)

    @patch("random.random", side_effect=[0.5])
    def test_escape_from_foe_with_middle_random_and_character_of_high_luck(self, _):
        test_character = {"Luck": 10}
        actual = escape_from_foe(character=test_character)
        self.assertTrue(actual)

    @patch("random.random", side_effect=[1.0])
    def test_escape_from_foe_with_highest_random_and_character_of_high_luck(self, _):
        test_character = {"Luck": 10}
        actual = escape_from_foe(character=test_character)
        self.assertTrue(actual)

