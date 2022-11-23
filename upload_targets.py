# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:56:48 2022

@author: Dimitris
"""

import pandas as pd
import server as server

path = r'C:\Users\Dimitris\.spyder-py3\ARVisualGuideDesktop\csv_data\test\targets.csv'

data = pd.read_csv(path, sep = " ")
