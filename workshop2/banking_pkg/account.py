# Function to display user's account balance
def show_balance(balance):
    return balance

## Function to display user's account balance after deposit
def deposit(balance):
    amount = input("Enter amount to deposit: ")
    current_balance = balance + float(amount)
    return show_balance(current_balance)

## Function to display user's account balance after withdraw
## Bonus Task 3
def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    amount = float(amount)

    if amount > balance:
        print("Error! You don't have sufficient funds!")
        return balance
    
    current_balance = balance - amount

    return show_balance(current_balance)

## Function to logout
def logout(name):
    print(f"Goodbye {name}!")
