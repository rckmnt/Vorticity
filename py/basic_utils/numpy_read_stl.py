# Read STLs from file
import numpy as np, os
from stl import mesh
'''
Print generic info from STL files
'''

walk_dir = r'C:\Users\Scott\Desktop\test\1_30'

stl_files = []

# Make list of all CSV files, read file, add lines to lines_to_write
for root, subdirs, files in os.walk(walk_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        stl_files.append(file_path)

for s in stl_files:

    print 'File: ', s

    # Using an existing closed stl file:
    your_mesh = mesh.Mesh.from_file(s)

    volume, cog, inertia = your_mesh.get_mass_properties()
    print("Face count                              = {0}".format(len(your_mesh)))
    print("Volume                                  = {0}".format(volume))
    print("Position of the center of gravity (COG) = {0}".format(cog))
    print("Inertia matrix at expressed at the COG  = {0}".format(inertia[0,:]))
    print("                                          {0}".format(inertia[1,:]))
    print("                                          {0}".format(inertia[2,:]))
