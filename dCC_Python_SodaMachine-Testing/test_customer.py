import unittest
from customer import Customer
from coins import Dime
from cans import Cola
from cans import OrangeSoda
from cans import RootBeer

class TestGetWalletCoin(unittest.TestCase):
    """Initail Customer Class for get_wallet_coin Method() testing"""
    def setUp(self):
        self.customer = Customer()
        
    def test_quarter_string_returns_quarter_from_wallet(self):
        """Does Quarter return Quarter from get_wallet_coin method()"""
        result = self.customer.get_wallet_coin("Quarter")
        self.assertEqual(result.value, 0.25)
    
    def test_dime_string_returns_dime_from_wallet(self):
        """Does Dime return the value of Dime to hand"""
        result = self.customer.get_wallet_coin("Dime")
        self.assertEqual(result.value, 0.10)
    
    def test_nickel_string_returns_nickel_value_from_wallet(self):
        """Does the Nickel String return the value of Nickel back to hand"""
        result = self.customer.get_wallet_coin("Nickel")
        self.assertEqual(result.value, 0.05)
    
    def test_penny_string_returns_penny_value_to_hand(self):
        """Does penny string return the pennies value back to hand"""
        result = self.customer.get_wallet_coin("Penny")
        self.assertEqual(result.value, 0.01)
    
    def test_incorrect_input_returns_none(self):
        """Does a none Vaiable input return None to hand"""
        result = self.customer.get_wallet_coin("deeme")
        self.assertIsNone(result)

class TestAddCoinsToWallet(unittest.TestCase):
    """Tests for Customers add_coins_to_wallet method"""

    def setUp(self):
        self.customer = Customer()

    def test_length_of_money_list_adding(self):
        """Test to ensure length of Customers Wallet Money List went up by three"""
        dime_1 = Dime()
        dime_2 = Dime()
        dime_3 = Dime()
        coins_list = [dime_1, dime_2, dime_3]
        coins_list_length = len(self.customer.wallet.money)

        self.customer.add_coins_to_wallet(coins_list)
        method_list = self.customer.wallet.money
        
        self.assertEqual((coins_list_length + 3), len(method_list))

    def test_length_of_money_list_not_changing(self):
        """Test to ensure Customers wallet stays the same when passing a empty list"""
        coins_list = []
        coins_list_length = len(self.customer.wallet.money)

        self.customer.add_coins_to_wallet(coins_list)
        method_list = self.customer.wallet.money

        self.assertEqual((coins_list_length), len(method_list))

class TestAddCanToBackpack(unittest.TestCase):
    """Testing Add_can_to_backpack to check if it alters the backpacks purchased cans list"""
    def setUp(self):
        self.customer = Customer()   

    def test_adding_cola_to_backpack(self):
        """Ensuring that Soda is added to the purchased_cans list in backpack"""
        original = len(self.customer.backpack.purchased_cans)
        cola = Cola()
        self.customer.add_can_to_backpack(cola)
        altered_value = len(self.customer.backpack.purchased_cans)
        self.assertEqual((original + 1), altered_value)
    
    def test_adding_orange_soda_to_backpack(self):
        """Ensuring that Orange Soda is added to the purchased_cans list in backpack"""
        original = len(self.customer.backpack.purchased_cans)
        cola = OrangeSoda()
        self.customer.add_can_to_backpack(cola)
        altered_value = len(self.customer.backpack.purchased_cans)
        self.assertEqual((original + 1), altered_value)
    
    def test_adding_root_beer_to_backpack(self):
        """Ensuring that Root Beer is added to the purchased_cans list in backpack"""
        original = len(self.customer.backpack.purchased_cans)
        cola = RootBeer()
        self.customer.add_can_to_backpack(cola)
        altered_value = len(self.customer.backpack.purchased_cans)
        self.assertEqual((original + 1), altered_value)
    


if __name__ == '__main__':
    unittest.main()