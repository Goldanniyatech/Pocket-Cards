# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#    Python Pocket Card 01 The Basics     #
#                                         #
#         By Yoann AMAR ASSOULINE         #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #
# 🪙 PEP-8 Style Guides https://peps.python.org/pep-0008/ ♦ https://realpython.com/python-pep8/#naming-conventions  



# # # # # # # # # # # # # #
#                         #
#    💻 Commentaries      #
#                         #
# # # # # # # # # # # # # #

# Single-line Comment

# Multi-line Comment
# with the hash (or number sign/ pound sign) 

""" Single line Docstring Comment """

""" Multi-line Docstring Comment
    Note: the autoDocstring VSCode extension can be used 
          to automatically generate docstrings
"""



# # # # # # # # # # # # # # # # # # # # # # # # #
#                                               #
# 💻 Python Standard Library Modules (Built-in) #
#                                               #
# # # # # # # # # # # # # # # # # # # # # # # # #
# 🪙 https://docs.python.org/3/py-modindex.html 


# Classic Module import
import os
import platform
import sys

# Import without specifying the module name when using it (no need to type random._ to access modules' methods)
from random import *

# Import a module and give an Alias 
import random as randomAlias

# Import Custom module only by typing their name
# import MyCustomModule

# Using a method from the imported module "os" to clear the terminal (for Windows only)
os.system('cls')
 
# Using a method from the "platform" module to display the current Operating System
print("Current Platform: " + str(platform.platform()))


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#     💻 Variables & Basic Data Types     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #
# Variables should be named after the snake_case convention (according to PEP-8 style guide)

# Basic Variables: Theory
none_01 = None

boolean_one = True
boolean_two = False
boolean_three = bool(True)

integer_one = 33
integer_two = 30594
integer_three = int(4930)
integer_four = integer_one + integer_two

float_one = 30.3
float_two = 4930.45
float_three = float(458.78)
float_four = float_one * float_two

complex_number_one = 2 + 3j
complex_number_one = complex(3 + 2j)

string_one = "Jonesy"  
string_two = 'Ramirez'
string_three = "Hello, Select your character!"
string_four = str(string_two + ", " + "Game Over!")
string_five = '🦁'
string_six = "453.5"


# Collection of Variables: Theory
dictionary_one = {
        "key one"   : "value one", # one item is comprised of a key and a value
        "key two"   : "value two", 
        "key three" : "value three"
}

list_one = ["item one", "item two", "item three"] # Ordered collection

set_one = {"item one", "item two", "item three"} # Unordered collection without Duplicate items.

tuple_one = ("item one", "item two", "item three") 


# Basic Variables: Real-life Examples
player_health = 100
player_shield = 150.5
player_total_life = player_health + player_shield

player_name = "Jonesy" 
character_select_sentence = "Select your character!"

# Collection of Variables: Real-life Examples 
enemies = ["Alien", "Zombie"]
allies = ("Ramirez", "Amy")
vehicles = {
    "Cars": ["Aston Martin DB5", "Ford Mustang MACH 1"], 
    "Trucks": ("Dodge Ram 2500", "Chevrolet K10 Stepside"), 
    "Bus": "Flying Bus"
}

video_game_settings = {
    "Difficulty": "Hard", 
    "Sound" : True, 
    "Max Health/ Shield/ Extra-Armor": [150, 100, 120], 
    "Controls": {
        "move_up" : "Up_Arrow", 
        "move_down": "Down_Arrow", 
        "move_left": "Left_Arrow", 
        "move_right": "Right_Arrow"
    }, 
    "Auto-Save": "Yes", 
    "Defaut Camera Position" : (10, 40, 150)
}

video_game_weapons = { # Dictionary with multiple values per key, by using a list/ tuple/ set inside
        "Assault Rifles": ["SCAR", "AK-47", "M16"], 
        "Pistols": ("Hand Cannon", "Revolver", "Silenced Pistol")
}


print("Video Game Weapon (Assault Rifles): " + video_game_weapons["Assault Rifles"][1])


# # # # # # # # # # # # # # # # # 
#                               #
#   💻 Basic Data Operations    #
#                               #
# # # # # # # # # # # # # # # # # 

# PEMDAS
math_operation_01 = 12 + (5 * 4^3 - 6)
print ("math_operation_01: " + str(math_operation_01))


# # # # # # # # # # # # # # # # # # # 
#                                   #
#    💻 Basic String Operations    #
#                                   #
# # # # # # # # # # # # # # # # # # # 

print_string_sequence = False 

if (print_string_sequence): 

    # String Escape Sequences 
    print('🔴 Escape Sequence Start')
    print("\\ Backslash")
    print("\n Newline")
    print('Double quote inside a "single quote" string')
    print("\"Double quote inside a double quote string\"") # Same goes for single quote! 
    print('\r Carriage Return \t  Horizontal tab')
    print("🔴 Escape Sequence End")

    # String Methods 
    test_string = "hello"
    print(test_string.capitalize())

    placeholder_string = "Welcome to the fighting arena, {player}"
    print(placeholder_string.format(player="Kazuya"))
    
    # f-string (Formatting String)
    print(f"Hello! {placeholder_string}")

    # r-string (Raw Strings | Used to ignore escape sequences and treat everything as literal characters)
    print(r'Hello\n How are you?')


# # # # # # # # # # # # # # # # # # # 
#                                   #
#    💻 Conditional Statements      # 
#                                   #
# # # # # # # # # # # # # # # # # # # 

boolean_four = False 

if (boolean_four) == False: 
    print ('bool is false')
else: 
    print('bool is true')

integer_five = 34
integer_six = 60 
if (integer_five < integer_six) and boolean_four: 
    print("Higher") 


# # # # # # # # # # # # # # # # # # # 
#                                   #
#             💻 Loops              # 
#                                   #
# # # # # # # # # # # # # # # # # # # 

# For Loops
vehicles = ("car", "bus", "train")
for x in vehicles: 
    print("For Loop x: " + str(x))

for i in range(20): 
    print (i)


# While Loops 
i = 1 
n = 10
while i < n: 
    print ("While Loop i: " + str(i)) 
    i += 1
    if i == 4: 
        continue
    if i == 8: 
        break
else: 
    print("While Loop completed!")

# Nested For & While Loops
players = ["Player 1", "Player 2", "Player 3"]
Enemies = ["Enemy 1", "Enemy 2", "Enemy 3"]

for player in players: 
    print(f"👾 {player} is attacking 👾 \n")

    for enemy in enemies: 
        print(" " + " " + f" {player} attacks {enemy}")
