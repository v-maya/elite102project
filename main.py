'''
Contains main functions of app

Future plan: move all functions into functions.py
main.py for test cases
information.py for data handling
'''
# Display and select action
def menu():
    print("\
           ----- Menu -----\n\
           1. Create account\n\
           2. Check balance\n\
           3. Deposit\n\
           4. Withdraw\n\
           5. Modify account\n\
           6. Delete account\n\
          ")
    option = int(input("What would you like to do? "))
    match option:
        case 1:
            print("Create account")
        case 2:
            print("Check balance")
        case 3:
            print("Deposit")
        case 4:
            print("Withdraw")
        case 5:
            print("Modify account")
        case 6:
            print("Delete account")
        case _:
            print("Whoops!")

# Welcome message for users
def welcome():
    print("Hello! Welcome to the banking app.")
    menu()

welcome()