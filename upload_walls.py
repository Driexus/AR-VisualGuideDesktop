# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:35:14 2022

@author: Dimitris
"""

import pandas as pd
import server

vertices_path = r'C:\Users\Dimitris\.spyder-py3\ARVisualGuideDesktop\csv_data\Museum\vertices.csv'
edges_path = r'C:\Users\Dimitris\.spyder-py3\ARVisualGuideDesktop\csv_data\Museum\edges.csv'

vertices = pd.read_csv(vertices_path, sep = " ", header = None).to_numpy()

edges = pd.read_csv(edges_path, sep = " ", header = None).to_numpy()
walls = []
for edge in edges:
    wall = [vertices[edge[0]], vertices[edge[1]]]
    dic = {"x1" : vertices[edge[0]][0], "y1" : vertices[edge[0]][1], 
           "x2" : vertices[edge[1]][0], "y2" : vertices[edge[1]][1] }
    walls.append(dic)
        
server.set_walls("test building", walls)
