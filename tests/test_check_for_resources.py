"""
Derek Woo
A01351415
"""


from unittest import TestCase
from character_management.character_level import check_for_resources


class TestCheckForResources(TestCase):
    def test_check_for_resources_with_a_resource(self):
        test_board = {(0, 0): "['R']", (1, 0): "[   ]"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = True
        actual = check_for_resources(board=test_board, character=test_character)
        self.assertEqual(expected, actual)

    def test_check_for_resources_with_no_resource(self):
        test_board = {(0, 0): "[   ]", (1, 0): "['R']"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0}
        expected = False
        actual = check_for_resources(board=test_board, character=test_character)
        self.assertEqual(expected, actual)
