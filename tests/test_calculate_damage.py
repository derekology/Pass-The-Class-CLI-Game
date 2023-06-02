from unittest import TestCase
from unittest.mock import patch
from combat_management.foe_combat import calculate_damage


class TestCalculateDamage(TestCase):
    def test_calculate_damage_with_non_dictionary_fighter(self):
        test_fighter = "String"
        with self.assertRaises(TypeError):
            calculate_damage(fighter=test_fighter)

    def test_calculate_damage_with_fighter_without_smarts_key(self):
        test_fighter = {"Luck": 1}
        with self.assertRaises(KeyError):
            calculate_damage(fighter=test_fighter)

    def test_calculate_damage_with_fighter_without_luck_key(self):
        test_fighter = {"Smarts": 1}
        with self.assertRaises(KeyError):
            calculate_damage(fighter=test_fighter)

    def test_calculate_damage_with_fighter_with_non_integer_smarts(self):
        test_fighter = {"Smarts": "1", "Luck": 1}
        with self.assertRaises(ValueError):
            calculate_damage(fighter=test_fighter)

    def test_calculate_damage_with_fighter_with_non_integer_luck(self):
        test_fighter = {"Smarts": 1, "Luck": "1"}
        with self.assertRaises(ValueError):
            calculate_damage(fighter=test_fighter)

    def test_calculate_damage_with_fighter_with_negative_smarts(self):
        test_fighter = {"Smarts": -1, "Luck": 1}
        with self.assertRaises(ValueError):
            calculate_damage(fighter=test_fighter)

    def test_calculate_damage_with_fighter_with_negative_luck(self):
        test_fighter = {"Smarts": 1, "Luck": -1}
        with self.assertRaises(ValueError):
            calculate_damage(fighter=test_fighter)

    @patch("random.randint", side_effect=[0.0])
    def test_calculate_damage_with_lowest_random_number_and_zero_attributes(self, _):
        test_fighter = {"Smarts": 0, "Luck": 0}
        expected = 0
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[0.0])
    def test_calculate_damage_with_lowest_random_number_and_one_attributes(self, _):
        test_fighter = {"Smarts": 1, "Luck": 1}
        expected = 0
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[0.0])
    def test_calculate_damage_with_lowest_random_number_and_greater_than_one_attributes(self, _):
        test_fighter = {"Smarts": 5, "Luck": 5}
        expected = 4
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[0.5])
    def test_calculate_damage_with_middle_random_number_and_zero_attributes(self, _):
        test_fighter = {"Smarts": 0, "Luck": 0}
        expected = 0
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[0.5])
    def test_calculate_damage_with_middle_random_number_and_one_attributes(self, _):
        test_fighter = {"Smarts": 1, "Luck": 1}
        expected = 1
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[0.5])
    def test_calculate_damage_with_middle_random_number_and_greater_than_one_attributes(self, _):
        test_fighter = {"Smarts": 5, "Luck": 5}
        expected = 4
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[1.0])
    def test_calculate_damage_with_highest_random_number_and_zero_attributes(self, _):
        test_fighter = {"Smarts": 0, "Luck": 0}
        expected = 0
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[1.0])
    def test_calculate_damage_with_highest_random_number_and_one_attributes(self, _):
        test_fighter = {"Smarts": 1, "Luck": 1}
        expected = 1
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)

    @patch("random.randint", side_effect=[1.0])
    def test_calculate_damage_with_highest_random_number_and_greater_than_one_attributes(self, _):
        test_fighter = {"Smarts": 5, "Luck": 5}
        expected = 4
        actual = calculate_damage(fighter=test_fighter)
        self.assertEqual(expected, actual)
