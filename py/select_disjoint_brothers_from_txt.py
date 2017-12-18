# Import to Rhino open RIVs from list
# If _Explode produces two meshes, write out both as new and delete old

import rhinoscriptsyntax as rs
import os


full_RIVs = r'C:\Users\Scott\Desktop\Sim1_FBXs_170905'
list_of_open_RIVs = 'C:\Users\Scott\Desktop\sim1_disjoint_brothers.txt'

disjoint_RIVs =[]
import_samples = []

# Read
with open(list_of_open_RIVs, "r") as RIV_file:
    #read each line from the file
    lines = RIV_file.readlines()
    for line in lines:
        disjoint_RIVs.append(line[:-1])

for d in disjoint_RIVs[0:50]:
    path = full_RIVs + "\\" + d.split('/')[-1].split('.')[0][0:6] +  "\\" +d
    import_samples.append(path)
    print path

#meshes = rs.GetObjects()

#rs.EnableRedraw(False)
#for m in meshes:
#    if rs.ObjectName(m) not in disjoint_RIVs:
#        rs.DeleteObject(m)


#for root, subdirs, files in os.walk(full_RIVs):
#    for f in files[0:100]:
#        print f
#        if f.split('.')[-1] == 'fbx':
#            if f in open_RIVs:
#                fullold = root + "\\" + f
#                print fullold


for i in import_samples:
            name = i

            rs.Command("_Import " + name + " ")
            rs.Command("_SelLast ")
            thing = rs.SelectedObjects()
            rs.ObjectName(thing, name)
            rs.Command("_SelNone ")
