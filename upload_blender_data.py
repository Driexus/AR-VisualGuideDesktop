# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:56:48 2022

@author: Dimitris
"""

import pandas as pd
import os
import server

# The directory from which we fetch the csv data
working_dir = r'C:\Users\Dimitris\.spyder-py3\ARVisualGuideDesktop\csv_data\Museum'
# The id of the building on which we will write the blender data
building_id = "test building"

def read_targets_coords():
    path = os.path.join(working_dir, "targets.csv")
    return pd.read_csv(path, sep = " ").to_dict("records")

def read_items_coords():
    path = os.path.join(working_dir, "items.csv")
    return pd.read_csv(path, sep = " ").to_dict("records")

def read_walls():
    vertices_path = os.path.join(working_dir, "vertices.csv")
    edges_path = os.path.join(working_dir, "edges.csv")
    
    vertices = pd.read_csv(vertices_path, sep = " ", header = None).to_numpy()    
    edges = pd.read_csv(edges_path, sep = " ", header = None).to_numpy()
    walls = []
    for edge in edges:
        dic = {"x1" : vertices[edge[0]][0], "y1" : vertices[edge[0]][1], 
               "x2" : vertices[edge[1]][0], "y2" : vertices[edge[1]][1] }
        walls.append(dic)
        
    return walls
    
items = read_items_coords()
targets = read_targets_coords()
walls = read_walls()

server.set_items_coords(building_id, items)
server.set_image_targets_coords(building_id, targets)        
server.set_walls(building_id, walls)