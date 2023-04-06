"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from board_management.manage_locations import mark_resources


class TestMarkResources(TestCase):
    def test_mark_resources_with_zero_resource_tiles(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        mark_resources(board=test_board, character=test_character, special_tiles=0)
        expected = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(0, 0)]])
    def test_mark_resources_with_one_resource_tile(self, _):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        mark_resources(board=test_board, character=test_character, special_tiles=1)
        expected = {(0, 0): "['R']", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(0, 0), (1, 1), (2, 2)]])
    def test_mark_resources_with_some_resource_tiles(self, _):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        mark_resources(board=test_board, character=test_character, special_tiles=3)
        expected = {(0, 0): "['R']", (1, 0): "[   ]", (2, 0): "[   ]",
                    (0, 1): "[   ]", (1, 1): "['R']", (2, 1): "[   ]",
                    (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "['R']"}
        actual = test_board
        self.assertEqual(expected, actual)

    @patch("random.sample", side_effect=[[(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (2, 2)]])
    def test_mark_resources_with_maximum_resource_tiles(self, _):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        mark_resources(board=test_board, character=test_character, special_tiles=8)
        expected = {(0, 0): "['R']", (1, 0): "['R']", (2, 0): "['R']",
                    (0, 1): "['R']", (1, 1): "['R']", (2, 1): "['R']",
                    (0, 2): "['R']", (1, 2): "[   ]", (2, 2): "['R']"}
        actual = test_board
        self.assertEqual(expected, actual)
