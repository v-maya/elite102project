import information as info
import tkinter as tk

root = tk.Tk()
root.title("Banking Application")

# vars
log_in_ID = [-1] 

# def grid
root.columnconfigure((0,1), weight=1)
root.rowconfigure((0,1,2,3), weight=1)

# frame 1
frame1 = tk.Frame(root, width=600, height=100, bg="#badee1")
frame1.grid(row=0, column=0, columnspan=2)

def load_frame1():
    frame1.pack_propagate(False)

    options_label = tk.Label(frame1, text="Banking App", font=('Arial', 18), bg="#badee1")
    options_label.pack(padx=20, pady=10)

    currentuser_label = tk.Label(frame1, text=f"Current User ID: {log_in_ID}", font=('Arial', 12), bg="#badee1")
    currentuser_label.pack()

    # all buttons
    createacc_btn = tk.Button(root, text="Create Account", height=1, font=("Arial", 16), bg="#badee1",command=lambda:info.create_account())
    createacc_btn.grid(row=1, column=0, padx=10, pady=10)

    checkbal_btn = tk.Button(root, text="Check Balance", height=1, font=("Arial", 16), bg="#badee1", command=lambda:info.check_balance(log_in_ID))
    checkbal_btn.grid(row=1, column=1, padx=10, pady=10)

    login_btn = tk.Button(root, text="Log In", height=1, font=("Arial", 16), bg="#badee1", command=lambda:info.log_in())
    login_btn.grid(row=2, column=0, padx=10, pady=10)

    withdraw_btn = tk.Button(root, text="Withdraw", height=1, font=("Arial", 16), bg="#badee1", command=lambda:info.withdraw(log_in_ID))
    withdraw_btn.grid(row=2, column=1, padx=10, pady=10)

    modifyacc_btn = tk.Button(root, text="Modify Account", height=1, font=("Arial", 16), bg="#badee1", command=lambda:info.modify_account(log_in_ID))
    modifyacc_btn.grid(row=3, column=0, padx=10, pady=10)

    deposit_btn = tk.Button(root, text="Deposit", height=1, font=("Arial", 16), bg="#badee1", command=lambda:info.deposit(log_in_ID))
    deposit_btn.grid(row=3, column=1, padx=10, pady=10)

    deleteacc_btn = tk.Button(root, text="Delete Account", height=1, font=("Arial", 16), bg="#badee1", command=lambda:info.delete_account(log_in_ID))
    deleteacc_btn.grid(row=4, column=0, padx=10, pady=10)

    quit_btn = tk.Button(root, text="Quit", height=1, font=("Arial", 16), bg="#badee1", command=lambda:quit())
    quit_btn.grid(row=4, column=1, padx=10, pady=10)

# main
load_frame1()
root.mainloop()