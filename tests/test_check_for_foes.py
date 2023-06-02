from unittest import TestCase
from unittest.mock import patch
from combat_management.manage_foes import check_for_foes


class TestCheckForFoes(TestCase):
    @patch("random.randint", side_effect=[1])
    def test_check_for_foes_when_foe_is_encountered_by_rolling_one(self, _):
        actual = check_for_foes()
        self.assertTrue(actual)

    @patch("random.randint", side_effect=[2])
    def test_check_for_foes_when_foe_is_not_encountered_by_rolling_two(self, _):
        actual = check_for_foes()
        self.assertFalse(actual)

    @patch("random.randint", side_effect=[3])
    def test_check_for_foes_when_foe_is_not_encountered_by_rolling_three(self, _):
        actual = check_for_foes()
        self.assertFalse(actual)

    @patch("random.randint", side_effect=[4])
    def test_check_for_foes_when_foe_is_not_encountered_by_rolling_four(self, _):
        actual = check_for_foes()
        self.assertFalse(actual)
