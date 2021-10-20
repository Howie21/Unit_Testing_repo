from typing import Union
import unittest
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """Tests for the fill_register method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that register list has len of 88"""
    def test_register_list_length(self):
        pass

class TestFillInventory(unittest.TestCase):
    """Tests for the fill_inventory method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that inventory has len of 30"""
    def test_inventory_list_length(self):
        pass

class TestGetCoinFromRegister(unittest.TestCase):
    """Tests for the get_coin_from_register method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that quarter can be returned from register"""
    def test_register_quarter(self):
        pass

    """Test that dime can be returned from register"""
    def test_register_dime(self):
        pass

    """Test that nickel can be returned from register"""
    def test_register_nickel(self):
        pass

    """Test that penny can be returned from register"""
    def test_register_penny(self):
        pass

    """Test that invalid string returns None"""
    def test_register_invalid_string(self):
        pass

class TestRegisterHasCoin(unittest.TestCase):
    """Tests for the register_has_coin method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that quarter returns true"""
    def test_quarter_returns_true(self):
        pass

    """Test that dime returns true"""
    def test_dime_returns_true(self):
        pass

    """Test that nickel returns true"""
    def test_nickel_returns_true(self):
        pass

    """Test that penny returns true"""
    def test_penny_returns_true(self):
        pass

    """Test that invalid coin name returns false"""
    def test_invalid_name_return(self):
        pass

class TestDetermineChangeValue(unittest.TestCase):
    """Tests for the determine_change_value method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that method works with higher payment value"""
    def test_higher_total_payment(self):
        pass

    """Test that method works with higher select_soda_price"""
    def test_higher_select_soda(self):
        pass

    """Test that method works with two equal values"""
    def test_two_equal_values(self):
        pass

class TestCalculateCoinValue(unittest.TestCase):
    """Tests for the calculate_coin_value method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that the sum of all coin values is equal to .41"""
    def test_coin_value(self):
        pass

    """Test that an empty list returns 0"""
    def test_empty_list(self):
        pass

class TestGetInventorySoda(unittest.TestCase):
    """Tests for the get_inventory_soda method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that Cola returns same name"""
    def test_cola_name(self):
        pass

    """Test that OrangeSoda returns same name"""
    def test_orange_sode_name(self):
        pass

    """Test that RootBeer returns same name"""
    def test_root_beer_name(self):
        pass

    """Test that invalid string 'Mountain Dew' returns None"""
    def test_invalid_string(self):
        pass

class TestReturnInventory(unittest.TestCase):
    """Tests for the return_inventory method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Test that Can object extends self.inventory list by 1"""
    def test_inventory_list_length(self):
        pass

class TestDepositCoinsIntoRegister(unittest.TestCase):
    """Tests for the deposit_coins_into_register method in SodaMachine class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    """Tests that length of self.register increases by four with four coins added"""
    def test_register_list_length(self):
        pass