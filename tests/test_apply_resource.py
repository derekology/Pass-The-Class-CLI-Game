"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from character_management.character_level import apply_resource, get_upgrade_choice


class TestApplyResource(TestCase):
    
    def test_apply_resource_with_non_dictionary_character(self):
        test_character = "String"
        with self.assertRaises(TypeError):
            apply_resource(character=test_character)
    
    def test_apply_resource_without_current_hp_key(self):
        test_character = {"Strength": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            apply_resource(character=test_character)
    
    def test_apply_resource_without_strength_key(self):
        test_character = {"Current HP": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            apply_resource(character=test_character)
    
    def test_apply_resource_without_luck_key(self):
        test_character = {"Current HP": 1, "Strength": 1}
        with self.assertRaises(KeyError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_non_integer_health(self):
        test_character = {"Current HP": "1", "Strength": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_non_integer_strength(self):
        test_character = {"Current HP": 1, "Strength": "1", "Luck": 1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_non_integer_luck(self):
        test_character = {"Current HP": 1, "Strength": 1, "Luck": "1"}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_negative_health(self):
        test_character = {"Current HP": -1, "Strength": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_negative_strength(self):
        test_character = {"Current HP": 1, "Strength": -1, "Luck": 1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_negative_luck(self):
        test_character = {"Current HP": 1, "Strength": 1, "Luck": -1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    @patch("builtins.input", side_effect=["Health"])
    def test_apply_resource_with_health_upgrade_with_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 3, "Strength": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["HEALTH"])
    def test_apply_resource_with_health_upgrade_with_uppercase_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 3, "Strength": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["health"])
    def test_apply_resource_with_health_upgrade_with_lowercase_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 3, "Strength": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["H"])
    def test_apply_resource_with_health_upgrade_with_uppercase_shorthand(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 3, "Strength": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["h"])
    def test_apply_resource_with_health_upgrade_with_lowercase_shorthand(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 3, "Strength": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["Strength"])
    def test_apply_resource_with_strength_upgrade_with_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["STRENGTH"])
    def test_apply_resource_with_strength_upgrade_with_uppercase_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["strength"])
    def test_apply_resource_with_strength_upgrade_with_lowercase_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["S"])
    def test_apply_resource_with_strength_upgrade_with_uppercase_shorthand(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["s"])
    def test_apply_resource_with_strength_upgrade_with_lowercase_shorthand(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["Luck"])
    def test_apply_resource_with_luck_upgrade_with_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["LUCK"])
    def test_apply_resource_with_luck_upgrade_with_uppercase_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["luck"])
    def test_apply_resource_with_luck_upgrade_with_lowercase_full_word(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["L"])
    def test_apply_resource_with_luck_upgrade_with_uppercase_shorthand(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["l"])
    def test_apply_resource_with_luck_upgrade_with_lowercase_shorthand(self, _):
        get_upgrade_choice.return_value = 'l'
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)

