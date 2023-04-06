"""
Derek Woo
A01351415
"""


from unittest import TestCase
from character_management.manage_character import is_alive


class TestIsAlive(TestCase):
    def test_is_alive_with_character_that_has_plenty_of_hp(self):
        test_character = {"Current HP": 5}
        actual = is_alive(character=test_character)
        self.assertTrue(actual)

    def test_is_alive_with_character_that_has_1_hp(self):
        test_character = {"Current HP": 1}
        actual = is_alive(character=test_character)
        self.assertTrue(actual)

    def test_is_alive_with_character_that_is_not_alive_with_0HP(self):
        test_character = {"Current HP": 0}
        actual = is_alive(character=test_character)
        self.assertFalse(actual)

    def test_is_alive_with_character_that_is_not_alive_with_negative_HP(self):
        test_character = {"Current HP": -5}
        actual = is_alive(character=test_character)
        self.assertFalse(actual)
