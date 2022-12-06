# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyrebase
import asyncio

## Initialize firebase modules

apiKey = "AIzaSyCsJYZrPmICYlOqEbGgsD0tAswaCJhTnMg"
authDomain = "ar-visualguide.firebaseapp.com"
databaseURL = "https://ar-visualguide-default-rtdb.europe-west1.firebasedatabase.app/"
storageBucket = "ar-visualguide.appspot.com"

config = {
  "apiKey": apiKey,
  "authDomain": authDomain,
  "databaseURL": databaseURL,
  "storageBucket": storageBucket
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

#authTask = asyncio.create_task(
#    sign_in_with_email_and_password_async("toliasj@yahoo.gr", "password"))


async def sign_in_with_email_and_password_async(email, password):
    user = auth.sign_in_with_email_and_password(email, password)
    return user

def get_walls(building_id):
    ref = db.child("buildings").child(building_id).child("walls")
    walls = ref.get().val()
    return walls

def get_building_ids():
    build_ids = db.child("buildings").shallow().get().val()
    return build_ids

def get_building_names():    
    build_ids = get_building_ids()
    names = {}
    for build_id in build_ids:
        ref = db.child("buildings").child(build_id).child("name")
        name = ref.get().val()
        names[build_id] = name
    return names
        
def get_building_data(build_id):
    ref = db.child("buildings").child(build_id)
    return ref.get().val()

def set_walls(build_id, walls):
    ref = db.child("buildings").child(build_id).child("walls")
    ref.set(walls)

def set_name(build_id, name):
    ref = db.child("buildings").child(build_id).child("name")
    ref.set(name)  
    
def set_items_characteristics(build_id, data):
    ref = db.child("buildings").child(build_id).child("items_characteristics")
    ref.set(data)
    
def set_items_coords(build_id, data):
    ref = db.child("buildings").child(build_id).child("items_coords")
    ref.set(data)
    
def set_image_targets_coords(build_id, data):
    ref = db.child("buildings").child(build_id).child("image_targets_coords")
    ref.set(data)