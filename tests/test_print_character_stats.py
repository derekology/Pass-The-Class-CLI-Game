"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from character_management.manage_character import print_character_stats
import io


class TestPrintCharacterStats(TestCase):
    def test_apply_resource_with_non_dictionary_character(self):
        test_character = "String"
        with self.assertRaises(TypeError):
            print_character_stats(character=test_character)

    def test_print_character_stats_without_current_name_key(self):
        test_character = {"Level": 0, "Current HP": 5, "Strength": 10, "Luck": 15}
        with self.assertRaises(KeyError):
            print_character_stats(character=test_character)

    def test_print_character_stats_without_level_key(self):
        test_character = {"Name": "Test Character", "Current HP": 5, "Strength": 10, "Luck": 15}
        with self.assertRaises(KeyError):
            print_character_stats(character=test_character)

    def test_print_character_stats_without_current_hp_key(self):
        test_character = {"Name": "Test Character", "Level": 0, "Strength": 10, "Luck": 15}
        with self.assertRaises(KeyError):
            print_character_stats(character=test_character)

    def test_print_character_stats_without_strength_key(self):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": 5, "Luck": 15}
        with self.assertRaises(KeyError):
            print_character_stats(character=test_character)

    def test_print_character_stats_without_luck_key(self):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": 5, "Strength": 10}
        with self.assertRaises(KeyError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_non_string_name(self):
        test_character = {"Name": 0, "Level": 0, "Current HP": 5, "Strength": 10, "Luck": 15}
        with self.assertRaises(TypeError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_non_integer_level(self):
        test_character = {"Name": "Test Character", "Level": "0", "Current HP": 5, "Strength": 10, "Luck": 15}
        with self.assertRaises(ValueError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_non_integer_health(self):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": "5", "Strength": 10, "Luck": 15}
        with self.assertRaises(ValueError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_non_integer_strength(self):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": 5, "Strength": "10", "Luck": 15}
        with self.assertRaises(ValueError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_non_integer_luck(self):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": 5, "Strength": 10, "Luck": "15"}
        with self.assertRaises(ValueError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_negative_level(self):
        test_character = {"Name": "Test Character", "Level": -1, "Current HP": 5, "Strength": 10, "Luck": 15}
        with self.assertRaises(ValueError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_negative_health(self):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": -5, "Strength": 10, "Luck": 15}
        with self.assertRaises(ValueError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_negative_strength(self):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": 5, "Strength": -10, "Luck": 15}
        with self.assertRaises(ValueError):
            print_character_stats(character=test_character)

    def test_print_character_stats_with_negative_luck(self):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": 5, "Strength": 10, "Luck": -15}
        with self.assertRaises(ValueError):
            print_character_stats(character=test_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_stats_with_all_zero_levels(self, mock_print):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": 0, "Strength": 0, "Luck": 0}
        print_character_stats(character=test_character)
        expected = "Test Character (Level 0)\nHealth: 0\nStrength: 0\nLuck:0\n"
        actual = mock_print.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_stats_with_all_one_levels(self, mock_print):
        test_character = {"Name": "Test Character", "Level": 1, "Current HP": 1, "Strength": 1, "Luck": 1}
        print_character_stats(character=test_character)
        expected = "Test Character (Level 1)\nHealth: 1\nStrength: 1\nLuck:1\n"
        actual = mock_print.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_stats_with_positive_levels(self, mock_print):
        test_character = {"Name": "Test Character", "Level": 10, "Current HP": 10, "Strength": 10, "Luck": 10}
        print_character_stats(character=test_character)
        expected = "Test Character (Level 10)\nHealth: 10\nStrength: 10\nLuck:10\n"
        actual = mock_print.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_stats_with_mixed_levels(self, mock_print):
        test_character = {"Name": "Test Character", "Level": 0, "Current HP": 5, "Strength": 10, "Luck": 15}
        print_character_stats(character=test_character)
        expected = "Test Character (Level 0)\nHealth: 5\nStrength: 10\nLuck:15\n"
        actual = mock_print.getvalue()
        self.assertIn(expected, actual)

