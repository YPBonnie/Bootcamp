## Week 1 Bootcamp Assignment
## Bonnie Dou

#--------------------------- Taks 1. Set up the game ----------------
# declare three varibles w first letter capitalized
wizard = 'wizard'.capitalize()
elf  = 'elf'.capitalize()
human = 'hUman'.capitalize()

# decare hp to hold the hit points for each role
wizard_hp = 70
elf_hp = 100
human_hp = 150

# decare damage of each character
wizard_damage = 150
elf_damage = 100
human_damage = 20

# decare hit points and damage for the Dragon
dragon_hp = 300
dragon_damage = 50

""" Please comment out Taksk 2 ~ Task 4 before running Task 5"""

#------------------------ Task 2. Prompt Player -------------------

# show the player a list of options to choose from
print(f"1) {wizard}")
print(f"2) {elf}")
print(f"3) {human}")

# choose your character from 1 to 3:
#character = input("Choose your character:")

#------------------------- Taks 3. Player Choice --------------------
while True:
    character = input("Choose your character (1 for Wizard, 2 for Elf, 3 for Human)")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        character= elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        character = "Unknown character. Please choose 1, 2, or 3."

print(f"You have chosen the character: {character}")
print(f"Health: {my_hp}")
print(f"Damage: {my_damage}")

#--------------------- Task 4: Battle with the Dragon! ---------------------------

while dragon_hp >0:
    # Player attacks the Dragon
    dragon_hp = dragon_hp - my_damage
    print(f"The {character} damaged the Dragon!")
    print(f"The Dragon's hitpoints are now: {dragon_hp}\n")

    # Check if Dragon is defeated
    if dragon_hp <= 0:
        print(f"The Dragon has lost the battle.\n")
        break

    # Dragon attacks the Player
    my_hp = my_hp - dragon_damage
    print(f"The Dragon strikes back at {character}")
    print(f"The {character}'s hitpoints are now: {my_hp}\n")

    # Check if Player is defeated
    if my_hp <= 0:
        print(f"The Dragon has lost the battle.\n")
        break


"""
#------------------ Task 5:  Optional Challenges ------------------------
# Please comment out Task 2,3, and 4 before running the following codes
# Add Dwarf and Exit as possible choice of Player
dwarf = "Dwarf".capitalize()
dwarf_hp = 10
dwarf_damage = 15

# show the player a list of options to choose from
print(f"1) {wizard}")
print(f"2) {elf}")
print(f"3) {human}")
print(f"4) {dwarf}")
print(f"5) Exit")

user_intention = True
while user_intention:
    character = input("Choose your character (Only input one of the following in any case: Wizard, Elf, Human, Dwarf, or Exit)")
    character = character.capitalize()
    if character == "Wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "Elf":
        character= elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "Human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "Dwarf":
        character = dwarf
        my_hp = dwarf_hp
        my_damage = dwarf_damage
        break
    elif character == "Exit":
        player_again_choice = input("Do you want to play again? Choose 1 for Yes, and 0 for No.")
        if player_again_choice == '0':
            user_intention = False
            break
        else:
            continue
    else:
        character = "Unknown character. Please choose one from Wizard, Elf, Human, Dward for Exit."


if character in ["Wizard", "Elf", "Human", "Dwarf"]:
    print(f"You have chosen the character: {character}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}")
else:
    print("Exiting game. Goodby!\n")

"""