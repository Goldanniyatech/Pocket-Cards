#!/usr/bin/python

"""
    🐍 Python Pocket Card - 3D Game Engine 🐍
          🐼 Panda3D - 01 The Basics 🐼

             By Yoann AMAR ASSOULINE

  🪙 https://docs.panda3d.org/1.10/python/index
"""  

from direct.showbase.ShowBase import ShowBase 
from panda3d.core import WindowProperties


class Panda3D_01_Basics (ShowBase): 
    """ Panda3D 01 The Basics 
        Simple Class to understand how Panda3D can work
    """

    def __init__ (self): 
        ShowBase.__init__ (self)

        self.panda3d_windows_properties()

    def panda3d_windows_properties (self): 
        """ Defining Useful Window Properties 
        """
        
        properties = WindowProperties() 
        properties.setSize (1200, 900)
        self.win.requestProperties(properties)

panda3d_card01_app = Panda3D_01_Basics()
panda3d_card01_app.run()
