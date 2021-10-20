import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):
    """Test to ensure fill_wallet method in Wallet Class fills wallet to 88"""
    def setUp(self):
        self.wallet = Wallet()

    def test_fill_wallet(self):
        length_of_list = len(self.wallet.money)
        self.assertEqual(length_of_list, 88)

if __name__ == '__main__':
    unittest.main()