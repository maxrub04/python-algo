import unittest
from trading_tools import calculate_profit
from trading_tools import calculate_loss


class MyTestCase(unittest.TestCase):
    def test_profit(self):
        self.assertEqual(calculate_profit(100,150),50,"Profit should be 50")

    def test_loss(self):
        self.assertEqual(calculate_profit(200,150),-50,"Loss should be 50")

    def test_no_profit_no_loss(self):
        self.assertEqual(calculate_profit(150,150),0,"Break even should be 0")

    def test_wrong_type(self):
        self.assertIsNone(calculate_profit("hello",150))


if __name__ == '__main__':
    unittest.main()
