"""
Derek Woo
A01351415
"""


from unittest import TestCase
from character_management.character_level import calculate_character_level


class TestCalculateCharacterLevel(TestCase):
    def test_calculate_character_level_with_0_hp_and_strength(self):
        test_character = {"Current HP": 0, "Strength": 0}
        calculate_character_level(character=test_character)
        expected = {"Current HP": 0, "Strength": 0, "Level": 0}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_calculate_character_level_with_1_hp_and_strength(self):
        test_character = {"Current HP": 1, "Strength": 1}
        calculate_character_level(character=test_character)
        expected = {"Current HP": 1, "Strength": 1, "Level": 0}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_calculate_character_level_with_10_hp_and_strength(self):
        test_character = {"Current HP": 10, "Strength": 10}
        calculate_character_level(character=test_character)
        expected = {"Current HP": 10, "Strength": 10, "Level": 4}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_calculate_character_level_with_higher_strength(self):
        test_character = {"Current HP": 5, "Strength": 10}
        calculate_character_level(character=test_character)
        expected = {"Current HP": 5, "Strength": 10, "Level": 3}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_calculate_character_level_with_higher_hp(self):
        test_character = {"Current HP": 10, "Strength": 5}
        calculate_character_level(character=test_character)
        expected = {"Current HP": 10, "Strength": 5, "Level": 3}
        actual = test_character
        self.assertEqual(expected, actual)

