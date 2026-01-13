#----------------- Task 1: Show homepage & initialize app data -------------------------#
#Import show_homepage from donations_pkg/homepage.py
from donations_pkg.homepage import show_homepage, show_donations
from donations_pkg.user import login, register, donate, validate_username

# Declare simulated database
database = {"admin": "password123"}

#Declare donations and assign it to be an empty string
donations = []

#Declare authorized_user as an empty string
authorized_user = ""

#----------------- Task 2 -------------------------#
#if not authorized_user:
#    show_homepage()
#    print("You must be logged in to donate")
#else:
#    print(f"Logged in as:{authorized_user}")


#----------------- Task 3. Handle user input -------------------------#

while True:
    show_homepage()
    # Task 2. Homepage and initialization set up
    if not authorized_user:
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

    # prompt user to select one the options
    user_choice = input("Choose an option: ")

    if user_choice == "1":
        # Task 4: Login functionality
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")
        authorized_user = login(database, input_username, input_password)

    elif user_choice == "2":
        # Task 5: Registration functionality
        input_username = input("Enter username: ")
        input_password = input("Enter password: ")

        res_register = register(database, input_username, input_password)

        if res_register != "":
            database[res_register] = input_password
            authorized_user = res_register
            print(f"Success! {authorized_user} is now logged in.")

    elif user_choice == "3":
        # Task 6: Donation functionality
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            if donation_string:
                donations.append(donation_string)

    elif user_choice == "4":
        # Task 7: Show donations functionality
        show_donations(donations)

    elif user_choice == "5":
        print("Leaving DonateMe...")
        break 

    else:
        print("Please select a valid option.")




