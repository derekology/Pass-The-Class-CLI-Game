from unittest import TestCase
from character_management.manage_character import is_alive
from unittest.mock import patch
import io


class TestIsAlive(TestCase):
    def test_is_alive_with_character_that_has_plenty_of_reeses(self):
        test_character = {"Reeses": 5}
        actual = is_alive(character=test_character)
        self.assertTrue(actual)

    def test_is_alive_with_character_that_has_1_reeses(self):
        test_character = {"Reeses": 1}
        actual = is_alive(character=test_character)
        self.assertTrue(actual)

    def test_is_alive_with_character_that_is_not_alive_with_0_reeses(self):
        test_character = {"Reeses": 0}
        actual = is_alive(character=test_character)
        self.assertFalse(actual)

    def test_is_alive_with_character_that_is_not_alive_with_negative_reeses(self):
        test_character = {"Reeses": -5}
        actual = is_alive(character=test_character)
        self.assertFalse(actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_is_alive_with_alive_message(self, mock_output):
        test_character = {"Reeses": 5}
        is_alive(character=test_character, alive_message="Test Alive Message")
        expected = "Test Alive Message\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_is_alive_with_not_alive_message(self, mock_output):
        test_character = {"Reeses": 0}
        is_alive(character=test_character, not_alive_message="Test Not Alive Message")
        expected = "Test Not Alive Message\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
