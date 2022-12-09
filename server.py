# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyrebase
import configparser

## Read config file
config = configparser.ConfigParser()
config.read("appConfig.ini")
if not ("FIREBASE" in config):
    raise Exception("Bad configuration: Missing application configuration file or missing 'FIREBASE' section in said file.")

fb_section = config["FIREBASE"]

fb_config = {
  "apiKey": fb_section["apiKey"],
  "authDomain": fb_section["authDomain"],
  "databaseURL": fb_section["databaseURL"],
  "storageBucket": fb_section["storageBucket"]
}

## Initialize firebase modules
firebase = pyrebase.initialize_app(fb_config)
auth = firebase.auth()
db = firebase.database()

email = fb_section["username"]
password = fb_section["password"]
user = auth.sign_in_with_email_and_password(email, password)

def get_walls(building_id):
    ref = db.child("buildings").child(building_id).child("walls")
    walls = ref.get(user["idToken"]).val()
    return walls

def get_building_ids():
    build_ids = db.child("buildings").shallow().get(user["idToken"]).val()
    return build_ids

def get_building_names():    
    build_ids = get_building_ids()
    names = {}
    for build_id in build_ids:
        ref = db.child("buildings").child(build_id).child("name")
        name = ref.get(user["idToken"]).val()
        names[build_id] = name
    return names
        
def get_building_data(build_id):
    ref = db.child("buildings").child(build_id)
    return ref.get(user["idToken"]).val()

def set_walls(build_id, walls):
    ref = db.child("buildings").child(build_id).child("walls")
    ref.set(walls, user["idToken"])

def set_name(build_id, name):
    ref = db.child("buildings").child(build_id).child("name")
    ref.set(name, user["idToken"])  
    
def set_items_characteristics(build_id, data):
    ref = db.child("buildings").child(build_id).child("items_characteristics")
    ref.set(data, user["idToken"])
    
def set_items_coords(build_id, data):
    ref = db.child("buildings").child(build_id).child("items_coords")
    ref.set(data, user["idToken"])
    
def set_image_targets_coords(build_id, data):
    ref = db.child("buildings").child(build_id).child("image_targets_coords")
    ref.set(data, user["idToken"])
    
def set_vuforia_keys(build_id, access_key, secret_key):
    access_ref = db.child("buildings").child(build_id).child("vuforia_access_key")
    access_ref.set(access_key, user["idToken"])
    secret_ref = db.child("buildings").child(build_id).child("vuforia_secret_key")
    secret_ref.set(secret_key, user["idToken"])