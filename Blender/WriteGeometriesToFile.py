import bpy
from os import system

# Clear console
cls = lambda: system('cls')
cls()

# Print geometries
obdata = bpy.context.active_object.data

# Write to file
outputPath = r'C:\Users\Dimitris\.spyder-py3\ARVisualGuideDesktop\Blender\Museum\vertices.csv'
file = open(outputPath, "w")

for v in obdata.vertices:
    file.write('{} {}\n'.format(v.co.x, v.co.y))

file.close()
outputPath = r'C:\Users\Dimitris\.spyder-py3\ARVisualGuideDesktop\Blender\Museum\edges.csv'
file = open(outputPath, "w")

for e in obdata.edges:
    file.write('{} {}\n'.format(e.vertices[0], e.vertices[1]))

file.close()