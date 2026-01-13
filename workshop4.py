#Week 4 Assignment
#Bonnie D

class User:
    #--------- Task 1. Create User class -----------------------
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    #--------- Task 2. Add User class instance methods ---------
    def change_name(self, new_name):
        if new_name and len(new_name) >= 2 and len(new_name) <= 10 and (new_name != self.name):
            self.name = new_name
        return self.name

    def change_pin(self, new_pin):
        if new_pin and len(new_pin) == 4 and (new_pin != self.pin):
            self.pin = new_pin
        return self.pin

    def change_password(self, new_password):
        if new_password and len(new_password) >= 5 and (new_password != self.password):
            self.password = new_password
        return self.password

class BankUser(User):
    #--------- Task 3. Create BankUser subclass ---------
    def __init__(self, name, pin, password):
        #Use super() to initialize the name, pin, and password from the User class
        super().__init__(name, pin, password)
        # Add the balance attribute to the class of BankUser
        self.balance = 0
        # Bonus: add on_hold attribute
        self.on_hold = False

    def toggle_on_hold(self):
        self.on_hold = not self.on_hold
        print(f"Account hold status for {self.name}: {self.on_hold}")

    #--------- Task 4. Add BankUser class instance methods ---------
    def show_balance(self):
        print(f"{self.name} has an account balance of: ${self.balance:,.2f}")

    def withdraw(self, amount):
        if self.on_hold:
            print(f"{self.name}'s account is on hold. Transaction rejected.")
            return False
        
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount to withdraw.")
            return False
        
        if amount > 0.0:
            self.balance = float(self.balance) - float(amount)
            if self.balance < 0.0:
                self.balance = 0.0
        return self.balance
    
    def deposit(self, amount):
        if self.on_hold:
            print(f"{self.name}'s account is on hold. Transaction rejected.")
            return False

        if amount > 0.0:
            self.balance = float(self.balance) + float(amount)
        return self.balance
    
    #--------- Task 5. Transfer and request money ---------
    def transfer_money(self, recipient, amount):
        if self.on_hold:
            print(f"Transaction rejected: {self.name}'s account is on hold.")
            return False

        if recipient.on_hold:
            print(f"Transaction rejected: {recipient.name}'s account is on hold.")
            return False

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount entered.")
            return False

        if amount <= 0:
            print("Transfer amount must be positive.")
            return False

        if self.balance < amount:
            print("Insufficient funds for this transfer.")
            return False

        print(f"You are transferring ${amount} to {recipient.name}")

        print(f"\nAuthentication required for {self.name}")
        user_input_pin = input("Enter your PIN:")

        if str(self.pin) == user_input_pin:
            print("Transfer authorized")
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferring ${amount} to {recipient.name}")
            self.show_balance()
            recipient.show_balance()
            return True
        
        else:
            print("Invalid PIN. Transaction cancelled.")
            return False

    def request_money(self, loaner, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount entered.")
            return False

        if amount <= 0:
            print("Request amount must be positive.")
            return False

        if loaner.balance < amount:
            print(f"Request failed. {loaner.name} has insufficient funds.")
            return False
        
        print(f"You are requesting ${amount:.2f} from {loaner.name}")
        print(f"Authetication required")

        input_password = input("Enter your password:")
        input_loaner_password = input("Enter loaner password:")
        
        if (self.password == input_password) and (loaner.password == input_loaner_password):
            print("Request authorized!\n")
            loaner.balance -= amount
            self.balance += amount
            
            print(f"{loaner.name} sent ${amount:.2f} to {self.name}")

            self.show_balance()
            loaner.show_balance()
            return True
        else:
            print("Authefication failed. Please try again\n")
            return False
    
    def on_hold(self):
        return False


""" Driver Code for Task 1 """
#user1 = User("Bob", 1234, "password")
#print(f"{user1.name}  {user1.pin}  {user1.password}")
    
""" Driver Code for Task 2 """
#user1.change_name("Bobby")
#user1.change_pin("4321")
#user1.change_password("newpassword")
#print(f"{user1.name}  {user1.pin}  {user1.password}")

""" Driver Code for Task 3"""
#user2 = BankUser("Bob", 1234, "password")
#print(f"{user2.name}  {user2.pin}   {user2.password}   {user2.balance}")


""" Driver Code for Task 4"""
#bankuser1 = BankUser("Bob", 1234, "password")
#bankuser1.show_balance()
#bankuser1.deposit(1500.50)
#bankuser1.withdraw(500)


""" Driver Code for Task 5"""
user1 = BankUser("Alice", 5678, "alicepassword")
user2 = BankUser("Bob", 1234, "password")
user1.show_balance()
user2.show_balance()

#Deposit 5000 to user1
user1.deposit(5000)

#Show current balance for both users
user1.show_balance()
user2.show_balance()

#user1 transfer $500 to user2
user1.transfer_money(user2, 500)

#user 1 request $250 from user2
user1.request_money(user2, 250)

#Enter the following input argments when running the above codes:
#5678
#alicepassword
#password