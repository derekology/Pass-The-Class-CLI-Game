"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from character_management.character_level import get_upgrade_choice


class TestGetUpgradeChoice(TestCase):

    @patch("builtins.input", side_effect=["Health"])
    def test_get_upgrade_choice_with_health_upgrade_with_full_word(self, _):
        expected = "Health"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["HEALTH"])
    def test_get_upgrade_choice_health_upgrade_with_uppercase_full_word(self, _):
        expected = "Health"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["health"])
    def test_get_upgrade_choice_with_health_upgrade_with_lowercase_full_word(self, _):
        expected = "Health"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["H"])
    def test_get_upgrade_choice_with_health_upgrade_with_uppercase_shorthand(self, _):
        expected = "H"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["h"])
    def test_get_upgrade_choice_with_health_upgrade_with_lowercase_shorthand(self, _):
        expected = "H"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Strength"])
    def test_get_upgrade_choice_with_strength_upgrade_with_full_word(self, _):
        expected = "Strength"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["STRENGTH"])
    def test_get_upgrade_choice_with_strength_upgrade_with_uppercase_full_word(self, _):
        expected = "Strength"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["strength"])
    def test_get_upgrade_choice_with_strength_upgrade_with_lowercase_full_word(self, _):
        expected = "Strength"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["S"])
    def test_get_upgrade_choice_with_strength_upgrade_with_uppercase_shorthand(self, _):
        expected = "S"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["s"])
    def test_get_upgrade_choice_with_strength_upgrade_with_lowercase_shorthand(self, _):
        expected = "S"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Luck"])
    def test_get_upgrade_choice_with_luck_upgrade_with_full_word(self, _):
        expected = "Luck"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["LUCK"])
    def test_get_upgrade_choice_with_luck_upgrade_with_uppercase_full_word(self, _):
        expected = "Luck"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["luck"])
    def test_get_upgrade_choice_with_luck_upgrade_with_lowercase_full_word(self, _):
        expected = "Luck"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["L"])
    def test_get_upgrade_choice_with_luck_upgrade_with_uppercase_shorthand(self, _):
        expected = "L"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["l"])
    def test_get_upgrade_choice_with_luck_upgrade_with_lowercase_shorthand(self, _):
        expected = "L"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)
