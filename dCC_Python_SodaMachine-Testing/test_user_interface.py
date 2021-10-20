import unittest
from unittest.case import TestCase
from user_interface import validate_main_menu, try_parse_int, get_unique_can_names, display_payment_value, validate_coin_selection


class TestValidateMainMenu(unittest.TestCase):

    def test_check_if_true_is_returned_with_one():
        number = 1
        (bool_one , result) = validate_main_menu(number)
        TestCase.assertEqual((bool_one, result), (True, number))

if __name__ == '__main__':
    unittest.main()