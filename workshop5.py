from random import randint

# Task 1: Random Guess
def guess_random_number(tries, start, stop):
    randnum = randint(start, stop)
    while tries > 0:
        print(f"\nNumber of tries left: {tries}")
        try:
            user_guess = int(input(f"Guess a number between {start} and {stop}: "))
            
            # Check if user's guess is within the allowed bounds
            if user_guess < start or user_guess > stop:
                print(f"Out of bounds! Stay between {start} and {stop}.")
                continue

        except ValueError:
            print("Invalid input! Please enter a positive integer number.")
            continue

        if user_guess > randnum:
            print("Guess lower!")
        elif user_guess < randnum:
            print("Guess higher!")
        else: 
            print("You guessed the correct number!")
            return
        
        tries -= 1
    
    print(f"You have failed to guess the number: {randnum}")

# Task 2: Linear Search
def guess_random_num_linear(tries, start, stop):
    rand_num = randint(start, stop)
    print(f"The number for the program to guess is: {rand_num}")


    for target_num in range(start, stop + 1):
        
        current_try = target_num - start + 1

        if current_try > tries:
            print("The program has run out of tries!")
            break

        print(f"Number of tries left: {tries - current_try + 1}")
        print(f"The program is guessing... {target_num}")

        if target_num == rand_num:
            print("The program has guessed the correct number!")
            return
        
    print("The program has failed to guess the correct number.")

#Task 3: Binary Search
def guess_random_num_binary(tries, start, stop):
    rand_num = randint(start, stop)
    print(f"Random number to find: {rand_num}")
    
    lower_bound = start
    upper_bound = stop
    current_try = tries

    list_values = range(start, stop + 1)

    while (lower_bound <= upper_bound) and (current_try >0):
        pivot = (lower_bound + upper_bound) //2
        pivot_value = list_values[pivot]

        if pivot_value == rand_num:
            print(f"Found it! {rand_num}")
            return pivot
        
        if pivot_value > rand_num:
            print("Guessing lower!")
            upper_bound = pivot - 1
        else:
            print("Guessing higher!")
            lower_bound = pivot + 1
        
        current_try -= 1
    
    print("Your program failed to find the number.")
    return -1

#----------------------- Test Driver Code for Task 1 ---------------------
guess_random_number(5, 0, 10)

#----------------------- Test Driver Code for Task 2 ---------------------
#guess_random_num_linear(5, 0, 10)

#----------------------- Test Driver Code for Task 3 ---------------------
#guess_random_num_binary(5, 0, 100)