# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:44:49 2022

@author: Dimitris
"""

import bpy
import os

filepath = bpy.data.filepath
directory = os.path.dirname(filepath)
print(directory)