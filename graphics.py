# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:03:17 2022

@author: Dimitris
"""

import server
import tkinter as tk
import math

dx = 0
dy = 0
m1x = 0
m1y = 0

left_x1 = 0
left_y1 = 0
placingLine = False
global tempLineId
global distance_text_id
global mouse_coords_text_id
wall_ids = []

def move_map(event):
    m2x = event.x
    m2y = event.y
    
    global m1x
    global m1y
    
    x = m2x - m1x
    y = m2y - m1y
    
    m1x = m2x
    m1y = m2y
    
    global dx
    dx += x
    global dy
    dy += y
    canvas.move(tk.ALL, x, y)
    update_mouse_coordinates(event)
        
def right_click(event):
    global m1x, m1y
    
    m1x = event.x
    m1y = event.y    
    
def left_click(event):
    global left_x1, left_y1, placingLine
    
    if placingLine:
        canvas.create_line(left_x1, left_y1, event.x, event.y)
        canvas.delete(tempLineId)
        canvas.delete(distance_text_id)
    else:
        left_x1 = event.x
        left_y1 = event.y
        
    placingLine = ~ placingLine
    
def scroll(event):
    global zoomModifier
    
    if event.delta > 0:
        zoomModifier *= 1.2
    elif zoomModifier > 1:
        zoomModifier /= 1.2
        
    update_mouse_coordinates(event)
    remove_walls()
    draw_walls()
    
def mouse_move(event):
    global tempLineId, hasDrawnFirstLine, distance_text_id
    
    if placingLine:
        if hasDrawnFirstLine:
            canvas.delete(tempLineId)
        tempLineId = canvas.create_line(left_x1, left_y1, event.x, event.y)
        hasDrawnFirstLine = True
        
        distance = math.dist([left_x1, left_y1], [event.x, event.y]) / zoomModifier
        canvas.delete(distance_text_id)
        distance_text_id = canvas.create_text(event.x + 5, event.y - 15, text = round(distance, 3), fill = "black")
        
    update_mouse_coordinates(event)
        
def escape_click(event):
    global placingLine, hasDrawnFirstLine
    
    if placingLine:
        placingLine = False
        hasDrawnFirstLine = False
        canvas.delete(tempLineId)
        canvas.delete(distance_text_id)

def remove_walls():
    global wall_ids
    
    for wall_id in wall_ids:
        canvas.delete(wall_id)
        
    wall_ids.clear()

def draw_walls():
    global canvas, wall_ids, dx, dy
    
    for wall in wall_coords:
        x1 = wall["x1"] * zoomModifier + dx
        x2 = wall["x2"] * zoomModifier + dx
        y1 = wall["y1"] * zoomModifier + dy
        y2 = wall["y2"] * zoomModifier + dy
        
        wall_id = canvas.create_line(x1, y1, x2, y2)
        wall_ids.append(wall_id)
        
def update_mouse_coordinates(event):
    global mouse_coords_text_id
    
    canvas.delete(mouse_coords_text_id)
    x = round((event.x - dx)/ zoomModifier, 3)
    y = round((event.y - dy)/ zoomModifier, 3)
    mouse_coords_text_id = canvas.create_text(40, 20, text = "{} , {}".format(x, y))


#wall_coords = server.get_walls("test building")
wall_coords = server.get_walls("home")

window = tk.Tk()

window.state("zoomed")
window.title("AR-VisualGuide")


zoomModifier = 20

canvas = tk.Canvas(window)
canvas.pack(fill = tk.BOTH, expand = True)

# Calculate the canvas dimensions to center the walls
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
dx = width/2
dy = height/2

# Bind buttons
canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)
canvas.bind("<MouseWheel>", scroll)
canvas.bind("<B3-Motion>", move_map)
canvas.bind("<Motion>", mouse_move)
canvas.bind_all("<Escape>", escape_click)

distance_text_id = canvas.create_text(0, 0, text = "")
mouse_coords_text_id = canvas.create_text(0,0, text = "")

draw_walls()

tk.mainloop()