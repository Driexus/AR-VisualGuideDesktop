# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:08:26 2022

@author: Dimitris
"""

import pandas as pd
import server as server

path = r'C:\Users\Dimitris\.spyder-py3\ARVisualGuideDesktop\csv_data\Museum\tours.csv'

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

server.set_items_characteristics("test building", out)