###########################################
#                                         #
#    Python Pocket Card 02 Functions      #
#                                         #
#         By Yoann AMAR ASSOULINE         #
#                                         #
########################################### 

# Built-in Modules 
import os
import sys

# Variables
chest_is_open = True  
player_name = "Jonesy"

player_health = 100 
player_shield = 205.34

##########################
# 01 💻 Functions Basics #
##########################
 
# Simple Function writing
def simple_function(): 
    """ Function Comment (Docstring) """
    print("This is a simple function")

# Simple Function Call
simple_function()

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
