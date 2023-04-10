"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
import io
from character_management.character_level import apply_resource, get_upgrade_choice


class TestApplyResource(TestCase):
    def test_apply_resource_with_non_dictionary_character(self):
        test_character = "String"
        with self.assertRaises(TypeError):
            apply_resource(character=test_character)
    
    def test_apply_resource_without_reeses_key(self):
        test_character = {"Smarts": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            apply_resource(character=test_character)
    
    def test_apply_resource_without_smarts_key(self):
        test_character = {"Reeses": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            apply_resource(character=test_character)
    
    def test_apply_resource_without_luck_key(self):
        test_character = {"Reeses": 1, "Smarts": 1}
        with self.assertRaises(KeyError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_non_integer_reeses(self):
        test_character = {"Reeses": "1", "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_non_integer_smarts(self):
        test_character = {"Reeses": 1, "Smarts": "1", "Luck": 1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_non_integer_luck(self):
        test_character = {"Reeses": 1, "Smarts": 1, "Luck": "1"}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_negative_reeses(self):
        test_character = {"Reeses": -1, "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_negative_smarts(self):
        test_character = {"Reeses": 1, "Smarts": -1, "Luck": 1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    def test_apply_resource_with_negative_luck(self):
        test_character = {"Reeses": 1, "Smarts": 1, "Luck": -1}
        with self.assertRaises(ValueError):
            apply_resource(character=test_character)
    
    @patch("builtins.input", side_effect=["Reeses"])
    def test_apply_resource_with_reeses_upgrade_with_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 3, "Smarts": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["REESES"])
    def test_apply_resource_with_reeses_upgrade_with_uppercase_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 3, "Smarts": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["reeses"])
    def test_apply_resource_with_reeses_upgrade_with_lowercase_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 3, "Smarts": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["R"])
    def test_apply_resource_with_reeses_upgrade_with_uppercase_shorthand(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 3, "Smarts": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["r"])
    def test_apply_resource_with_reeses_upgrade_with_lowercase_shorthand(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 3, "Smarts": 0, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["Smarts"])
    def test_apply_resource_with_smarts_upgrade_with_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["SMARTS"])
    def test_apply_resource_with_smarts_upgrade_with_uppercase_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["smarts"])
    def test_apply_resource_with_smarts_upgrade_with_lowercase_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["S"])
    def test_apply_resource_with_smarts_upgrade_with_uppercase_shorthand(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["s"])
    def test_apply_resource_with_smarts_upgrade_with_lowercase_shorthand(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 1, "Luck": 0}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["Luck"])
    def test_apply_resource_with_luck_upgrade_with_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["LUCK"])
    def test_apply_resource_with_luck_upgrade_with_uppercase_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["luck"])
    def test_apply_resource_with_luck_upgrade_with_lowercase_full_word(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)
    
    @patch("builtins.input", side_effect=["L"])
    def test_apply_resource_with_luck_upgrade_with_uppercase_shorthand(self, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["l"])
    def test_apply_resource_with_luck_upgrade_with_lowercase_shorthand(self, _):
        get_upgrade_choice.return_value = 'l'
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Reeses": 0, "Smarts": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Reeses"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_apply_resource_with_reese_upgrade_check_printed_string(self, mock_output, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = "Sound of you upgrading yourself"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch("builtins.input", side_effect=["Smarts"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_apply_resource_with_smarts_upgrade_check_printed_string(self, mock_output, _):
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = "Sound of you upgrading yourself"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=["l"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_apply_resource_with_luck_upgrade_check_printed_string(self, mock_output, _):
        get_upgrade_choice.return_value = 'Luck'
        test_character = {"Reeses": 0, "Smarts": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = "Sound of you upgrading yourself"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
