import re

#-- Task: Challenge to valid username starts with a letter and contains only alphanumeric characters
def validate_username(username):
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*$'

    return bool(re.match(pattern, username))


#----------- Task 4. Login functionality --------------------
## Function of login functionality for my app
def login(database, username, password):
    #Challenge: case-insensitive for login
    username_lower = username.lower()
    if not validate_username(username_lower):
        print("Invalid username. Please enter a valid username that starts with a letter and only contains alphanumeric characters!")
        return ""
    elif username_lower in database:
        if password == database[username_lower]:
            print(f"Welcome back {username_lower}!")
            return username_lower
        else:
            print(f"Incorrect password for {username_lower}.")
            return ""
    else:
        print("User not found. Please register.")
        return ""

#----------- Task 5. Register functionality --------------------
# Function of user register functionality for my app
def register(database, username, password):
    # Challenge: case-insensitive for register
    username_lower = username.lower()

    if not validate_username(username_lower):
        print("Invalid username. Please enter a valid username that starts with a letter and only contains alphanumeric characters!")
        return ""
    # Challenge: validation for username and password
    elif len(password) < 5:
        print("Invalid password! Please enter password at least 5 characters.")
        return ""
    elif len(username_lower) > 10:
        print("Invalid username! Please enter usrername no more than 10 characters!")
        return ""
    elif username_lower in database:
        print(f"Username {username_lower} already registered!")
        return ""
    else:
        print(f"Username {username_lower} registered!")
        return username_lower

#----------- Task 6. Donate functionality --------------------
def donate(username):
    donation_amt = input("Enter amount to donate: ")
    try:
        # convert the input donation amount to a float
        amount = float(donation_amt)

        #Challenge: check if donation is positive
        if amount <= 0:
            print("Error: Donation must be greater than $0.00.")
            return ""

        # create the formatted string
        donation_string = f"{username} donated ${amount:.2f}"
        # print and return Thank you message.
        print(f"Thank you! {donation_string}")
        return donation_string

    except ValueError:
        # Catch the error when the user typed data other than numbers
        print("Error: Invalid input! Please enter a numeric value.")



