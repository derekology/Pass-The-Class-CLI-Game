from unittest import TestCase
from unittest.mock import patch
from board_management.guessing_game import guessing_game


class TestGuessingGame(TestCase):
    @patch("random.randint", side_effect=[2])
    @patch("builtins.input", side_effect=["2"])
    def test_guessing_game_after_a_correct_guess(self, _, __):
        actual = guessing_game()
        self.assertTrue(actual)

    @patch("random.randint", side_effect=[2])
    @patch("builtins.input", side_effect=["3"])
    def test_guessing_game_after_an_incorrect_guess(self, _, __):
        actual = guessing_game()
        self.assertFalse(actual)
