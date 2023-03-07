###########################################
#                                         #
#    Python Pocket Card 01 The Basics     #
#                                         #
#         By Yoann AMAR ASSOULINE         #
#                                         #
###########################################

# PEP-8 Style Guides https://peps.python.org/pep-0008/ ♦ https://realpython.com/python-pep8/#naming-conventions  



#######################
# 00 💻 Commentaries #
#######################

# Single-line Comment

# Multi-line Comment
# with the hash mark. 


""" Single line Docstring Comment """

""" Multi-line Docstring Comment
    Note: the autoDocstring VSCode extension can be used 
          to automatically generate docstrings
"""



####################################################
# 01 💻 Python Standard Library Modules (Built-in) #
####################################################
# https://docs.python.org/3/py-modindex.html 

# Classic import
import os
import platform
import sys

# Import without specifying the module name (no need to type random._ when using modules' methods)
from random import *

# Import a module and give it an alias 
import random as randomAlias

# Using a method from the imported module "os" to clear the terminal (for Windows only)
os.system('cls')
 
# Using a method from the "platform" module to display the current Operating System
print("Current Platform: " + str(platform.platform()))


############################### 
#  02 💻 Basic Data Types    #
###############################

# Simple Variables: Theory
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


# Variables: Real-life Examples
player_health = 100
player_shield = 150.5
player_total_life = player_health + player_shield

player_name = "Jonesy" 
character_select_sentence = "Select your character!"

enemies = ["Alien", "Zombie"]
allies = ("Ramirez", "Amy")

###############################
# 03 💻 Basic Data Operations #
###############################

# PEMDAS
math_operation_01 = 12 + (5 * 4^3 - 6)
print ("math_operation_01: " + str(math_operation_01))


#################################
# 04 💻 Basic String Operations #
#################################

# String Escape Sequences 
print('🔴 Escape Sequence Start')
print("\\ Backslash")
print("\n Newline")
print("\"Double quote inside a double quote string\"") # Same goes for \' single quote strings
print('\r Carriage Return \t  Horizontal tab')
print("🔴 Escape Sequence End")

# String methods 
test_string = "hello"
placeholder_string = "Welcome to the fighting arena, {player}"

print(test_string.capitalize())
print(placeholder_string.format(player="Kazuya"))

################################
# 05 💻 Conditional Statements # 
################################

boolean_four = False 

if (boolean_four) == False: 
    print ('bool is false')
else: 
    print('bool is true')

integer_five = 34
integer_six = 60 
if (integer_five < integer_six): 
    print("Higher") 


################
# 06 💻 Loops #
################

# For Loops
vehicles = ("car", "bus", "train")
for x in vehicles: 
    print("For Loop x: " + str(x))


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

# Nested for & while loops

