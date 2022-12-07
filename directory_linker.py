# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:08:55 2022

@author: Dimitris
"""

import os
import configparser

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
        return os.path.join(self.wdir, "config.ini")
    
    def get_building_id(self):
        config_path = self.get_config_filepath()
        
        config = configparser.ConfigParser()
        config.read(config_path)
        
        return config["FIREBASE"]["buildingId"]

    
    def set_building_id(self, build_id):
        config_path = self.get_config_filepath()
        
        ## Check if a building id already exists
        config = configparser.ConfigParser()
        config.read(config_path)
        if config.has_option("FIREBASE", "buildingId"):
            raise Exception("Building id is already set. If you wish to set a new id, remove the 'buildingId' line in the 'config.ini' file first.")
        
        ## Write the building id
        config["FIREBASE"] = {}
        config["FIREBASE"]["buildingId"] = build_id
        
        with open(config_path, 'w') as file:
            config.write(file)
            
    def get_vuforia_access_key(self):
        config_path = self.get_config_filepath()
        
        config = configparser.ConfigParser()
        config.read(config_path)
        
        return config["VUFORIA"]["accessKey"]
    
    def get_vuforia_secret_key(self):
        config_path = self.get_config_filepath()
        
        config = configparser.ConfigParser()
        config.read(config_path)
        
        return config["VUFORIA"]["secretKey"]