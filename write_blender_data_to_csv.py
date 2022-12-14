import bpy
import os, sys, importlib
import math

# Clear console
os.system('cls')

# Import directory linker and create instance    
filepath = bpy.data.filepath
wdir = os.path.dirname(filepath)
proj_dir = os.path.dirname(wdir)
app_dir = os.path.dirname(proj_dir)

if not app_dir in sys.path:
    sys.path.append(app_dir)

import directory_linker as dl
importlib.reload(dl)

linker = dl.Linker(wdir)

# Get csv directory
outputDir = linker.get_or_create_csv_dir()

objects = bpy.data.objects

walls = objects["Walls"]
targets = objects["Targets"]
items = objects["Items"]

# Write wall vertices
outputPath = os.path.join(outputDir, "vertices.csv")
file = open(outputPath, "w")
for v in walls.data.vertices:
    file.write('{} {}\n'.format(v.co.x, v.co.y))
file.close()

# Write wall edges
outputPath = os.path.join(outputDir, "edges.csv")
file = open(outputPath, "w")
for e in walls.data.edges:
    file.write('{} {}\n'.format(e.vertices[0], e.vertices[1]))
file.close()

# Write target data
outputPath = os.path.join(outputDir, "targets.csv")
file = open(outputPath, "w")
file.write('{} {} {} {} {} {} {}\n'.format("image_target_id", "x", "y", "z", "euler_x", "euler_y", "euler_z"))
rad_inv = 180/math.pi
for target in targets.children:
    location = target.location
    rotation = target.rotation_euler
    file.write('{} {} {} {} {} {} {}\n'.format(target.name, location[0], location[1], location[2], rotation[0]*rad_inv, rotation[1]*rad_inv, rotation[2]*rad_inv))
file.close()

# Write item data
outputPath = os.path.join(outputDir, "items.csv")
file = open(outputPath, "w")
file.write('{} {} {} {}\n'.format("item_id", "x", "y", "z"))
for item in items.children:
    location = item.location
    file.write('{} {} {} {}\n'.format(item.name, location[0], location[1], location[2]))
file.close()