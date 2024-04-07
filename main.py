'''
Contains main functions of app

Future plan: move all functions into functions.py
main.py for test cases
information.py for data handling
'''
import information as info

# This ID verifies who is logged in and who can access what data. Set to -1 on start to avoid accessing accounts
# without logging in.
log_in_ID = -1

# Display and select action
def menu():
    print("\
           ----- Menu -----\n\
           1. Create account\n\
           2. Log in\n\
           3. Check balance\n\
           4. Deposit\n\
           5. Withdraw\n\
           6. Modify account\n\
           7. Delete account\n\
          ")
    option = int(input("What would you like to do? "))
    match option:
        case 1:
            info.create_account()
        case 2:
            global log_in_ID
            log_in_ID = info.log_in()
        case 3:
            print("Deposit")
        case 4:
            print("Withdraw")
        case 5:
            print("Modify account")
        case 6:
            info.modify_account(log_in_ID)
        case 7:
            info.delete_account(log_in_ID)
        case _:
            print("Whoops!")

# Welcome message for users
def welcome():
    print("Hello! Welcome to the banking app.")
    while True:
        menu()

welcome()
print(log_in_ID)