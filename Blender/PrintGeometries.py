import bpy
from os import system

# Clear console
cls = lambda: system('cls')
cls()

# Print geometries
obdata = bpy.context.object.data

print('Vertices:')
for v in obdata.vertices:
    print('{}. {} {} {}'.format(v.index, v.co.x, v.co.y, v.co.z))

print('Edges:')
for e in obdata.edges:
    print('{}. {} {}'.format(e.index, e.vertices[0], e.vertices[1]))

print('Faces:')
for f in obdata.polygons:
    print('{}. '.format(f.index), end='')
    for v in f.vertices:
        print('{} '.format(v), end='')
    print() # for newline