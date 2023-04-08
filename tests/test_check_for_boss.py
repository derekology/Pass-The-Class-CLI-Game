"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from combat_management.manage_foes import check_for_boss


class TestCheckForBoss(TestCase):
    def test_check_for_boss_with_non_dictionary_character(self):
        test_character = "String"
        with self.assertRaises(TypeError):
            check_for_boss(character=test_character)

    def test_check_for_boss_with_dictionary_missing_luck(self):
        test_character = {}
        with self.assertRaises(KeyError):
            check_for_boss(character=test_character)

    def test_check_for_boss_with_non_integer_luck(self):
        test_character = {"Level": "0"}
        with self.assertRaises(ValueError):
            check_for_boss(character=test_character)

    def test_check_for_boss_with_negative_luck(self):
        test_character = {"Level": -1}
        with self.assertRaises(ValueError):
            check_for_boss(character=test_character)

    @patch("random.random", side_effect=[0.0])
    def test_check_for_boss_with_lowest_random_value_and_zero_level(self, _):
        test_character = {"Level": 0}
        actual = check_for_boss(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[0.0])
    def test_check_for_boss_with_lowest_random_value_and_one_level(self, _):
        test_character = {"Level": 1}
        actual = check_for_boss(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[0.0])
    def test_check_for_boss_with_lowest_random_value_and_high_level(self, _):
        test_character = {"Level": 10}
        actual = check_for_boss(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[0.5])
    def test_check_for_boss_with_middle_random_value_and_zero_level(self, _):
        test_character = {"Level": 0}
        actual = check_for_boss(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[0.5])
    def test_check_for_boss_with_middle_random_value_and_one_level(self, _):
        test_character = {"Level": 1}
        actual = check_for_boss(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[0.5])
    def test_check_for_boss_with_middle_random_value_and_high_level(self, _):
        test_character = {"Level": 10}
        actual = check_for_boss(character=test_character)
        self.assertTrue(actual)

    @patch("random.random", side_effect=[1.0])
    def test_check_for_boss_with_highest_random_value_and_zero_level(self, _):
        test_character = {"Level": 0}
        actual = check_for_boss(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[1.0])
    def test_check_for_boss_with_highest_random_value_and_one_level(self, _):
        test_character = {"Level": 1}
        actual = check_for_boss(character=test_character)
        self.assertFalse(actual)

    @patch("random.random", side_effect=[1.0])
    def test_check_for_boss_with_highest_random_value_and_high_level(self, _):
        test_character = {"Level": 10}
        actual = check_for_boss(character=test_character)
        self.assertTrue(actual)
