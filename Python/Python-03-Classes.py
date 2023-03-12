#!/usr/bin/python

"""
    🐍    Python Pocket Cards    🐍
    🐍          Classes          🐍

         By Yoann AMAR ASSOULINE

         
""" 

# Python Standard Library Modules 
import os
import platform
import sys
from abc import ABC, abstractmethod

# Cleaning the Terminal
if os.name == 'nt': os.system('cls')
else: os.system('clear')

# # # # # # # # # # # # # # # # # # # 
#                                  #
#   💻 Basic Classes             #
#                                  #
# # # # # # # # # # # # # # # # # # # 

# Basic Fruit Class  
class Fruit: 
    """Simple class used to create any kind of fruit """
 
    # Class Attributes
    category = "Fruit"

    # Class Constructor (always executed when Class is initialized) 
    def __init__(self, name_arg, quantity_arg = 1):  
        """  
            You can test out the code, automatically when the docstring is generated, by using this: 
            >>> test_class = SimpleClass()
        """

        # Instance Attributes
        self.name = name_arg
        self.quantity = quantity_arg
    

    # Instance Method ♦ (Three method types: Instance Method • Class Method • Static Method)
    def increase_quantity(self, added_quantity_arg):
        """ Instance Method to show the Class Instance attribute "name" """
        if type(added_quantity_arg) == int: 
            return self.quantity + added_quantity_arg
        else: 
            return print("please use an integer for the added_quantity_arg")
    
    @classmethod
    def classmethod(cls):
        """ Class Method """
        pass

    @staticmethod 
    def list_of_accepted_fruits():
        """ Static Method """ 
        fruits = ["Apple", "Banana", "Orange", "Pear", 
                  "Kiwi", "Strawberry", "Watermelon"]
        return "Static method called"
    
# Class Objects Instantiation
apple = Fruit("Golden")
strawberry = Fruit("Allstar", 3)
cherry = Fruit("Early Lory")

print_fruit_class_operations = False
if print_fruit_class_operations == True: 

    print(apple.name)
    cherry.show_name()
    print(Fruit.category) 


#################################
# 💻 Abstract & Concrete Classes
#################################

# Abstract (Parent) Class  
class Animal (ABC): 
    """ Abstract (or Parent) Class 
        Can't be instantiated
    """

    def __init__(self):  
        """ By using the NotImplementedError, you can make sure the user will not try to instantiate the abstract class. 
            That's only in case you're not using any abstractmethod. 
        """
        raise NotImplementedError("Cannot implement this") 
 
    def eat (self): 
        print("Animal is eating")


# Concrete (Child) Class
class Dolphin (Animal): 
    """ Concrete (or Child) Class
    """

    def __init__ (self): 
        print ("New Dolphin")

# Objects Instantiation
spinner_dolphin = Dolphin()
# Dinosaur = Animal() # Will raise an error.  
print (issubclass(Dolphin, Animal))
print (isinstance(Dolphin(), Animal))





# Basic Class 03
class Vehicle (ABC): 
    """ Vehicle Class """
    
    # Class Variables 
    Category = "Vehicle"  

    # Class constructor
    def __init__ (self, carName, carSeats, carTransmission): 

        # Properties
        self.vehicle_name = carName 
        self.vehicle_seats = carSeats
        self.vehicle_transmission = carTransmission
     
        # Properties and Access levels 
        self.vehicle_plate = None # Public Level
        self._vehicle_start_button = None # Protected Level (one underscore before the variable name)
        self.__vehicle_keys = None # Private Level (two underscores before the variable name)


    @abstractmethod
    def show_vehicle_info(self): 
        pass 
    
    @abstractmethod
    def car_driving(self): 
        pass

class Car(Vehicle): 
 
    def show_vehicle_info (self): 
        """ Showing some information about the vehicle """ 
        print("Vehicle Name: " + str(self.vehicle_name))
        print("Vehicle Seats: " + str(self.vehicle_seats)) 
        print("Vehicle Transmission: " + str(self.vehicle_transmission))

    def car_driving (self): 
        pass
    

Lamborghini = Car("Lamborghini", 2, "Auto")
Lamborghini.show_vehicle_info() 


