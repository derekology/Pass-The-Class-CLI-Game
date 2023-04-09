"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from character_management.character_level import get_upgrade_choice


class TestGetUpgradeChoice(TestCase):
    @patch("builtins.input", side_effect=["Reeses"])
    def test_get_upgrade_choice_with_reeses_upgrade_with_full_word(self, _):
        expected = "Reeses"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["REESES"])
    def test_get_upgrade_choice_reeses_upgrade_with_uppercase_full_word(self, _):
        expected = "Reeses"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["reeses"])
    def test_get_upgrade_choice_with_reeses_upgrade_with_lowercase_full_word(self, _):
        expected = "Reeses"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["R"])
    def test_get_upgrade_choice_with_reeses_upgrade_with_uppercase_shorthand(self, _):
        expected = "R"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["r"])
    def test_get_upgrade_choice_with_reeses_upgrade_with_lowercase_shorthand(self, _):
        expected = "R"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Smarts"])
    def test_get_upgrade_choice_with_smarts_upgrade_with_full_word(self, _):
        expected = "Smarts"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["SMARTS"])
    def test_get_upgrade_choice_with_smarts_upgrade_with_uppercase_full_word(self, _):
        expected = "Smarts"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["smarts"])
    def test_get_upgrade_choice_with_smarts_upgrade_with_lowercase_full_word(self, _):
        expected = "Smarts"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["S"])
    def test_get_upgrade_choice_with_smarts_upgrade_with_uppercase_shorthand(self, _):
        expected = "S"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["s"])
    def test_get_upgrade_choice_with_smarts_upgrade_with_lowercase_shorthand(self, _):
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
