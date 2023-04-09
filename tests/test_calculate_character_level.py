"""
Derek Woo
A01351415
"""


from unittest import TestCase
from character_management.character_level import calculate_character_level


class TestCalculateCharacterLevel(TestCase):
    def test_calculate_character_level_with_non_dictionary_character(self):
        test_character = "String"
        with self.assertRaises(TypeError):
            calculate_character_level(character=test_character)

    def test_calculate_character_level_without_reeses_key(self):
        test_character = {"Smarts": 1}
        with self.assertRaises(KeyError):
            calculate_character_level(character=test_character)

    def test_calculate_character_level_without_smarts_key(self):
        test_character = {"Reeses": 1}
        with self.assertRaises(KeyError):
            calculate_character_level(character=test_character)

    def test_calculate_character_level_without_reeses_or_smarts_key(self):
        test_character = {}
        with self.assertRaises(KeyError):
            calculate_character_level(character=test_character)

    def test_calculate_character_level_with_0_reeses_and_smarts(self):
        test_character = {"Reeses": 0, "Smarts": 0}
        calculate_character_level(character=test_character)
        expected = {"Reeses": 0, "Smarts": 0, "Level": 0}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_calculate_character_level_with_1_reeses_and_smarts(self):
        test_character = {"Reeses": 1, "Smarts": 1}
        calculate_character_level(character=test_character)
        expected = {"Reeses": 1, "Smarts": 1, "Level": 0}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_calculate_character_level_with_10_reeses_and_smarts(self):
        test_character = {"Reeses": 10, "Smarts": 10}
        calculate_character_level(character=test_character)
        expected = {"Reeses": 10, "Smarts": 10, "Level": 4}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_calculate_character_level_with_higher_smarts(self):
        test_character = {"Reeses": 5, "Smarts": 10}
        calculate_character_level(character=test_character)
        expected = {"Reeses": 5, "Smarts": 10, "Level": 3}
        actual = test_character
        self.assertEqual(expected, actual)

    def test_calculate_character_level_with_higher_reeses(self):
        test_character = {"Reeses": 10, "Smarts": 5}
        calculate_character_level(character=test_character)
        expected = {"Reeses": 10, "Smarts": 5, "Level": 3}
        actual = test_character
        self.assertEqual(expected, actual)

