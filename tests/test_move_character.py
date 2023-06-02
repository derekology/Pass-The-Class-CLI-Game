from unittest import TestCase
from character_management.character_movement import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_up(self):
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character(character=test_character, direction="Up")
        expected = (1, 0)
        actual = (test_character["X-coordinate"], test_character["Y-coordinate"])
        self.assertEqual(expected, actual)

    def test_move_character_right(self):
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character(character=test_character, direction="Right")
        expected = (2, 1)
        actual = (test_character["X-coordinate"], test_character["Y-coordinate"])
        self.assertEqual(expected, actual)

    def test_move_character_down(self):
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character(character=test_character, direction="Down")
        expected = (1, 2)
        actual = (test_character["X-coordinate"], test_character["Y-coordinate"])
        self.assertEqual(expected, actual)

    def test_move_character_Left(self):
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character(character=test_character, direction="Left")
        expected = (0, 1)
        actual = (test_character["X-coordinate"], test_character["Y-coordinate"])
        self.assertEqual(expected, actual)
