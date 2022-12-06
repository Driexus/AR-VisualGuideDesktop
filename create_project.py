# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:44:49 2022

@author: Dimitris
"""

import os, sys, bpy, importlib
import random, string

# Import directory linker and create instance    
filepath = bpy.data.filepath
wdir = os.path.dirname(filepath)
proj_dir = os.path.dirname(wdir)
app_dir = os.path.dirname(proj_dir)

if not app_dir in sys.path:
    sys.path.append(app_dir)

import directory_linker as dl
importlib.reload(dl)

linker = dl.Linker(wdir)

# Create a random id https://stackoverflow.com/questions/2511222/efficiently-generate-a-16-character-alphanumeric-string
build_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(42))

linker.get_or_create_csv_dir()
linker.set_building_id(build_id)