"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
import io
from character_management.character_movement import get_user_choice


class TestGetUserChoice(TestCase):
    @patch("builtins.input", side_effect=["W"])
    def test_get_user_choice_with_a_valid_up_direction_as_an_uppercase_letter(self, _):
        expected = "Up"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["D"])
    def test_get_user_choice_with_a_valid_right_direction_as_an_uppercase_letter(self, _):
        expected = "Right"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["S"])
    def test_get_user_choice_with_a_valid_down_direction_as_an_uppercase_letter(self, _):
        expected = "Down"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["A"])
    def test_get_user_choice_with_a_valid_left_direction_as_an_uppercase_letter(self, _):
        expected = "Left"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["w"])
    def test_get_user_choice_with_a_valid_up_direction_as_an_lowercase_letter(self, _):
        expected = "Up"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["d"])
    def test_get_user_choice_with_a_valid_right_direction_as_an_lowercase_letter(self, _):
        expected = "Right"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["s"])
    def test_get_user_choice_with_a_valid_down_direction_as_an_lowercase_letter(self, _):
        expected = "Down"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["a"])
    def test_get_user_choice_with_a_valid_left_direction_as_an_lowercase_letter(self, _):
        expected = "Left"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Sideways", "W"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_with_an_invalid_direction(self, mock_print, _):
        get_user_choice()
        expected = "Invalid direction entered."
        actual = mock_print.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', side_effect=["Sideways", "W"])
    def test_get_user_choice_with_an_valid_direction_after_an_invalid_one(self, _):
        expected = "Up"
        actual = get_user_choice()
        self.assertEqual(expected, actual)
