from unittest import TestCase
from character_management.character_movement import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_with_first_valid_move_in_a_corner(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9a"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = validate_move(board=test_board, character=test_character, direction="Right")
        self.assertTrue(actual)

    def test_validate_move_with_second_valid_move_in_a_corner(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9b"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = validate_move(board=test_board, character=test_character, direction="Down")
        self.assertTrue(actual)

    def test_validate_move_with_first_invalid_move_in_a_corner(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9c"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = validate_move(board=test_board, character=test_character, direction="Up")
        self.assertFalse(actual)

    def test_validate_move_with_second_invalid_move_in_a_corner(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9d"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        actual = validate_move(board=test_board, character=test_character, direction="Left")
        self.assertFalse(actual)

    def test_validate_move_with_first_valid_move_from_the_middle(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9e"}
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = validate_move(board=test_board, character=test_character, direction="Up")
        self.assertTrue(actual)

    def test_validate_move_with_second_valid_move_from_the_middle(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9f"}
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = validate_move(board=test_board, character=test_character, direction="Right")
        self.assertTrue(actual)

    def test_validate_move_with_third_valid_move_from_the_middle(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9g"}
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = validate_move(board=test_board, character=test_character, direction="Down")
        self.assertTrue(actual)

    def test_validate_move_with_fourth_valid_move_from_the_middle(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9h"}
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = validate_move(board=test_board, character=test_character, direction="Left")
        self.assertTrue(actual)

    def test_validate_move_with_first_valid_move_from_a_side(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9i"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 1}
        actual = validate_move(board=test_board, character=test_character, direction="Up")
        self.assertTrue(actual)

    def test_validate_move_with_second_valid_move_from_a_side(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9j"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 1}
        actual = validate_move(board=test_board, character=test_character, direction="Right")
        self.assertTrue(actual)

    def test_validate_move_with_third_valid_move_from_a_side(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9k"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 1}
        actual = validate_move(board=test_board, character=test_character, direction="Down")
        self.assertTrue(actual)

    def test_validate_move_with_first_invalid_move_from_a_side(self):
        test_board = {(0, 0): "Room 1", (0, 1): "Room 2", (0, 2): "Room 3",
                      (1, 0): "Room 4", (1, 1): "Room 5", (1, 2): "Room 6",
                      (2, 0): "Room 7", (2, 1): "Room 8", (2, 2): "Room 9l"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 1}
        actual = validate_move(board=test_board, character=test_character, direction="Left")
        self.assertFalse(actual)
