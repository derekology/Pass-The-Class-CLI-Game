"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
import io
from combat_management.foe_combat import fight_foe


class TestFightFoe(TestCase):
    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_non_dictionary_character(self, _):
        test_character = "String"
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": 1, "Luck": 1}
        with self.assertRaises(TypeError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_non_dictionary_foe(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": 1, "Luck": 1}
        test_foe = "String"
        with self.assertRaises(TypeError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_missing_reeses(self, _):
        test_character = {"Name": "test_character", "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_missing_smarts(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_missing_luck(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_missing_reeses(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Smarts": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_missing_smarts(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Luck": 1}
        with self.assertRaises(KeyError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_missing_luck(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": 1}
        with self.assertRaises(KeyError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_having_non_integer_reeses(self, _):
        test_character = {"Name": "test_character", "Reeses": "1", "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": "1", "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_having_non_integer_smarts(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": "1", "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": "1", "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_having_non_integer_luck(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": 1, "Luck": "1"}
        test_foe = {"Name": "test_foe", "Reeses": "1", "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_having_negative_reeses(self, _):
        test_character = {"Name": "test_character", "Reeses": -1, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": "1", "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_having_negative_smarts(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": -1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": "1", "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_character_having_negative_luck(self, _):
        test_character = {"Name": "test_character", "Reeses": 1, "Smarts": 1, "Luck": -1}
        test_foe = {"Name": "test_foe", "Reeses": "1", "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_having_non_integer_reeses(self, _):
        test_character = {"Name": "test_character", "Reeses": "1", "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": "1", "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_having_non_integer_smarts(self, _):
        test_character = {"Name": "test_character", "Reeses": "1", "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": "1", "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_having_non_integer_luck(self, _):
        test_character = {"Name": "test_character", "Reeses": "1", "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": 1, "Luck": "1"}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_having_negative_reeses(self, _):
        test_character = {"Name": "test_character", "Reeses": "1", "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": -1, "Smarts": 1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_having_negative_smarts(self, _):
        test_character = {"Name": "test_character", "Reeses": "1", "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": -1, "Luck": 1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 0])
    def test_fight_foe_with_foe_having_negative_luck(self, _):
        test_character = {"Name": "test_character", "Reeses": "1", "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 1, "Smarts": 1, "Luck": -1}
        with self.assertRaises(ValueError):
            fight_foe(character=test_character, foe=test_foe)

    @patch("random.randint", side_effect=[0, 100])
    def test_fight_foe_with_character_dying(self, _):
        test_character = {"Name": "test_character", "Reeses": 10, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 10, "Smarts": 1, "Luck": 1}
        fight_foe(character=test_character, foe=test_foe)
        self.assertLessEqual(test_character["Reeses"], 0)

    @patch("random.randint", side_effect=[0, 100])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_fight_foe_with_character_dying_printed_infliction_message(self, mock_output, _):
        test_character = {"Name": "test_character", "Reeses": 10, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 10, "Smarts": 1, "Luck": 1}
        fight_foe(character=test_character, foe=test_foe)
        expected = "You eat 10 pieces of Reeses due to stress from the test_foe."
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch("random.randint", side_effect=[100])
    def test_fight_foe_with_opponent_dying(self, _):
        test_character = {"Name": "test_character", "Reeses": 10, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 10, "Smarts": 1, "Luck": 1}
        fight_foe(character=test_character, foe=test_foe)
        self.assertLessEqual(test_foe["Reeses"], 0)

    @patch("random.randint", side_effect=[100])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_fight_foe_with_opponent_dying_printed_infliction_message(self, mock_output, _):
        test_character = {"Name": "test_character", "Reeses": 10, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 10, "Smarts": 1, "Luck": 1}
        fight_foe(character=test_character, foe=test_foe)
        expected = "You complete 10 questions on the test_foe."
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch("random.randint", side_effect=[100])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_fight_foe_with_opponent_dying_printed_victory_message(self, mock_output, _):
        test_character = {"Name": "test_character", "Reeses": 10, "Smarts": 1, "Luck": 1}
        test_foe = {"Name": "test_foe", "Reeses": 10, "Smarts": 1, "Luck": 1}
        fight_foe(character=test_character, foe=test_foe)
        expected = "You passed the test_foe!"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
