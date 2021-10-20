import unittest
from unittest.case import TestCase
from user_interface import validate_main_menu, try_parse_int, get_unique_can_names, display_payment_value, validate_coin_selection


class TestValidateMainMenu(unittest.TestCase):

    def test_check_if_true_is_returned_with_one(self):
        """Testing ValidateMainMenu() method sends back correct information 
        the Following methods do the same test, with the exception of the number changing"""
        number = 1
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (True, 1))

    def test_check_if_true_is_returned_with_two(self):
        number = 2
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (True, 2))

    def test_check_if_true_is_returned_with_three(self):
        number = 3
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (True, 3))

    def test_check_if_true_is_returned_with_four(self):
        number = 4
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (True, 4))

    def test_check_if_false_is_returned_with_five(self):
        number = 5
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (False, None))



if __name__ == '__main__':
    unittest.main()