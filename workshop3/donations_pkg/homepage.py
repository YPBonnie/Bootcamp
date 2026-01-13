#Define the function to show homepage
def show_homepage():
    print("")
    print("         === DonateMe Homepage ===           ")
    print("---------------------------------------------")
    print("| 1. Login           | 2. Register           ")
    print("---------------------------------------------")
    print("| 3. Donate          | 4. Show Donations     ")
    print("---------------------------------------------")
    print("                 5. Exit                     ")
    print("---------------------------------------------")


#----------- Task 7. Show donations functionality --------------------
def show_donations(donations):
    print("\n--- All Donations ---")
    total = 0.0
    if not donations:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
            # donation is a string such as "username donated $100.00"
            try:
                amount = float(donation.split("$")[1])
                total += amount
            except (IndexError, ValueError):
                continue

    print(f"Total = ${total:.2f}")
    return total


