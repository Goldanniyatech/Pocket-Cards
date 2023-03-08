#!/usr/bin/python
# (First line is called a Shebang)

"""
    🐍 Python Pocket Card 01 The Basics 🐍

         By Yoann AMAR ASSOULINE

  🪙 PEP-8 Style Guides https://peps.python.org/pep-0008/
  🪙 https://realpython.com/python-pep8/#naming-conventions  
"""  
 

# # # # # # # # # # # # #  #
#                         #
#    💻 Commentaries     #
#                         #
# # # # # # # # # # # # #  #

# Single-line Comment

# Multi-line Comment
# with the hash (or number sign/ pound sign) 

""" Single line Docstring Comment """

""" Multi-line Docstring Comment
    Note: the autoDocstring VSCode extension can be used 
          to automatically generate docstrings
"""


# Python Standard Library (Importing modules) 
import os
import platform
import sys 
from enum import Enum

os.system('cls' if os.name == 'nt' else 'clear')
 
# # # # # # # # # # # # # # # # # # # # # # #
#                                          #
#     💻 Variables & Data Types          #
#                                          #
# # # # # # # # # # # # # # # # # # # # # # #
# Variables should be named after the snake_case convention (according to PEP-8 style guide)
# Basic Data Types: 

# None (or null) Data Type | The only way to define variables without assigning a proper value
memory_card = None

# Boolean 
game_speed_boot = True # Equivalent to 1 (The Python bool class inherit from the int class)
player_has_key = False # Equivalent to 0
player_has_car = bool(False) # Just to force the data type in python, since it's dynamically typed. 

# Integer  
number_of_players = 1
number_of_enemies = int(45)
total_characters = number_of_players + number_of_enemies
player_weapon_ammo = (200 +100) * 6 

# Floating Point Numbers  
player_health = 150.38
player_shield = 220.5
player_extra_armor = float(300.1)
player_total_life = player_health + player_shield + player_extra_armor
math_operation_01 = 12 + (5 * 4^3 - 6) # Remember about the PEMDAS rule 

# Strings
player_nickname = "Fighter"
player_emblem = '🦁'
playable_character_01 = "Jonesy"
playable_character_02 = 'Ramirez' 
playable_character_03 = 'Haven'  
message_character_select = "Select your character!" 
message_welcome = "Welcome" + " " + "to the battlefield"
message_ending = str(player_nickname + ", " + "Game Over!")

# Complex numbers
complex_number_one = 2 + 3j
complex_number_one = complex(3 + 2j)


# Collection of Variables: Dictionaries
vehicles_dict = {
    "Bus": "Flying Bus", # one dictionary item is comprised of a key (here the Bus category) and a value (here the Flying Bus model)
    "Cars": ["Aston Martin DB5", "Ford Mustang MACH 1"], # Key with multiple values, by using a list/ tuple/ set inside
    "Trucks": ("Dodge Ram 2500", "Chevrolet K10 Stepside")
}
vehicles_dict["Bus"] = "Grounded Bus" # Updating the value of a key 
vehicles_dict["Motorcycles"] = "Harley Davidson" # adding a new key-value pair
del vehicles_dict["Trucks"] # Removing a key-value pair

game_settings_dict = {
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

dictionary_print_results = True 
if (dictionary_print_results): 
    print(vehicles_dict["Bus"]) 
    print(f"⭐ Game Settings \n Difficulty: {game_settings_dict['Difficulty']}")
    print(game_settings_dict["Controls"]["move_right"])
    bus_inside_vehicles_dict = "Bus" in vehicles_dict # Checking if "Bus" key is inside dict
    print(f"Bus inside vehicles_dict? {bus_inside_vehicles_dict}")


# Collection of Variables: Lists
characters_list = ["Jonesy", "Ramirez", "Haven"] # Ordered collection


# Collection of Variables: Sets
enemy_set = {"Zombie", "Werewolf", "Dragon"} # Unordered collection without Duplicate items.
enemy_set.add("Vampire")
enemy_set.remove("Zombie")

# Collection of Variables: Frozensets (unchangeable)
enemy_frozenset = frozenset(enemy_set)

# Collection of Variables: Tuples
weapons_tuple = ("Longsword", "Dagger", "Bow and Arrow") 
allies = ("Amy", "Peely")


# Enum (extra data type. You need to use the Enum Module, from the Python Standard Library)
class Day (Enum): 
    MONDAY = 1 
    TUESDAY = 2
    WEDNESDAY = 3 
    THURSDAY = 4 
    FRIDAY = 5
    SATURDAY = 6 
    SUNDAY = 7



# # # # # # # # # # # # # # # # # # # 
#                                   #
#    💻 Basic String Operations    #
#                                   #
# # # # # # # # # # # # # # # # # # # 

print_string_sequence = False 
if (print_string_sequence): 

    # String Escape Sequences  
    print("🔴 \\ Backslash")
    print("🔴 \n Newline")
    print('🔴 Double quote inside a "single quote" string')
    print("🔴 \"Double quote inside a double quote string\"") # Same goes for single quote! 
    print('🔴 \r Carriage Return') 
    print('🔴 \t Horizontal tabulation')

    # String Methods 
    player_armor_name = "hello"
    print(player_armor_name.capitalize())
    placeholder_string = "Welcome to the fighting arena, {fighter}"
    print(placeholder_string.format(fighter="Kazuya"))
    
    # f-string (Formatting String)
    print(f"Hello! {placeholder_string}")

    # r-string (Raw Strings | Used to ignore escape sequences and treat everything as literal characters)
    print(r'Hello\n How are you?')


# # # # # # # # # # # # # # # # # # # 
#                                   #
#    💻 Conditional Statements      # 
#                                   #
# # # # # # # # # # # # # # # # # # # 

player_has_car = False 
key_is_gold = True
number_of_keys = 4

if (player_has_car == True): 
    print("vrai")
else: 
    print ("faux")

list1 = ["test"]
list1 = ["super"]
list1 = ["hey"]

message_player_keys = int(input("combien de clés ? "))
print(f" DEBUG 'message_player_keys': {message_player_keys}")
if (message_player_keys > 2): 
    print("3 clés au moins")
elif (number_of_keys > 1): 
    print ("2 clés au moins")
elif (number_of_keys > 1): 
    print ("2 clés au moins")
elif (number_of_keys > 1): 
    print ("2 clés au moins")
else: 
    print ("no key")



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
    i += 1


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
enemies = ["Enemy 1", "Enemy 2", "Enemy 3"]

for player in players: 
    print(f"👾 {player} is attacking 👾 \n")

    for enemy in enemies: 
        print(" " + " " + f" {player} attacks {enemy}")
