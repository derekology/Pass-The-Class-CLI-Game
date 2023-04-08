"""
Derek Woo
A01351415
"""


from unittest import TestCase
from unittest.mock import patch
from combat_management.manage_foes import create_foe


class TestCreateFoe(TestCase):
    def test_create_foe_with_non_dictionary_fighter(self):
        test_character = "String"
        with self.assertRaises(TypeError):
            create_foe(character=test_character)

    def test_create_foe_with_fighter_without_health_key(self):
        test_character = {"Strength": 1}
        with self.assertRaises(KeyError):
            create_foe(character=test_character)

    def test_create_foe_with_fighter_without_strength_key(self):
        test_character = {"Current HP": 1}
        with self.assertRaises(KeyError):
            create_foe(character=test_character)

    def test_create_foe_with_fighter_with_non_integer_health(self):
        test_character = {"Current HP": "1", "Strength": 1}
        with self.assertRaises(ValueError):
            create_foe(character=test_character)

    def test_create_foe_with_fighter_with_non_integer_strength(self):
        test_character = {"Current HP": 1, "Strength": "1"}
        with self.assertRaises(ValueError):
            create_foe(character=test_character)

    def test_create_foe_with_fighter_with_negative_health(self):
        test_character = {"Current HP": -1, "Strength": 1}
        with self.assertRaises(ValueError):
            create_foe(character=test_character)

    def test_create_foe_with_fighter_with_negative_strength(self):
        test_character = {"Current HP": 1, "Strength": -1}
        with self.assertRaises(ValueError):
            create_foe(character=test_character)

    @patch("random.choice", side_effect=["pop quiz"])
    @patch("random.random", side_effect=[0, 0])
    @patch("random.randint", side_effect=[1])
    def test_create_foe_with_minimum_random_values_and_non_boss(self, _, __, ___):
        test_character = {"Current HP": 1, "Strength": 1}
        expected = {"Name": "pop quiz", "Current HP": 1, "Strength": 1, "Level": 0, "Luck": 1}
        actual = create_foe(character=test_character, boss=False)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["pop quiz"])
    @patch("random.random", side_effect=[0.5, 0.5])
    @patch("random.randint", side_effect=[2])
    def test_create_foe_with_middle_random_values_and_non_boss(self, _, __, ___):
        test_character = {"Current HP": 1, "Strength": 1}
        expected = {"Name": "pop quiz", "Current HP": 2, "Strength": 2, "Level": 0, "Luck": 2}
        actual = create_foe(character=test_character, boss=False)
        self.assertEqual(expected, actual)

    @patch("random.choice", side_effect=["pop quiz"])
    @patch("random.random", side_effect=[1, 1])
    @patch("random.randint", side_effect=[3])
    def test_create_foe_with_maximum_random_values_and_non_boss(self, _, __, ___):
        test_character = {"Current HP": 1, "Strength": 1}
        expected = {"Name": "pop quiz", "Current HP": 4, "Strength": 3, "Level": 1, "Luck": 3}
        actual = create_foe(character=test_character, boss=False)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[1])
    def test_create_foe_with_boss(self, _):
        test_character = {"Current HP": 1, "Strength": 1}
        expected = {"Name": "Final exam", "Current HP": 15, "Strength": 7, "Level": 4, "Luck": 1}
        actual = create_foe(character=test_character, boss=True)
        self.assertEqual(expected, actual)
