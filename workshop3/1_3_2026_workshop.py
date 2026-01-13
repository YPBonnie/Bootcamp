class enemy:
    def __init__(self, hp, name, special_ability = "none"):
        self.hp = hp
        self.name = name
        self.sepecial_ability = special_ability

    def __str__(self): #access its own variables
        return f"""Our emeny is the {self.name} 
{self.name} has {self.hp} hp 
{self.name} has a special ability of {self.sepecial_ability}
        """ # reurn multiple lines can use """ ....\n ...\n ... """
    


koopa = enemy(2, "koope", "shell")
print(koopa)

#check python tutor: can visualize your codes
#replit.com: it can make everything 


class character:
    def __init__(self, character_class, attack_dmg:int, special_ability, weapon, hp=100, money:int=100):
        self.character_class = character_class
        self.attack_dmg = attack_dmg # can i use int(attach_dmg)? 
        self.special_ability = special_ability
        self.weapon = weapon
        self.hp = hp
        self.money = money
        self.mana = 50

    def __str__(self): #non multi line version
        return f"""This character is a {self.character_class}
It has {self.name}
        """

wizard = character("wizard", 150, "Lightning", "staff", 120, 200)
#wizard.replenish_mana(100)

class paladin(character): #class inheritant
    def __init__(self, character_class, attach_dmg, special_ability, weapon, hp, religion, money=200): #change the default money from character class. 
        super().__init__(character_class, attach_dmg, special_ability, weapon, hp, money)
        self.armor = "steel"
        self.faith = religion #show self.X does not need to match the varialbe name.         

    def heal_other(self, other_character:character): # if you specify :character here, you will have a class of attributes after other_character
        print(f"{self.character_class} is healing {other_character.character_class}")
        self.hp -= 20
        other_character.hp += 50

pal_aidan = paladin("paladin", 50, "heal", "axe", 300, "saradomin") #they will have $200 by default

pal_aidan.heal_other(wizard)

print(pal_aidan.hp)
print(wizard.hp)


print("Pass" if num==5 else "Fail")

num = 5
if num==5:
    print("Pass")
else:
    print("Fail")


#Portfolio is due this week
# some libraries to look inot: 
#pandas, numpy, pygame, pysimplegui -> today's workshop. Turn the bank class to turn into an App.



Bonnie
bonnie_36143
Online
Join the channel: https://www.nucamp.co/discord/add/onpa-pyfun-sat02 Leave the channel: https://www.nucamp.co/discord/remove/onpa-pyfun-sat02

Victor Manuel Cuevas — 12/5/25, 11:47 AM
and a assignment during class tomorrow
Trevor B — 12/5/25, 1:46 PM
i promise you it’ll be more chill than you think
Trevor B — 12/6/25, 9:14 AM
Attachment file type: acrobat
workshop_week_5.pdf
1.03 MB
Trevor B — 12/6/25, 9:52 AM
https://tinyurl.com/4fsaexds
Trevor B — 12/6/25, 11:43 AM
https://projecteuler.net/about
About - Project Euler
A website dedicated to the fascinating world of mathematics and programming
# counter = 0
# for i in range(100):
#     for j in range(100):
#         for k in range(100):
#             for l in range(100):
#                 print(i,j,k,l)
Expand
12_6_2025_workshop.py
2 KB
Attachment file type: acrobat
The Big Book of Small Projects.pdf
20.28 MB
Attachment file type: acrobat
Python for Data Analysis Data Wrangling with Pandas, NumPy, and IPython by Wes McKinney.pdf
12.72 MB
Attachment file type: acrobat
Python Cookbook Recipes for Mastering Python 3, 3rd Edition by David Beazley, Brian K. Jones.pdf
10.00 MB
Trevor B — 12/6/25, 11:50 AM
Attachment file type: acrobat
Game Programming Algorithms and Techniques A Platform-Agnostic Approach (Sanjay Madhav).pdf
10.01 MB
Attachment file type: acrobat
Make Art with Python Programming for Creative People by Kirk Kaiser.pdf
7.95 MB
Dylan Wilson — 12/12/25, 6:25 PM
Hello everyone! @Trevor B are you going to be our primary instructor?
Trevor B — 12/12/25, 6:57 PM
hey! yes i will be your instructor. 

i am looking forward to meeting you all tomorrow! 

i will make your python learning experience excellent
Trevor B — 12/13/25, 9:15 AM
Attachment file type: acrobat
week_1_python.pdf
379.09 KB
Trevor B — 12/13/25, 9:59 AM
here
Trevor B — 12/13/25, 11:14 AM
# n -= 1 is a short hand way of saying n = n - 1

# if you break out of a nested while loop, you only break out of that current one, you will still be in the outer one.
# n = 10
# while n > - 10:
#     print(n)
Expand
12_13_2025_workshop.py
2 KB
LaMar Frank Triplett

 — 12/13/25, 3:24 PM
@Trevor B Having  a little trouble with the second while loop. I'm so close, yet so far.
#Ballet with dragon code would go here. 
while True:
    dragon_hp = dragon_hp - my_damage
    my_hp = my_hp - dragon_damage
    print("The", character, "damaged the dragon!", my_damage)
    print("The dragon has", dragon_hp, "hitpoints left.",  my_hp)
    if dragon_hp <= 0:
        print("The dragon has lost Battle!")
        break
    if my_hp <= 0:
        print("The", character, "has lost Battle!")
        break
    else:
        print("Unknown character ")
        print("You have left the loop.")
Trevor B — 12/13/25, 3:27 PM
check the dragons hp immediately after you reduce it from the players damage to see if its alive still, then you can subtract from the player and see if theyre alive

so you have the code just rearrange the order
Philip N

 — 12/16/25, 10:34 AM
The fib recursion function in the study material is one example for why programming is hard, especially for questions on DSA at interviews.  Below is the code for solving the fib problem iteratively, you can see even without recursion, it is not a peace of cake for most newbies.  I am looking forward to Trevor’s lecture on algorithmic thinking, specifically how to break down complex problems into clear, executable steps and translate that logic into precise code. Understanding this formulation process will be invaluable
iFib(n):
    # 1. Handle the base cases (n=0, n=1, n=2)
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # 2. Initialize the first two values
    a = 0
    b = 1

    # 3. Iterate from the 2nd number up to the nth number
    # We start at the 2nd number (i=2) because we already know the 0th and 1st
    for i in range(2, n + 1):
        current_fib = a + b

        # Update the sequence for the next iteration,  the old F(n-1) becomes the new F(n-2)
        a = b 
        # The new F(n) becomes the new F(n-1)
        b = current_fib 

    # The loop stops when 'b' holds the result for the nth number
    return b
Jose Escobar — 12/16/25, 8:36 PM
Hey @Trevor B  can I update my code?
from teh weekly assignment?
Trevor B — 12/16/25, 8:37 PM
yeah you can, i couldn’t grade today so i will be tomorrow morning
Jose Escobar — 12/16/25, 8:40 PM
okay Ill add the new file
thnx
Jose Escobar — 12/16/25, 8:48 PM
I tried to update it, but couldnt find an option to, I got some errors but didnt want to miss the deadline and so I submitted it.
But I went over with a friend and found the errors and got it fixed now.
Trevor B — 12/16/25, 9:53 PM
don’t worry about the submission and points, all i care about is that you learn and feel confident in what you know
Trevor B — 12/20/25, 9:08 AM
Attachment file type: acrobat
week_2_python.pdf
794.77 KB
Elias Escoto Lara — 12/20/25, 10:10 AM
https://pythontutor.com/visualize.html#mode=edit
Trevor B — 12/20/25, 11:04 AM
# more about the range function

# words = ["hey", "hi", "hello"]
# # words = [0, 1, 2]

# for i in words:
Expand
12_20_2025_workshop.py
5 KB
Bryuan Mathis — 12/22/25, 3:57 PM
Hey @Trevor B was just curious on your take on Leetcode? Do you think its a good resource for us to begin using now or is it not necessary for increasing skill?
Trevor B — 12/22/25, 4:06 PM
don’t use it right now. i would say after week 5 you can though
Bryuan Mathis — 12/22/25, 4:23 PM
cool thanks lol I was worried that I wasn't practicing enough
Trevor B — 12/24/25, 11:22 PM
Grades are in! Sorry for the delay. If anyone is running late from the holidays just let me know please
LaMar Frank Triplett

 — 12/24/25, 11:40 PM
Aloha Trevor, I’m running a little late. I’ve just submitted wk 2 assignment but I’m still working the extra credit stuff. Really sorry. I hate to have you working on Christmas. 
Trevor B — 12/24/25, 11:41 PM
no worries, i’ll grade it on saturday during the workshop with no penalty. have a nice Christmas if you celebrate!
LaMar Frank Triplett

 — 12/24/25, 11:44 PM
:thank_you: :shaka_sign: really appreciate! Have a very merry Christmas!
Trevor B — 12/27/25, 9:09 AM
Attachment file type: acrobat
week_3_python.pdf
246.77 KB
Trevor B — 12/27/25, 10:34 AM
# Slicing
# list_name[starting point (inclusive, by default is 0, optional): end point (exclusive end point, by default will go to the end, optional): steps (optional)]
# ^^^^ this is similar to the range function in terms of how the values work
# colons (:) are required even if you don't enter a value, this is because otherwise you'd just be accessing an individual index instead of slicing

Expand
12_27_2025_workshop.py
4 KB
LaMar Frank Triplett

 — 12/27/25, 10:57 AM
while True:
    print("\n          === Automated Teller Machine ===          ")
    name = input("Enter name for register: ")
    pin = input("Enter PIN: ")
    balance = 0
    print(f"{name} has been registered with a starting balance of ${balance}") #Pass arugment using f-string.


    if len(name) <= 1 and len(name) <= 10: #bonus tasks- Finally remembered that 'len(name)' objects should on both sides of 'AND"
        print("Registration Successful!")
        break

    elif len(pin) ==  4: #bonus tasks- Not completely sure if I'm using the 'len(pin)' function right.
        print("Registration Successful!")
        break

    else:
        print("\n  Invalid name is entered. Please enter registration name with less than 10 characters..")
Bryuan Mathis — 12/27/25, 11:35 AM
from donations_pkg.homepage import show_homepage
from donations_pkg.user import login

database = {
    "username":"admin",
    "password":"password123"
}

donations = []
authorized_user = ""





if authorized_user == "":
    print("You must be loggged in to donate")
else: 
    print(f"Logged in as: {authorized_user}")

choice = input("Choose an option to continue:")

if choice == "1":
    username = input("Enter Username:")
    password = input("Enter a password:")
    authorized_user = login(database,username,password)
elif choice == "2": 
    print('TODO:Write Register Functionality')
elif choice == "3":
    print("TODO: Write Donate Functionality")
elif choice == "4": 
    print("TODO: Write Show Donations Functionality")
elif choice == "5":
    print("Goodbye")
else: 
    print('Invalid option!')
def login(database:dict, username:str, password:str):
    if username in database and password in database == database[username]:
        print(f"Welcome {username}!")
    elif password != database[username]:
        print("Wrong password")
    elif username != database[username]:
        print("Wrong username")
    else: 
        print("Information not found")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\bryua\Documents\NucampFolder\Python\1-Fundamentals\Week 3\Workshop_3\donations_pkg\user.py", line 6, in login
    elif password != database[username]:
                     ~~~~^^^^^^^^^^
KeyError: 'admin'


def login(database:dict, username:str, password:str):
    if username and password in database == database[username]:
        print(f"Welcome {username}!")
    elif password != database[username]:
Expand
user.py
1 KB

def show_homepage():
    print("------------------------------------------------")
    print("|  1.      Login      |  2.   Register          |")
    print("------------------------------------------------")
    print("|  3.      Donate      |  2.  Show Donations    |")
Expand
homepage.py
1 KB
from donations_pkg.homepage import show_homepage
from donations_pkg.user import login

database = {
    "username":"admin",
    "password":"password123"
Expand
app.py
1 KB
Trevor B — 12/27/25, 11:51 AM
https://youtu.be/5vgpZWkyyjs DO NOT VIEW THIS UNTIL AFTER YOU TRY THE ICE CREAM SHOP CHALLENGE
YouTube
Trev-Rock
Coding Challenge Review: Ice Cream Shop
Image
Philip N

 — 12/30/25, 3:41 PM
How are you doing ? I am on material linked_list2.py class Node, do you agree with my study node on this one?
    def init(self, value):
        self.value = value
        self.next = None # None is type neutral for empty, this is not that "" for empty string

head = Node("1st Node")
head.next = Node("2nd Node")

def iter_linked_list(node):
    while node is not None: # evaluate the entire node, the address of variable "node", not the node.value
        print(node.value)
        node = node.next
 
iter_linked_list(head)
Trevor B — 9:10 AM
Attachment file type: acrobat
week_4_notes.pdf
291.51 KB
Trevor B — 10:24 AM
https://pythontutor.com/render.html#mode=display
class character:
    def __init__(self, character_class, attack_dmg:int, special_ability, weapon, hp=100, money:int=100):
        self.character_class = character_class
        self.attack_dmg = int(attack_dmg)
        self.special_ability = special_ability
        self.weapon = weapon
Expand
1_3_2026_workshop.py
4 KB
class person_in_line:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
Expand
conga_line.py
1 KB
libraries to look into, pandas, numpy, pygame, pysimplegui
for the portfolio project ^^^
﻿
class character:
    def __init__(self, character_class, attack_dmg:int, special_ability, weapon, hp=100, money:int=100):
        self.character_class = character_class
        self.attack_dmg = int(attack_dmg)
        self.special_ability = special_ability
        self.weapon = weapon
        self.hp = hp
        self.money = money
        self.mana = 50
    
    def __str__(self): # use triple quotation marks for multi-line string
        return f"""This character is a {self.character_class}
It has {self.attack_dmg} damage
It has {self.hp} hp
It has {self.mana} mana
The {self.character_class} is known for wielding their trusty {self.weapon} and fighting enemies with their powerful {self.special_ability}
They have {self.money} monies."""

    def replenish_mana(self, amt:int):
        self.mana += amt

class paladin(character):
    def __init__(self, character_class, attack_dmg, special_ability, weapon, hp, religion, money=200):
        super().__init__(character_class, attack_dmg, special_ability, weapon,hp,money)
        self.character_class = "paladin" # here, we changed it so that regardless of what the user puts for the character class attribute, that it will switch to paladin 
        self.armor = "steel"
        self.faith = religion # this is to show you that self.X does not need to match the variable name, although it is useful to make them match for readability purposes
    
    def __str__(self): # non multi line version
        return f"This character is a paladin\nIt has {self.attack_dmg} damage\nIt has {self.hp} hp\nIt has {self.mana} mana\nThe {self.character_class} is known for wielding their trusty {self.weapon} and fighting enemies with their powerful {self.special_ability}. They have {self.money} monies. They wield shiny {self.armor} armor. They are aligned with their {self.faith} faith"

    def replenish_mana(self, amt): # THIS IS POLYMORPHISM
        self.mana += amt
        self.hp *= 2
    
    def heal_other(self, other_character:character):
        print(f"{self.character_class} is healing {other_character.character_class}")
        self.hp -= 25
        other_character.hp += 50

# Here is an example of taking an input from a user to then use as a parameter for a class
# damage = input("how much damage do you deal? ")
# wizard = character("wizard", damage, "lightning", "staff",120,200)
# in the __init__ method of the class, we are typecasting this to an integer. You can also typecast it before using it as a parameter for the object

wizard = character("wizard", 150, "lightning", "staff",120,200)

wizard.replenish_mana(100)

print(wizard)

pal_aidan = paladin("sdfghjklsfdghjkl", 50,"heal","axe",300,"saradomin")

pal_aidan.replenish_mana(35)
print(pal_aidan)

pal_aidan.heal_other(wizard)

print(wizard)



# num = 19
# print("Pass" if num == 5 else "Fail")


# --------------------------------------------------------
# mario class example
class enemy:
    def __init__(self, hp, name):
        self.name = name
        self.hp = hp

class koopa(enemy):
    def __init__(self, hp, name, shell_color, flight:bool):
        super().__init__(hp, name)
        self.shell_color = shell_color
        self.flight = flight


class drybones(koopa):
    def __init__(self, hp, name, shell_color, flight):
        super().__init__(hp, name, shell_color, flight)
    
    def return_to_life(self):
        print("dry bones respawns")

class goomba(enemy):
    def __init__(self, hp, name, flight, spike):
        super().__init__(hp,name)
        self.flight = flight
        self.spike = spike


#Trevor's notes: 1_3_2026_workshop.py

