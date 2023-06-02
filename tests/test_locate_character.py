from unittest import TestCase
from board_management.manage_locations import locate_character


class TestLocateCharacter(TestCase):
    def test_locate_character_with_non_dictionary_character(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = "Test Character"
        with self.assertRaises(TypeError):
            locate_character(board=test_board, character=test_character)

    def test_locate_character_with_non_dictionary_board(self):
        test_board = "String"
        test_character = {"X-coordinate": 2, "Y-coordinate": 2}
        with self.assertRaises(TypeError):
            locate_character(board=test_board, character=test_character)

    def test_locate_character_with_no_x_coordinate_key(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Y-coordinate": 0}
        with self.assertRaises(KeyError):
            locate_character(board=test_board, character=test_character)

    def test_locate_character_with_no_y_coordinate_key(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0}
        with self.assertRaises(KeyError):
            locate_character(board=test_board, character=test_character)

    def test_locate_character_with_non_integer_x_coordinate_value(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": "0", "Y-coordinate": 0}
        with self.assertRaises(TypeError):
            locate_character(board=test_board, character=test_character)

    def test_locate_character_with_non_integer_y_coordinate_value(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": "0"}
        with self.assertRaises(TypeError):
            locate_character(board=test_board, character=test_character)

    def test_locate_character_with_non_valid_character_location(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 6, "Y-coordinate": 3}
        with self.assertRaises(ValueError):
            locate_character(board=test_board, character=test_character)

    def test_locate_character_with_player_at_origin(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        locate_character(board=test_board, character=test_character)
        expected = {(0, 0): "[\x1b[92m'P'\x1b[0m]", (1, 0): "[   ]", (2, 0): "[   ]",
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
                    (0, 1): "[   ]", (1, 1): "[\x1b[92m'P'\x1b[0m]", (2, 1): "[   ]",
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
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[\x1b[92m'P'\x1b[0m]"}
        actual = test_board
        self.assertEqual(expected, actual)
