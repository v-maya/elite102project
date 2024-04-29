"""
Unit testing for main functions in information.py
"""

import information as info
import unittest
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="h3110$iMn",
    database="banking"
    )

class TestFunctions(unittest.TestCase):
    
    # tests whether the log_in function returns a value (the user_id)
    def test_log_in(self):
        self.assertIsNotNone(info.log_in(), True)

    def test_withdraw_with_insufficient_balance(self): # has to be tested with user ID 10 with a withdrawl of 100
        cursor = connection.cursor()
        query = ("SELECT BALANCE FROM user_table WHERE id = 10")
        cursor.execute(query)
        myresult = cursor.fetchone()
        smyresult = str(myresult[0])
        smyresult = float(smyresult)

        info.withdraw(info.log_in())

        query2 = ("SELECT BALANCE FROM user_table WHERE id = 10")
        cursor.execute(query2)
        myresult2 = cursor.fetchone()
        smyresult2 = str(myresult2[0])
        smyresult2 = float(smyresult2)

        connection.commit()
        cursor.close()
        self.assertEqual(smyresult, smyresult2) # checks to see if balance remains unchanged after insufficient funds

    def test_deposit(self): # has to be tested with user ID 6 with any deposit
        cursor = connection.cursor()
        query = ("SELECT BALANCE FROM user_table WHERE id = 6")
        cursor.execute(query)
        myresult = cursor.fetchone()
        smyresult = str(myresult[0])
        smyresult = float(smyresult)
        connection.commit() # I don't understand why this is needed here while the other one doesn't need it.
    
        info.deposit(info.log_in())

        query2 = ("SELECT BALANCE FROM user_table WHERE id = 6")
        cursor.execute(query2)
        myresult2 = cursor.fetchone()
        smyresult2 = str(myresult2[0])
        smyresult2 = float(smyresult2)

        connection.commit()
        cursor.close()
        self.assertNotEqual(smyresult, smyresult2) # checks to see if balance changed after depositing

if __name__ == "__main__":
    unittest.main()