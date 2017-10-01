# Import to Rhino open RIVs from list
# If _Explode produces two meshes, write out both as new and delete old

import rhinoscriptsyntax as rs
import os

rs.EnableRedraw(False)

full_RIVs = r'C:\Users\Scott\Desktop\Sim1_FBXs_170814'
list_of_open_RIVs = 'C:\Users\Scott\Desktop\RIV_data_Sim1_170815.csv'

open_RIVs =[]

# Read
with open(list_of_open_RIVs, "r") as RIV_file:
    #read each line from the file
    lines = RIV_file.readlines()
    for line in lines:
        columns = line.split(",")
        if columns[3] == ' Yes':
            open_RIVs.append(columns[0])

for root, subdirs, files in os.walk(full_RIVs):
    for f in files:
        if f.split('.')[-1] == 'fbx':
            if f in open_RIVs:
                fullold = root + "\\" + f
                print fullold
                name = f

                rs.Command("_Import " + fullold + " ")
                rs.Command("_SelLast ")
                thing = rs.SelectedObjects()
                rs.ObjectName(thing, name)
                rs.Command("_SelNone ")