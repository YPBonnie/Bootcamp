from banking_pkg import account
from banking_pkg.account import show_balance, deposit, withdraw, logout

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#--------------------- Task 2: Registration Step ---------------------#
print("          === Automated Teller Machine ===          ")
reg_username = input("Enter name to register: ").capitalize()
reg_pin = input("Enter PIN: ")
balance = float(0) 
print(f"{reg_username} has been registered with a starting balane of ${balance}")

#--------------------- Task 3: Login Step ---------------------#
while True:
    print("LOGIN")
    input_username = input("Enter name: ").capitalize()
    input_pin = input("Enter PIN: ")

    # Check if input credentials match registration
    if input_username == reg_username and input_pin == reg_pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

"""
# Display the ATM menu
while True:
    print(atm_menu(input_username))
    user_option = input("Choose an option:")
"""
#--------------------- Task 4: The banking package ---------------------#
# Note: Block Lines 36-39 in order to run the following codes
while True:
    # Call atm_menu show the option table for the user
    atm_menu(input_username)

    user_option = input("Choose an option:")

    if user_option == "1":
        print("Current Balance: $" + str(show_balance(balance)))

    elif user_option == "2":
        balance = deposit(balance)   
        print("Current Balance: $" + str(balance))

    elif user_option == "3":
        balance = withdraw(balance)
        print("Current Balance: $" + str(balance))

    elif user_option == "4":
        logout(input_username)
        break

    else:
        print("Invalid option, please try again")
        continue

""" Unblock Lines 69-94 to complete Bonus Task 1 and 2. Bonus Task 3 is completed in ../banking_pkg/account.py. 
#------------- Bonus Task 1 --------------------#
print("          === Automated Teller Machine ===          ")

while True:

    reg_username = input("Enter name to register: ").strip() ## remove accidental spaces
    
    if len(reg_username) < 1 or len(reg_username) > 10:
        print("Invalid user name, please try again (1-10 characters only)")
    else:
        reg_username = reg_username.capitalize()
        print(f"Success! Welcome, {reg_username}.")
        break # exit the loop 

#------------- Bonus Task 2 --------------------#
while True:

    reg_pin = input("Enter PIN: ").strip() ## remove accidental spaces

    if len(reg_pin) != 4:
        print("Invalid user PIN, please try again (4 digits only) ")
    else:
        reg_pin = reg_pin
        print(f"Success! Welcome, {reg_pin}.")
        break

"""