"""
Derek Woo
A01351415
"""


from unittest import TestCase
from board_management.manage_board import draw_board
from unittest.mock import patch
import io


class TestDrawBoard(TestCase):
    def test_draw_board_with_invalid_key_value(self):
        test_board = {(0, 0): 123, (1, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]"}
        with self.assertRaises(TypeError):
            draw_board(board=test_board, columns=2)

    def test_draw_board_with_key_of_less_than_two_integers(self):
        test_board = {(0): "[   ]", (1, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]"}
        with self.assertRaises(TypeError):
            draw_board(board=test_board, columns=2)

    def test_draw_board_with_key_of_more_than_two_integers(self):
        test_board = {(0, 0, 0): "[   ]", (1, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]"}
        with self.assertRaises(TypeError):
            draw_board(board=test_board, columns=2)

    def test_draw_board_with_non_integer_key(self):
        test_board = {(0, "a"): "[   ]", (1, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]"}
        with self.assertRaises(TypeError):
            draw_board(board=test_board, columns=2)

    def test_draw_board_with_non_integer_column(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]"}
        with self.assertRaises(TypeError):
            draw_board(board=test_board, columns="a")

    def test_draw_board_with_one_column(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]"}
        with self.assertRaises(ValueError):
            draw_board(board=test_board, columns=1)

    def test_draw_board_with_zero_columns(self):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]"}
        with self.assertRaises(ValueError):
            draw_board(board=test_board, columns=0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_board_with_smallest_board_possible(self, mock_print):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]"}
        draw_board(board=test_board, columns=2)
        expected = "[   ][   ]\n" \
                   "[   ][   ]\n"
        actual = mock_print.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_board_with_large_board(self, mock_print):
        test_board = {(0, 0): "[   ]", (1, 0): "[   ]", (2, 0): "[   ]", (3, 0): "[   ]",
                      (0, 1): "[   ]", (1, 1): "[   ]", (2, 1): "[   ]", (3, 1): "[   ]",
                      (0, 2): "[   ]", (1, 2): "[   ]", (2, 2): "[   ]", (3, 2): "[   ]",
                      (0, 3): "[   ]", (1, 3): "[   ]", (2, 3): "[   ]", (3, 3): "[   ]"}
        draw_board(board=test_board, columns=4)
        expected = "[   ][   ][   ][   ]\n" \
                   "[   ][   ][   ][   ]\n" \
                   "[   ][   ][   ][   ]\n" \
                   "[   ][   ][   ][   ]\n"
        actual = mock_print.getvalue()
        self.assertEqual(expected, actual)
