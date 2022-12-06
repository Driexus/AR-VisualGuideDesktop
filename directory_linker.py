# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:08:55 2022

@author: Dimitris
"""

import os

class Linker:
    def __init__(self, project_path):
        self.wdir = project_path
    
    def get_project_dir(self):
        return self.wdir
    
    def get_project_name(self):
        return os.path.basename(self.wdir)
    
    def get_or_create_csv_dir(self):
        csv_dir = os.path.join(self.wdir, "csv_data")
        
        if not os.path.exists(csv_dir):
            os.mkdir(csv_dir)
            
        return csv_dir
    
    def get_config_filepath(self):
        return os.path.join(self.wdir, "config.txt")
    
    def get_building_id(self):
        config_path = self.get_config_filepath()
        
        with open(config_path, "r") as file:        
            return file.read()
    
    def set_building_id(self, build_id):
        config_path = self.get_config_filepath()
        
        if os.path.exists(config_path):
            raise Exception("Building id is already set. If you wish to set a new id, delete the config.txt file first.")
        
        with open(config_path, 'w') as file:
            file.write(build_id)