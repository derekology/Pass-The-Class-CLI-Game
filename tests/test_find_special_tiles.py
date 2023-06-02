from unittest import TestCase
from unittest.mock import patch
from board_management.manage_locations import find_special_tiles


class TestFindSpecialTiles(TestCase):
    def test_find_special_tiles_with_non_dictionary_character(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = "Test"
        with self.assertRaises(TypeError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=3)

    def test_find_special_tiles_with_non_dictionary_board(self):
        test_board = "Test Board"
        test_character = {"Level": 1, "X-coordinate": "0", "Y-coordinate": 0}
        with self.assertRaises(TypeError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=3)

    def test_find_special_tiles_with_non_integer_number_of_resource_tiles(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        with self.assertRaises(TypeError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles="3")

    def test_find_special_tiles_with_no_x_coordinate_key(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "Y-coordinate": 0}
        with self.assertRaises(KeyError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=3)

    def test_find_special_tiles_with_no_y_coordinate_key(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0}
        with self.assertRaises(KeyError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=3)

    def test_find_special_tiles_with_non_integer_x_coordinate_value(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": "0", "Y-coordinate": 0}
        with self.assertRaises(TypeError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=3)

    def test_find_special_tiles_with_non_integer_y_coordinate_value(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": "0"}
        with self.assertRaises(TypeError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=3)

    def test_find_special_tiles_with_non_valid_character_location(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 6, "Y-coordinate": 3}
        with self.assertRaises(ValueError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=3)

    def test_find_special_tiles_with_too_many_resource_tiles(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        with self.assertRaises(ValueError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=8)

    def test_find_special_tiles_with_negative_resource_tiles(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        with self.assertRaises(ValueError):
            find_special_tiles(board=test_board, character=test_character, resource_tiles=-1)

    def test_find_special_tiles_with_zero_resource_tiles_with_no_boss(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        find_special_tiles(board=test_board, character=test_character, resource_tiles=0)
        expected = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(0, 0)]])
    @patch("random.random", side_effect=[0])
    def test_find_special_tiles_with_one_resource_tile_with_no_boss(self, _, __):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        find_special_tiles(board=test_board, character=test_character, resource_tiles=1)
        expected = {(0, 0): "[\x1b[36m'L'\x1b[0m]", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(0, 0), (1, 1), (2, 2)]])
    @patch("random.random", side_effect=[0])
    def test_find_special_tiles_with_some_resource_tiles_with_no_boss(self, _, __):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        find_special_tiles(board=test_board, character=test_character, resource_tiles=3)
        expected = {(0, 0): "[\x1b[36m'L'\x1b[0m]", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "[\x1b[36m'L'\x1b[0m]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[\x1b[36m'L'\x1b[0m]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (2, 2)]])
    @patch("random.random", side_effect=[0])
    def test_find_special_tiles_with_maximum_resource_tiles_with_no_boss(self, _, __):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        find_special_tiles(board=test_board, character=test_character, resource_tiles=7)
        expected = {(0, 0): "[   ]", (1, 0): "[\x1b[36m'L'\x1b[0m]", (2, 0): "[\x1b[36m'L'\x1b[0m]",
                    (0, 1): "[\x1b[36m'L'\x1b[0m]", (1, 1): "[\x1b[36m'L'\x1b[0m]", (2, 1): "[\x1b[36m'L'\x1b[0m]",
                    (0, 2): "[\x1b[36m'L'\x1b[0m]", (1, 2): "[   ]", (2, 2): "[\x1b[36m'L'\x1b[0m]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.random", side_effect=[10])
    @patch("random.randint", side_effect=[0])
    def test_find_special_tiles_with_zero_resource_tiles_with_boss(self, _, __):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        find_special_tiles(board=test_board, character=test_character, resource_tiles=0)
        expected = {(0, 0): "[   ]", (1, 0): "[\x1b[31m'E'\x1b[0m]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(0, 1)]])
    @patch("random.random", side_effect=[10])
    @patch("random.randint", side_effect=[0])
    def test_find_special_tiles_with_one_resource_tile_with_a_boss(self, _, __, ___):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        find_special_tiles(board=test_board, character=test_character, resource_tiles=1)
        expected = {(0, 0): "[   ]", (1, 0): "[\x1b[31m'E'\x1b[0m]", (2, 0): "[   ]",
                    (0, 1): "[\x1b[36m'L'\x1b[0m]", (1, 1): "[   ]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(0, 1), (1, 1), (2, 2)]])
    @patch("random.random", side_effect=[10])
    @patch("random.randint", side_effect=[0])
    def test_find_special_tiles_with_some_resource_tiles_with_a_boss(self, _, __, ___):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        find_special_tiles(board=test_board, character=test_character, resource_tiles=3)
        expected = {(0, 0): "[   ]", (1, 0): "[\x1b[31m'E'\x1b[0m]", (2, 0): "[   ]",
                    (0, 1): "[\x1b[36m'L'\x1b[0m]", (1, 1): "[\x1b[36m'L'\x1b[0m]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[\x1b[36m'L'\x1b[0m]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(2, 0), (0, 1), (1, 1), (1, 2), (2, 1), (0, 2), (2, 2)]])
    @patch("random.random", side_effect=[10])
    @patch("random.randint", side_effect=[0])
    def test_find_special_tiles_with_maximum_resource_tiles_with_a_boss(self, _, __, ___):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"Level": 1, "X-coordinate": 0, "Y-coordinate": 0}
        find_special_tiles(board=test_board, character=test_character, resource_tiles=7)
        expected = {(0, 0): "[   ]", (1, 0): "[\x1b[31m'E'\x1b[0m]", (2, 0): "[\x1b[36m'L'\x1b[0m]",
                    (0, 1): "[\x1b[36m'L'\x1b[0m]", (1, 1): "[\x1b[36m'L'\x1b[0m]", (2, 1): "[\x1b[36m'L'\x1b[0m]",
                    (0, 2): "[\x1b[36m'L'\x1b[0m]", (1, 2): "[\x1b[36m'L'\x1b[0m]", (2, 2): "[\x1b[36m'L'\x1b[0m]"}
        actual = test_board
        self.assertEqual(expected, actual)
