"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from character_management.character_level import apply_resource


class TestApplyResource(TestCase):
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

    @patch("builtins.input", side_effect=["l"])
    def test_apply_resource_with_luck_upgrade_with_lowercase_shorthand(self, _):
        test_character = {"Current HP": 0, "Strength": 0, "Luck": 0}
        apply_resource(character=test_character)
        expected = {"Current HP": 0, "Strength": 0, "Luck": 1}
        actual = test_character
        self.assertEqual(expected, actual)

