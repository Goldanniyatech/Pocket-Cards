#!/usr/bin/python

"""
    🐍    Python Pocket Cards    🐍
    🐍        Functions          🐍

         By Yoann AMAR ASSOULINE

         
""" 


# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                #
# 💻 Python Standard Library Modules (Built-in) #
#                                                #
# # # # # # # # # # # # # # # # # # # # # # # # # #
# 🪙 https://docs.python.org/3/py-modindex.html 
# 🪙 https://www.w3schools.com/python/python_ref_functions.asp
# 🪙 https://www.programiz.com/python-programming/methods/built-in


# Python Standard Library (Importing modules) 
import os
import platform
import sys 
from enum import Enum

# Importing modules without without specifying their names when using them (For instance, no need to type random.randint() to access modules' class methods, only randint())
from random import *

# Importing modules and giving to each of them a specific alias 
import random as randomAlias

# Importing third-party modules (with their corresponding packages installed with PIP)
import customtkinter

# Importing custom/ personal modules found in the exact same directory
# import MyCustomModule




# Using a method from the "os" module to clear the terminal (for Windows only)
os.system('cls' if os.name == 'nt' else 'clear')
 
# Using a method from the "platform" module to display the current Operating System
print("Current Platform: " + platform.platform())
 



print() 

input() 

# Creating a Sequence of Numbers 

# Variables
chest_is_open = True  
player_name = "Jonesy"

player_health = 100 
player_shield = 205.34

 
# # # # # # # # # # # # # # # # # # # # # # #
#                                          #
#     💻 Functions Basics                #
#                                          #
# # # # # # # # # # # # # # # # # # # # # # #



def spawn_enemy(): 
    """ 
    Simple Function to spawn an enemy 

    You can test it out in docstring
    >>> spawn_enemy() 
    """
    
    # Local Variables (can't be accessed outside of the function) 
    enemies_list = ["Goblin", "Orc"] 
    enemy_max_health = 250 
    current_enemies = 20
    current_players = 30 

    # Global Variables
    global MAX_PLAYERS 
    global MAX_ENEMIES
    MAX_PLAYERS = 100
    MAX_ENEMIES = 1500

    if (current_players > current_enemies): 
        old_enemies_count = current_enemies
        current_enemies += randint(10, 50)
        print(f"Enemies count went from {old_enemies_count} to {current_enemies}")

# Function Call
spawn_enemy()


# Function with Three Arguments/ Parameters
def function_with_arguments(arg1, arg2, arg3 = "my optional argument"):
    print( "Function with arguments: " + str(arg1) + " " + str(arg2) + " " + str(arg3))

function_with_arguments("Hello", arg2="test")


def check_variable_type(variable_to_check): 
    """ Function to check any variable type, with one argument (variable_to_check) """ 
    return type(variable_to_check)

# Function Calls
print(check_variable_type(chest_is_open))
print(check_variable_type(player_name))
print(check_variable_type(player_shield))

# Print the docstring
print(check_variable_type.__doc__)


# Example Functions 
def player_identity(): 
    """ Function to display information about the current player"""
    print("Health: " + str(player_health))
