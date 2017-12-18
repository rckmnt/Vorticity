# Import to Rhino open RIVs from list
# This imports a small subset of disjointed brothers RIVs from a text file of analyzed RIVs


import rhinoscriptsyntax as rs
import os


full_RIVs = r'C:\Users\Scott\Desktop\Sim1_FBXs_170905'
list_of_open_RIVs = 'C:\Users\Scott\Desktop\sim1_disjoint_brothers.txt'

disjoint_RIVs = []
import_samples = []

# Read
with open(list_of_open_RIVs, "r") as RIV_file:
    #read each line from the file
    lines = RIV_file.readlines()
    for line in lines:
        disjoint_RIVs.append(line[:-1])

for d in disjoint_RIVs:
    path = full_RIVs + "\\" + d.split('/')[-1].split('.')[0][0:6] +  "\\" +d
    import_samples.append(path)
    print path



for i in import_samples:
    path = i
    name = path.split('\\')[-1][0:10]

    rs.Command("_Import " + path + " ")
    rs.Command("_SelLast ")
    thing = rs.SelectedObjects()
    rs.ObjectName(thing, name)
    rs.Command("_SelNone ")
