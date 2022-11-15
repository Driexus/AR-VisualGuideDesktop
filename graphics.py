# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:03:17 2022

@author: Dimitris
"""

import server as fb
import tkinter as tk
import math

dx = 0
dy = 0
m1x = 0
m1y = 0

left_x1 = 0
left_y1 = 0
placingLine = False
hasDrawnFirstLine = False
global tempLineId
global distance_text_id
global mouse_coords_text_id

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
        
def right_click(event):
    global m1x
    m1x = event.x
    global m1y
    m1y = event.y
    
def left_click(event):
    global left_x1, left_y1, placingLine
    
    if placingLine:
        canvas.create_line(left_x1, left_y1, event.x, event.y)
        hasDrawnFirstLine = False
        canvas.delete(tempLineId)
        canvas.delete(distance_text_id)
    else:
        left_x1 = event.x
        left_y1 = event.y
        
    placingLine = ~ placingLine
    
def mouse_move(event):
    global tempLineId, hasDrawnFirstLine, distance_text_id, mouse_coords_text_id
    
    if placingLine:
        if hasDrawnFirstLine:
            canvas.delete(tempLineId)
        tempLineId = canvas.create_line(left_x1, left_y1, event.x, event.y)
        hasDrawnFirstLine = True
        
        distance = math.dist([left_x1, left_y1], [event.x, event.y]) / zoomModifier
        canvas.delete(distance_text_id)
        distance_text_id = canvas.create_text(event.x + 5, event.y - 15, text = round(distance, 4), fill = "black")
        
    # Update the mouse coordinates
    canvas.delete(mouse_coords_text_id)
    mouse_coords_text_id = canvas.create_text(40, 20, text = "{} , {}".format(event.x / zoomModifier, event.y / zoomModifier, anchor = tk.N))
    
def escape_click(event):
    global placingLine, hasDrawnFirstLine
    
    if placingLine:
        placingLine = False
        hasDrawnFirstLine = False
        canvas.delete(tempLineId)
        canvas.delete(distance_text_id)


walls = fb.get_walls2()

window = tk.Tk()

window.state("zoomed")
window.title("AR-VisualGuide")


zoomModifier = 20

canvas = tk.Canvas(window)
canvas.pack(fill = tk.BOTH, expand = True)

# TODO calculate the canvas dimensions to center the walls
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)
canvas.bind("<B3-Motion>", move_map)
canvas.bind("<Motion>", mouse_move)
canvas.bind_all("<Escape>", escape_click)

distance_text_id = canvas.create_text(0, 0, text = "")
mouse_coords_text_id = canvas.create_text(0,0, text = "")

for wall in walls:
    x1 = wall["y1"] * zoomModifier + width/2
    x2 = wall["y2"] * zoomModifier + width/2
    y1 = wall["x1"] * zoomModifier + height/2
    y2 = wall["x2"] * zoomModifier + height/2
    
    canvas.create_line(x1, y1, x2, y2)
    
tk.mainloop()

