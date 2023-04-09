"""
Derek Woo
A01351415
"""


from unittest import TestCase
from utilities.check_for_special_tile import check_for_special_tile


class TestCheckForSpecialTile(TestCase):
    def test_check_for_special_tile_with_a_non_dictionary_character(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = "String"
        with self.assertRaises(TypeError):
            check_for_special_tile(board=test_board, character=test_character, boss=False)

    def test_check_for_special_tile_with_a_non_dictionary_board(self):
        test_board = "Test Board"
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        with self.assertRaises(TypeError):
            check_for_special_tile(board=test_board, character=test_character, boss=False)

    def test_check_for_special_tile_with_no_x_coordinate_key(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Y-coordinate": 0}
        with self.assertRaises(KeyError):
            check_for_special_tile(board=test_board, character=test_character, boss=False)

    def test_check_for_special_tile_with_no_y_coordinate_key(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0}
        with self.assertRaises(KeyError):
            check_for_special_tile(board=test_board, character=test_character, boss=False)

    def test_check_for_special_tile_with_non_integer_x_coordinate_value(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": "0", "Y-coordinate": 0}
        with self.assertRaises(TypeError):
            check_for_special_tile(board=test_board, character=test_character, boss=False)

    def test_check_for_special_tile_with_non_integer_y_coordinate_value(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": "0"}
        with self.assertRaises(TypeError):
            check_for_special_tile(board=test_board, character=test_character, boss=False)

    def test_check_for_special_tile_with_non_valid_character_location(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 6, "Y-coordinate": 3}
        with self.assertRaises(ValueError):
            check_for_special_tile(board=test_board, character=test_character, boss=False)

    def test_check_for_special_tile_with_a_resource_but_no_boss_looking_for_resource(self):
        test_board = {(0, 0): "[\x1b[36m'L'\x1b[0m]", (1, 0): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = True
        actual = check_for_special_tile(board=test_board, character=test_character, boss=False)
        self.assertEqual(expected, actual)

    def test_check_for_special_tile_with_no_resource_and_no_boss_looking_for_resource(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[\x1b[36m'L'\x1b[0m]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = check_for_special_tile(board=test_board, character=test_character, boss=False)
        self.assertEqual(expected, actual)

    def test_check_for_special_tile_with_a_boss_but_no_resource_looking_for_resource(self):
        test_board = {(0, 0): "[\x1b[31m'E'\x1b[0m]", (1, 0): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = check_for_special_tile(board=test_board, character=test_character, boss=False)
        self.assertEqual(expected, actual)

    def test_check_for_special_tile_with_no_boss_and_no_resource_looking_for_resource(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[\x1b[31m'E'\x1b[0m]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = check_for_special_tile(board=test_board, character=test_character, boss=False)
        self.assertEqual(expected, actual)
        self.assertEqual(expected, actual)

    def test_check_for_special_tile_with_a_resource_but_no_boss_looking_for_boss(self):
        test_board = {(0, 0): "[\x1b[36m'L'\x1b[0m]", (1, 0): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = check_for_special_tile(board=test_board, character=test_character, boss=True)
        self.assertEqual(expected, actual)

    def test_check_for_special_tile_with_no_resource_and_no_boss_looking_for_boss(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[\x1b[36m'L'\x1b[0m]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = check_for_special_tile(board=test_board, character=test_character, boss=True)
        self.assertEqual(expected, actual)

    def test_check_for_special_tile_with_a_boss_but_no_resource_looking_for_boss(self):
        test_board = {(0, 0): "[\x1b[31m'E'\x1b[0m]", (1, 0): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = True
        actual = check_for_special_tile(board=test_board, character=test_character, boss=True)
        self.assertEqual(expected, actual)

    def test_check_for_special_tile_with_no_boss_and_no_resource_looking_for_boss(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[\x1b[31m'E'\x1b[0m]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = check_for_special_tile(board=test_board, character=test_character, boss=True)
        self.assertEqual(expected, actual)
