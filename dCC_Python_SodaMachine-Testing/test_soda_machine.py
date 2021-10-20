from typing import Union
import unittest
from soda_machine import SodaMachine
from coins import *
from cans import *

class TestFillRegister(unittest.TestCase):
    """Tests for the fill_register method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that register list has len of 88"""
    def test_register_list_length(self):
        length = len(self.soda_machine.register)
        self.assertEqual(length, 88)

class TestFillInventory(unittest.TestCase):
    """Tests for the fill_inventory method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that inventory has len of 30"""
    def test_inventory_list_length(self):
        length = len(self.soda_machine.inventory)
        self.assertEqual(length, 30)

class TestGetCoinFromRegister(unittest.TestCase):
    """Tests for the get_coin_from_register method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that quarter can be returned from register"""
    def test_register_quarter(self):
        return_object = self.soda_machine.get_coin_from_register("Quarter")
        self.assertIsInstance(return_object, Quarter)

    """Test that dime can be returned from register"""
    def test_register_dime(self):
        return_object = self.soda_machine.get_coin_from_register("Dime")
        self.assertIsInstance(return_object, Dime)

    """Test that nickel can be returned from register"""
    def test_register_nickel(self):
        return_object = self.soda_machine.get_coin_from_register("Nickel")
        self.assertIsInstance(return_object, Nickel)

    """Test that penny can be returned from register"""
    def test_register_penny(self):
        return_object = self.soda_machine.get_coin_from_register("Penny")
        self.assertIsInstance(return_object, Penny)

    """Test that invalid string returns None"""
    def test_register_invalid_string(self):
        return_object = self.soda_machine.get_coin_from_register(" ")
        self.assertIsNone(return_object)

class TestRegisterHasCoin(unittest.TestCase):
    """Tests for the register_has_coin method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that quarter returns true"""
    def test_quarter_returns_true(self):
        value = self.soda_machine.register_has_coin("Quarter")
        self.assertTrue(value)

    """Test that dime returns true"""
    def test_dime_returns_true(self):
        value = self.soda_machine.register_has_coin("Dime")
        self.assertTrue(value)


    """Test that nickel returns true"""
    def test_nickel_returns_true(self):
        value = self.soda_machine.register_has_coin("Nickel")
        self.assertTrue(value)


    """Test that penny returns true"""
    def test_penny_returns_true(self):
        value = self.soda_machine.register_has_coin("Penny")
        self.assertTrue(value)


    """Test that invalid coin name returns false"""
    def test_invalid_name_return(self):
        value = self.soda_machine.register_has_coin(" ")
        self.assertFalse(value)


class TestDetermineChangeValue(unittest.TestCase):
    """Tests for the determine_change_value method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that method works with higher payment value"""
    def test_higher_total_payment(self):
        total_payment = 1.00
        selected_soda_price = .60
        change_given = self.soda_machine.determine_change_value(total_payment, selected_soda_price)

        self.assertEqual = (change_given, .40)

    """Test that method works with higher select_soda_price"""
    def test_higher_select_soda(self):
        total_payment = .50
        selected_soda_price = .60
        change_given = self.soda_machine.determine_change_value(total_payment, selected_soda_price)

        self.assertEqual(change_given, -.10)

    """Test that method works with two equal values"""
    def test_two_equal_values(self):
        total_payment = .50
        selected_soda_price = .50
        change_given = self.soda_machine.determine_change_value(total_payment, selected_soda_price)

        self.assertEqual(change_given, 0)


class TestCalculateCoinValue(unittest.TestCase):
    """Tests for the calculate_coin_value method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that the sum of all coin values is equal to .41"""
    def test_coin_value(self):
        quarter = Quarter()
        dime = Dime()
        nickel = Nickel()
        penny = Penny()

        sum_of_coins = quarter.value + dime.value + nickel.value + penny.value
        self.assertEqual = (sum_of_coins, .41)

    """Test that an empty list returns 0"""
    def test_empty_list(self):
        coin_list = []
        value = self.soda_machine.calculate_coin_value(coin_list)

        self.assertEqual(value, 0)

class TestGetInventorySoda(unittest.TestCase):
    """Tests for the get_inventory_soda method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that Cola returns same name"""
    def test_cola_name(self):
        value = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(value.name, 'Cola')

    """Test that OrangeSoda returns same name"""
    def test_orange_sode_name(self):
        
        value = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertEqual(value.name, 'Orange Soda')

    """Test that RootBeer returns same name"""
    def test_root_beer_name(self):
        value = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertEqual(value.name, 'Root Beer')

    """Test that invalid string 'Mountain Dew' returns None"""
    def test_invalid_string(self):
        value = self.soda_machine.get_inventory_soda('Mountain Dew')
        self.assertIsNone(value)

class TestReturnInventory(unittest.TestCase):
    """Tests for the return_inventory method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that Can object extends self.inventory list by 1"""
    def test_inventory_list_length(self):
        cola = Cola()
        original_length = len(self.soda_machine.inventory)

        self.soda_machine.return_inventory(cola)
        self.assertEqual(original_length + 1, len(self.soda_machine.inventory))

class TestDepositCoinsIntoRegister(unittest.TestCase):
    """Tests for the deposit_coins_into_register method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Tests that length of self.register increases by four with four coins added"""
    def test_register_list_length(self):
        quarter = Quarter()
        dime = Dime()
        nickel = Nickel()
        penny = Penny()

        coin_list = [quarter, dime, nickel, penny]
        self.soda_machine.deposit_coins_into_register(coin_list)

        self.assertEqual(len(self.soda_machine.register), 92)

if __name__ == '__main__':
    unittest.main()