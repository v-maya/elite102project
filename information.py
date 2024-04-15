#all python functions for main

import mysql.connector
#from datetime import datetime

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="h3110$iMn",
    database="banking"
    )

# Allows the user to create an account saved onto an SQL table. IDs correspond with each user
# and is used for identification.
# This function is currently working.
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

# User types in their username and password and the function retrieves the corresponding ID to be used
# in checking and making transactions.
# This function is currently working. Returns the user ID as a list.
def log_in():
    cursor = connection.cursor(buffered=True)
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    values = (username, password)
    sql = ("SELECT ID FROM user_table WHERE username=%s AND password=%s")
    cursor.execute(sql, values)
    connection.commit()
    myresult = cursor.fetchone()
    list = []
    if myresult is None:
        print("Incorrect credentials. Try again!")
        return -1
    for x in myresult:
        if isinstance(x, int):
            print("Logged in!")
            list.append(x)
            print(list)
            return list
    cursor.close()

# User checks their current balance expressed as a decimal in the form of 0.00.
# This function is currently working.
def check_balance(user_id):
    cursor = connection.cursor(buffered=True)
    while user_id == [-1]:
        print("Whoops! Please log in first.")
        user_id = log_in()
    cursor = connection.cursor()
    value = user_id
    check_data = ("SELECT BALANCE FROM user_table WHERE id=%s")
    cursor.execute(check_data, value)
    print(cursor.rowcount, "record found.")
    myresult = cursor.fetchone()
    if myresult != None:
        print("Your current account balance is $" + str(myresult[0]))
    #for x in myresult:
    #    print(x)
    connection.commit()
    cursor.close()

# Using another table, meant to track deposits that the user makes. Automatically updates user balance.
# May want to update function such that only data from the tables is being used rather than the pure user input.
# Reason why transaction data is stored on another table is so the user can check their transaction history
# in part to the usage of a foreign uid key.
# This function is currently working. NOT USING FOREIGN KEY
def deposit(user_id):
    cursor = connection.cursor(buffered=True)
    while user_id == [-1]:
        print("Whoops! Please log in first.")
        user_id = log_in()
    try:
        amount = float(input("How much would you like to deposit? "))
    except ValueError:
        print("Whoops! Please enter a decimal number.")
        amount = float(input("How much would you like to deposit? "))
    value = user_id

    get_balance = ("SELECT BALANCE FROM user_table WHERE id=%s")
    cursor.execute(get_balance, value)
    myresult = cursor.fetchone()
    smyresult = str(myresult[0])
    smyresult = float(smyresult)

    newresult = smyresult + amount
    snewresult = str(newresult)
    user_id = str(user_id[0])

    query = ("UPDATE user_table SET BALANCE = %s WHERE id=%s")
    cursor.execute(query, (snewresult, user_id))
    
    connection.commit()
    print(cursor.rowcount, "records changed.")
    cursor.close()

# Using another table, meant to track withdrawals that the user makes. Automatically updates user balance.
# May want to update function such that only data from the tables is being used rather than the pure user input.
# Reason why transaction data is stored on another table is so the user can check their transaction history
# in part to the usage of a foreign uid key.
# This function is currently working. NOT USING FOREUGN KEY
def withdraw(user_id):
    cursor = connection.cursor(buffered=True)
    while user_id == [-1]:
        print("Whoops! Please log in first.")
        user_id = log_in()
    try:
        amount = float(input("How much would you like to withdraw? "))
    except ValueError:
        print("Whoops! Please enter a decimal number.")
        amount = float(input("How much would you like to withdraw? "))
    value = user_id

    get_balance = ("SELECT BALANCE FROM user_table WHERE id=%s")
    cursor.execute(get_balance, value)
    myresult = cursor.fetchone()
    smyresult = str(myresult[0])
    smyresult = float(smyresult)

    newresult = smyresult - amount
    if newresult < 0:
        print("Insufficient funds!")
        return

    snewresult = str(newresult)
    user_id = str(user_id[0])

    query = ("UPDATE user_table SET BALANCE = %s WHERE id=%s")
    cursor.execute(query, (snewresult, user_id))

    connection.commit()
    print(cursor.rowcount, "records changed.")
    cursor.close()

# User enters in new data to update their existing account. User ID is needed to verify identity.
# This function is currently working. user_id is converted to an integer within the function.
def modify_account(user_id):
    while user_id == [-1]:
        print("Whoops! Please log in first.")
        user_id = log_in()
    cursor = connection.cursor()
    name = input("Enter new name: ")
    username = input("Create new username: ")
    password = input("Create new password: ")
    email = input("Enter your new email: ")
    integer = -1
    for item in user_id:
        integer = item
    values = (name, username, password, email, integer)
    add_data = ("UPDATE user_table SET name = %s, username = %s, password = %s, email = %s WHERE ID = %s")
    cursor.execute(add_data, values)
    connection.commit()
    print(cursor.rowcount, "record changed.")
    cursor.close()

# Once logged in, the user will be able to delete their own account. However, the function should also work
# if the user chooses to log in upon start up.
# This function is currently working. user_id is expected as a list in this SQL line.
def delete_account(user_id):
    while user_id == [-1]:
        print("Whoops! Please log in first.")
        user_id = log_in()
    cursor = connection.cursor()
    value = user_id
    remove_data = ("DELETE FROM user_table WHERE id=%s")
    cursor.execute(remove_data, value)
    connection.commit()
    print(cursor.rowcount, "record deleted.")
    cursor.close()