#!/usr/bin/python

"""
    🐍 Python Pocket Card - 3D Digital Content Creation Software 🐍
                 🍊 Blender - 01 The Basics 🍊

                     By Yoann AMAR ASSOULINE

  🪙 https://docs.panda3d.org/1.10/python/index
"""  

# Dictionary to provide information about the Addon
bl_info = {
        "name" : "Script Name", 
        "description" : "Addon Description", 
        "author" : "Addon Author", 
        "version" : (1, 0), 
        "blender" : (3, 0, 0),  
}

# Python Standard Library Modules 
import sys

# Blender Modules
try: 
    import bpy   
except ImportError: 
    print('⚠️ You must run this Python script from the Blender Software')
    sys.exit()


class Blender_Operator_Simple (bpy.types.Operator): 
    """ 
        Blender Operator Class (Simple Version)    
    """
    def __init__ (self): 
        print("Blender Python Script Loading")



# # # # # # # # # # # # # # # # # # # #
#                                    #
#  📖 Registration                 #
#                                    # 
# # # # # # # # # # # # # # # # # # # #

# Module Registration 
def register(): 
    bpy.utils.register_class(Blender_Operator_Simple)

def unregister(): 
    bpy.utils.unregister_class(Blender_Operator_Simple)

if __name__ == "__main__": 
    register()
