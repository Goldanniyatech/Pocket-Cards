###########################################
#                                         #
#    Python Pocket Card 01 The Basics     #
#                                         #
#         By Yoann AMAR ASSOULINE         #
#                                         #
###########################################

# Reference
# PEP-8 Style Guides https://peps.python.org/pep-0008/ 
#                    https://realpython.com/python-pep8/#naming-conventions  



#######################
# 00 💻 Commentaries #
#######################

# Single-line Commentaries 

# Multi-line commetaries
# with the hash mark. 


""" Single line Docstring Comment """

""" Multi-line Docstring Comment
    Note: the autoDocstring VSCode extension can be used 
          to automatically generate docstrings
"""

##########################
# 01 💻 Built-in Modules #
##########################

import os
import platform
import sys

# Clearing the Terminal by using the os imported module
os.system('cls')

# Displaying the current Operating System by using the platform module
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
list_one = ["item one", "item two", "item three"]

tuple_one = ("item one", "item two", "item three")

set_one = {"item one", "item two", "item three"}

dictionary_one = {
        "key one"   : "value one", # one item is comprised of a key and a value
        "key two"   : "value two", 
        "key three" : "value three"
}


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

# For Looop 

vehicles = ("car", "bus", "train")

for x in vehicles: 
    print("For Loop x: " + str(x))

# While Loop 

i = 1 
n = 10

while i < n: 
    print ("While Loop i: " + str(i))
    i += 1
