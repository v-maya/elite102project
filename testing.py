"""
Unit testing for main functions in information.py
"""

import information as info
import unittest

class TestFunctions(unittest.TestCase):

    def test_log_in(self):
        self.assertIsNotNone(info.log_in(), True)

    def test_withdraw_with_insufficient_balance(self):
        self.assertIsNone(info.withdraw(info.log_in()), True)

    def test_deposit(self):
        self.assertIsNone(info.deposit(info.log_in()), True)

if __name__ == "__main__":
    unittest.main()