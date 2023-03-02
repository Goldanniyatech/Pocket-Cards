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


#################################
# 01 💻 Basic Classes
#################################

# Basic Class 01 
class Animal: 
    """ Docstring to document the whole Class """

    # The constructor is always executed when the class is initiated! 
    def __init__(self): 
        """ Docstring to document any function (including the built-in __init__ function) """
        pass # Statement to use as a placeholder. 

# Objects Instantiation
Dolphin = Animal()
Dinosaur = Animal() 


# Basic Class 02 
class Fruit: 
    """ Fruit Class """

    # Class variables shared by all instances  
    category="Fruit"

    def __init__(self, name_arg, quantity_arg = 1): 
        """ """
        # Instance variable unique to each instance 
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
print(Fruit.name)

# Basic Class 03
class Vehicles: 
    """ Vehicle Class """
    
    # Class Variables 
    Category = "Vehicle"  

    # Class constructor
    def __init__ (self, carName, carSeats, carTransmission): 
        self.vehicle_name = carName 
        self.vehicle_seats = carSeats
        self.vehicle_transmission = carTransmission
     
    # Class Methods 
    def ConsoleClear(self): 
        """ Clear the IDE Terminal/ Console on Windows """
        if os.name == 'nt': os.system('cls')
        else: os.system('clear')
     
    def showVehicleInformation(self): 
        """ Showing some information about the vehicle """
        self.ConsoleClear()
        print("Vehicle Name: " + str(self.vehicle_name))
        print("Vehicle Seats: " + str(self.vehicle_seats)) 
        print("Vehicle Transmission: " + str(self.vehicle_transmission))
     
    def carDriving(self): 
        pass


Lamborghini = Vehicles("Lamborghini", 2, "Auto")
#Lamborghini.showVehicleInformation() 


