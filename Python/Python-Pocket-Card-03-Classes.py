###########################################
#                                         #
#    Python Pocket Card 03 Classes        #
#                                         #
#         By Yoann AMAR ASSOULINE         #
#                                         #
###########################################  

# Built-in Modules 
import os
import platform
import sys
from abc import ABC, abstractmethod

# Cleaning the Terminal
if os.name == 'nt': os.system('cls')
else: os.system('clear')

#################################
# 01 💻 Basic Classes
#################################

class SimpleClass: 
    """ Docstring to document the whole Class """

    # Class Attributes
    class_attribute_01 = 0 
    class_attribute_02 = ""

    # Class Constructor, always executed when the Class is initialized.
    def __init__ (self, instance_arg): 
        """ Docstring to document any function (including the built-in __init__ function) """
        # Instance Attributes
        self.instance_attribute_01 = instance_arg

    def simple_method (self): 
        pass # Statement used as a placeholder



# Basic Class 02 
class Fruit: 
    """ Fruit Class """
 
    category="Fruit"

    def __init__(self, name_arg, quantity_arg = 1):  
        self.name = name_arg
        self.quantity = quantity_arg
    
    def show_name(self):
        return print(self.name) 

apple = Fruit("Golden")
strawberry = Fruit("Allstar", 3)
cherry = Fruit("Early Lory")
apple.show_name() 
cherry.show_name()
print(Fruit.category) 


#################################
# 02 💻 Abstract & Concrete Classes
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


