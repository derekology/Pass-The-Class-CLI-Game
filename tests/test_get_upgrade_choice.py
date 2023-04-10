"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
import io
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
        expected = "Reeses"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["r"])
    def test_get_upgrade_choice_with_reeses_upgrade_with_lowercase_shorthand(self, _):
        expected = "Reeses"
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
        expected = "Smarts"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["s"])
    def test_get_upgrade_choice_with_smarts_upgrade_with_lowercase_shorthand(self, _):
        expected = "Smarts"
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
        expected = "Luck"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["l"])
    def test_get_upgrade_choice_with_luck_upgrade_with_lowercase_shorthand(self, _):
        expected = "Luck"
        actual = get_upgrade_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Reeses"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_reeses_upgrade_with_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["REESES"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_reeses_upgrade_with_uppercase_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["reeses"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_reeses_upgrade_with_lowercase_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["R"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_reeses_upgrade_with_uppercase_shorthand_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["r"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_reeses_upgrade_with_lowercase_shorthand_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Smarts"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_smarts_upgrade_with_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["SMARTS"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_smarts_upgrade_with_uppercase_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["smarts"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_smarts_upgrade_with_lowercase_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["S"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_smarts_upgrade_with_uppercase_shorthand_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["s"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_smarts_upgrade_with_lowercase_shorthand_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["Luck"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_luck_upgrade_with_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["LUCK"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_luck_upgrade_with_uppercase_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["luck"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_luck_upgrade_with_lowercase_full_word_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["L"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_luck_upgrade_with_uppercase_shorthand_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["l"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_upgrade_choice_with_luck_upgrade_with_lowercase_shorthand_check_printed_string(self, mock_output, _):
        get_upgrade_choice()
        expected = "*Sound of you finding a study resource*\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
