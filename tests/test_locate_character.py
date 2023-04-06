"""
Derek Woo
A01351415
"""


from unittest import TestCase
from baord_management.manage_locations import locate_character


class TestLocateCharacter(TestCase):
    def test_locate_character_with_player_at_origin(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        locate_character(board=test_board, character=test_character)
        expected = {(0, 0): "['P']", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        actual = test_board
        self.assertEqual(expected, actual)

    def test_locate_character_with_player_at_middle_of_board(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        locate_character(board=test_board, character=test_character)
        expected = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "['P']", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        actual = test_board
        self.assertEqual(expected, actual)

    def test_locate_character_with_player_at_bottom_right_of_board(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 2, "Y-coordinate": 2}
        locate_character(board=test_board, character=test_character)
        expected = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "['P']"}
        actual = test_board
        self.assertEqual(expected, actual)
