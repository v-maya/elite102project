'''
Contains main functions of app

Future plan: move all functions into functions.py
main.py for test cases
information.py for data handling

Make a separate file for unit testing after creating the UI
'''
import information as info

# This ID verifies who is logged in and who can access what data. Set to -1 on start to avoid accessing accounts
# without logging in.
log_in_ID = [-1] 

# Display and select action
def menu():
    global log_in_ID
    print("\
           ----- Menu -----\n\
           1. Create account\n\
           2. Log in\n\
           3. Check balance\n\
           4. Deposit\n\
           5. Withdraw\n\
           6. Modify account\n\
           7. Delete account\n\
           8. Quit\
          ")
    
    try:
        option = int(input("What would you like to do? "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        option = int(input("What would you like to do? "))

    global log_in_ID
    match option:
        case 1:
            info.create_account()
        case 2:
            log_in_ID = info.log_in()
        case 3:
            info.check_balance(log_in_ID)
        case 4:
            info.deposit(log_in_ID)
        case 5:
            info.withdraw(log_in_ID)
        case 6:
            info.modify_account(log_in_ID)
        case 7:
            info.delete_account(log_in_ID)
        case 8:
            info.connection.close()
            quit()
        case _:
            print("Whoops! Please enter a valid option number.")

# Welcome message for users
def welcome():
    print("Hello! Welcome to the banking app.")
    # Already has a quit statement within menu()
    while True:
        menu()

# Main program
welcome()