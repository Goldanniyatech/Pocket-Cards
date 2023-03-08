#!/usr/bin/python

"""
    🐍 Python Pocket Card 05 Programming Paradigms 🐍

         By Yoann AMAR ASSOULINE
 
         
""" 

import os 
import platform
import random
import sys 

os.system('cls')

# # # # # # # # # # # # # # # # #
#                              #
#  📖 Imperative Paradigm    #
#                              # 
# # # # # # # # # # # # # # # # #

# Imperative Example #1

player_characters = ["Jonesy", "Ramirez", "Haven"]
for character in player_characters: 
    print(character)

i = 0 
while i < len(player_characters): 
    print(str(i) + ": " + player_characters[i])
    i += 1



# Imperative Example #2

player_position = 0 
player_health = 100
player_shield = 150.0 

# Enemies & position (enemy, position)
enemies = [('Zombie', random.randint(5, 95)), ('Vampire', random.randint(20, 80)), ('Werewolf', random.randint(40, 60))]

while True: 

    print(f"Player position: {player_position}")

    # Check if player reached the end 
    if player_position >= 100: 
        print ("You win! \n")
        print (f"Remaining Health: {player_health} ♦ Remaining Shield: {player_shield}")
        break 

    for enemy in enemies: 
        if enemy[1] == player_position: 
            print(f"You are attacked by a {enemy[0]}")
            
            if player_shield > 0: 
                player_shield -= 20
            else: player_health -= 10

    if player_health <= 0: 
        print ("GAME OVER!!")
        break 

    player_position +=1 




# # # # # # # # # # # # # # # # # # # #
#                                    #
#  📖 Object Oriented Paradigm     #
#                                    # 
# # # # # # # # # # # # # # # # # # # #


# Object Oriented Example #1 

class Student: 

    def __init__ (self, student_name_arg, student_class_arg, student_grades_arg): 
        self.student_name = student_name_arg
        self.student_class = student_class_arg
        self.student_grades = student_grades_arg

    def add_grade (self, grade_arg): 
        self.student_grades.append(grade_arg)

    def get_average_grade (self): 
        average_grade = sum(self.student_grades) / len(self.student_grades)
        formatted_average_grade = "{:.1f}".format(average_grade)
        return formatted_average_grade

    def print_summary (self): 
        print(f"Name: {self.student_name}")
        print(f"Class: {self.student_class}")
        print(f"Grade: {self.student_grades}")
        print(f"Average Grade: {self.get_average_grade()}")

student_one = Student("Jonesy", "Computer Science",[random.randint(5, 20), random.randint(10, 16)])
student_two = Student("Haven", "English",[random.randint(5, 20), random.randint(10, 16)])

student_one.add_grade(random.randint(1, 17))

student_one.print_summary()
student_two.print_summary()



