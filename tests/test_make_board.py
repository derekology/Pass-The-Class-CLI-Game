"""
Derek Woo
A01351415
"""


from unittest import TestCase
from board_management.manage_board import make_board


class TestSimpleGame(TestCase):
    def test_make_board_with_non_integer_row_and_column_size(self):
        with self.assertRaises(TypeError):
            make_board("bcd", "abc")

    def test_make_board_with_non_integer_row_size(self):
        with self.assertRaises(TypeError):
            make_board("abc", 3)

    def test_make_board_with_non_integer_column_size(self):
        with self.assertRaises(TypeError):
            make_board(3, "abc")

    def test_make_board_with_invalid_row_and_column_size(self):
        with self.assertRaises(ValueError):
            make_board(1, 1)

    def test_make_board_with_invalid_row_size(self):
        with self.assertRaises(ValueError):
            make_board(1, 2)

    def test_make_board_with_invalid_column_size(self):
        with self.assertRaises(ValueError):
            make_board(2, 1)

    def test_make_board_with_unequal_columns_and_rows(self):
        with self.assertRaises(ValueError):
            make_board(3, 4)

    def test_make_board_with_smallest_board_possible(self):
        expected = {(0, 0): "[   ]", (0, 1): "[   ]", (1, 0): "[   ]", (1, 1): "[   ]"}
        actual = make_board(2, 2)
        self.assertEqual(expected, actual)

    def test_make_board_with_large_board(self):
        expected = {(0, 0): "[   ]", (0, 1): "[   ]", (0, 2): "[   ]", (0, 3): "[   ]",
                    (1, 0): "[   ]", (1, 1): "[   ]", (1, 2): "[   ]", (1, 3): "[   ]",
                    (2, 0): "[   ]", (2, 1): "[   ]", (2, 2): "[   ]", (2, 3): "[   ]",
                    (3, 0): "[   ]", (3, 1): "[   ]", (3, 2): "[   ]", (3, 3): "[   ]"}
        actual = make_board(4, 4)
        self.assertEqual(expected, actual)
