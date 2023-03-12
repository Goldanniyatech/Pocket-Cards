#!/usr/bin/python

"""
    🐍 Python Pocket Card 08 PSL 🐍

         By Yoann AMAR ASSOULINE
 
         
""" 

# Python Standard Library
import os 
os.system('cls')



import datetime 

date_now = datetime.datetime.now() 
time_now = date_now.time()
test = datetime.datetime.now().time()
date_difference = datetime.date (2023, 3, 3) - datetime.date(2021, 12, 20)

print_datetime_operations = True
if (print_datetime_operations): 
    print(f"Date: {date_now}\t Time: {time_now}")

import os 

current_working_directory = os.getcwd() 
files_current_dir = os.listdir(current_working_directory) 

 

import random

enemy_type = ["Zombie", "Werewolf"]
enemy_health = random.randint(10, 150) # Random integer between the first value (10) and the second value (150)
enemy_power = random.random() # random float between 0 and 1

current_enemy = random.choice(enemy_type)

print_random_operations = False
if (print_random_operations):
    print(f"A new enemy is challenging you: a {current_enemy}")
    print(f"Enemy Health: {enemy_health} ♦ Enemy Power: {enemy_power}")



import sys


import time


