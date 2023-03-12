#!/usr/bin/python

"""
    🐍    Python Pocket Cards    🐍
    🐍        Files I/O          🐍

         By Yoann AMAR ASSOULINE
 
         
""" 

# Python Standard Library (Text File)
import os 
import platform
import sys 
import string

# Python Standard Library (Binary File)
import pickle


# # # # # # # # # # # # #  #
#                         #
#  📖  Text Files       #
#                         # 
# # # # # # # # # # # # #  #

class TextFile_Basic: 
    """ Simple Class to open or create a text file 
        It does not handle errors (check the  TextFile_Advanced Class)
    """

    def __init__ (self, filename_arg, ): 
        os.system ('cls')

        self.filename = filename_arg
        self.file = None 

    def create_file (self): 
        self.file = open(self.filename, 'r')

    def open_file(self): 
        # open() function has two interesting modes: 'w' to write and 'x' to create
        self.file = open(self.filename, 'x')

    def close_file (self): 
        if self.file is not None: 
            self.file.close()
            self.file = None

text_file_operation = TextFile_Basic("Test.txt")
text_file_operation.open_file() 



class TextFile_Advanced: 
    """ 
        Advanced Text File 
    """

    def __init__ (self): 
        pass

    def open_file (self): 
        pass

    def read_file (self): 
        pass 

    def write_file (self): 
        pass

    def close_file (self): 
        pass


# # # # # # # # # # # # #  #
#                         #
#  📖  Binary Files     #
#                         # 
# # # # # # # # # # # # #  #
