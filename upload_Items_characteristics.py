# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:08:26 2022

@author: Dimitris
"""

import os, sys
import pandas as pd
import server as server
import directory_linker as dl

if len(sys.argv) != 2:
    raise Exception("Expected 1 argument and got {}".format(len(sys.argv) - 1))

wdir = sys.argv[1]
linker = dl.Linker(wdir)

# The directory from which we fetch the csv data
csv_dir = linker.get_or_create_csv_dir()

# The id of the building on which we will write the blender data
building_id = linker.get_building_id()

path = os.path.join(csv_dir, "tours.csv")

# Drop the index collumn
data = pd.read_csv(path, sep = ",", usecols= [i for i in range(1,5)]).to_dict("records")

# Keep the ids in seperate dictionary
ids = pd.read_csv(path, sep =",", usecols=[0]).to_dict("records")

# Combine them into a new dictionary in the form of "id : data"
out = {}
for entry, value in zip(ids, data):
    # Remove some unneeded data
    value["section"] = value["section"].replace("Μόνιμη Έκθεση: ", "").replace('"', '')

    key = entry["id"]
    out[key] = value

server.set_items_characteristics(building_id, out)