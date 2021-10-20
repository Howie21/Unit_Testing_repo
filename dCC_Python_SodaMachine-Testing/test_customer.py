import unittest
from customer import Customer

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


if __name__ == '__main__':
    unittest.main()