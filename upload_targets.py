# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:56:48 2022

@author: Dimitris
"""

import pandas as pd
import os
import server

working_dir = r'C:\Users\Dimitris\.spyder-py3\ARVisualGuideDesktop\csv_data\test\\'

def read_targets():
    path = os.path.join(working_dir, "targets.csv")
    return pd.read_csv(path, sep = " ")

def read_items():
    path = os.path.join(working_dir, "items.csv")
    return pd.read_csv(path, sep = " ")
    
items = read_items().to_dict("records")
targets = read_targets().to_dict("records")

server.set_items_coords("test building", items)
server.set_targets_coords("test building", targets)