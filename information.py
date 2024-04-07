# Testing of MySQL and experimenting, not yet adapted to needs

import mysql.connector
from datetime import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="h3110$iMn",
    database="banking"
    )

def create_account():
    cursor = connection.cursor()
    name = input("Enter your name: ")
    username = input("Create a username: ")
    password = input("Create a password: ")
    email = input("Enter your email: ")
    values = (name, username, password, email)
    add_data = ("INSERT INTO user_table (name, username, password, email) VALUES (%s, %s, %s, %s)")

    cursor.execute(add_data, values)
    connection.commit()

    print(cursor.rowcount, "record inserted.")

    cursor.close()
    connection.close()

def check_balance():
    pass

def deposit():
    pass

def withdraw():
    pass

def modify_account():
    pass

def delete_account():
    pass

