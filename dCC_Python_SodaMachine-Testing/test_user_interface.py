import unittest
from unittest.case import TestCase
from user_interface import validate_main_menu, try_parse_int, get_unique_can_names, display_payment_value, validate_coin_selection
from cans import OrangeSoda, Cola, RootBeer
from coins import Dime, Nickel, Quarter, Penny

class TestValidateMainMenu(unittest.TestCase):

    def test_check_if_true_is_returned_with_one(self):
        """Testing ValidateMainMenu() method sends back correct information 
        the Following methods do the same test, with the exception of the number changing"""
        number = 1
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (True, 1))
        """Pass"""

    def test_check_if_true_is_returned_with_two(self):
        number = 2
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (True, 2))
        """Pass"""

    def test_check_if_true_is_returned_with_three(self):
        number = 3
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (True, 3))
        """Pass"""

    def test_check_if_true_is_returned_with_four(self):
        number = 4
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (True, 4))
        """Pass"""

    def test_check_if_false_is_returned_with_five(self):
        number = 5
        result = validate_main_menu(number)
        bool_value = result[0]
        returned_number = result[1]
        self.assertEqual((bool_value, returned_number), (False, None))
        """Pass"""

class TestTryParseIntMethod(unittest.TestCase):
    """Testing to ensure proper value's are returned from the method"""

    def test_try_parse_returns_ten_as_int_when_given_ten_as_str(self):
        """Ensuring that the method will correctly return a value when it can be turned into a integer"""
        value = try_parse_int("10")
        self.assertEqual(value, 10)
        """Pass"""

    def test_try_parse_returns_zero(self):
        """Ensuring method will return a 0 when given a string that can not be parsed"""
        value = try_parse_int("hello")
        self.assertEqual(value, 0)
        """Pass"""

class TestGetUniqueCanNames(unittest.TestCase):
    """Testing to ensure method only returns Unique Names, or nothing"""

    def test_ensure_proper_names_returns_when_given_list(self):
        """Given a list, will the method return the unique names"""
        can1 = RootBeer()
        can2 = RootBeer()
        can3 = OrangeSoda()
        can4 = OrangeSoda()
        can5 = Cola()
        can6 = Cola()
        cans_list = [can1, can2, can3, can4, can5, can6]
        result = get_unique_can_names(cans_list)
        length = len(result) - 1
        self.assertEqual(length, 2)
        """Pass"""
    
    def test_ensure_when_given_empty_list_result_is_empty(self):
        """When the method is given a empty list, it returns a empty list"""
        cans_list = []
        result = get_unique_can_names(cans_list)
        self.assertEqual(result, cans_list)
        """Pass"""

class TestDisplayPaymentValue(unittest.TestCase):
    """Ensuring method returns total value of coins or zero if given none"""

    def test_does_return_value_of_coins_given(self):
        Q = Quarter()
        D = Dime()
        N = Nickel()
        P = Penny()
        wallet_list = [Q, D, N ,P]
        result = display_payment_value(wallet_list)
        self.assertEqual(result, .41)
        """Pass"""

    def test_does_return_zero_when_given_no_coins(self):
        money = []
        result = display_payment_value(money)
        self.assertEqual(result, 0)
        """Pass"""

class TestValidateCoinSelection(unittest.TestCase):
    """Testing to ensure Method returns proper tuple"""

    def test_validate_1_returns_true_and_coin(self):
        """Given 1 returns True and Quarter"""
        number = 1
        result = validate_coin_selection(number)
        bool_value = result[0]
        returned_coin = result[1]
        self.assertEqual((bool_value, returned_coin), (True, "Quarter"))
        """Pass"""
    
    def test_validate_2_returns_true_and_coin(self):
        """Given 2 returns True and Dime"""
        number = 2
        result = validate_coin_selection(number)
        bool_value = result[0]
        returned_coin = result[1]
        self.assertEqual((bool_value, returned_coin), (True, "Dime"))
        """Pass"""
    
    def test_validate_3_returns_true_and_coin(self):
        """Given 3 returns True and Nickel"""
        number = 3
        result = validate_coin_selection(number)
        bool_value = result[0]
        returned_coin = result[1]
        self.assertEqual((bool_value, returned_coin), (True, "Nickel"))
        """Pass"""
    
    def test_validate_4_returns_true_and_coin(self):
        """Given 4 returns True and Penny"""
        number = 4
        result = validate_coin_selection(number)
        bool_value = result[0]
        returned_coin = result[1]
        self.assertEqual((bool_value, returned_coin), (True, "Penny"))
        """Pass"""
    
    def test_validate_5_returns_true_and_done(self):
        """Given 5 returns True and Done"""
        number = 5
        result = validate_coin_selection(number)
        bool_value = result[0]
        returned_coin = result[1]
        self.assertEqual((bool_value, returned_coin), (True, "Done"))
        """Pass"""

    def test_validate_6_returns_False_and_None(self):
        """Given 6 returns False and None"""
        number = 6
        result = validate_coin_selection(number)
        bool_value = result[0]
        returned_coin = result[1]
        self.assertEqual((bool_value, returned_coin), (False, None))
        """Pass"""



if __name__ == '__main__':
    unittest.main()