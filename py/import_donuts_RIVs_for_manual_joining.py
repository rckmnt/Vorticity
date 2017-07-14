import rhinoscriptsyntax as rs
import os

"""
Rhino Python utility
    Used for importing the closed FBXs of 33-35 to manually combine donuts into one mes
    Import FBXs, name each object as filename of FBX 
"""

# Add FBX folder root path here:
fbxs = "C:\Users\Scott\Desktop\pre_donuts"

def all_Filez_in(dir):
    allFilez = []
    for roots, subds, filez in os.walk(dir):
        for fname in filez:
            f_path = os.path.join(roots, fname)
            allFilez.append(f_path)
            #print('\t- file %s (full path: %s)' % (filename, file_path))
    return allFilez

riv_paths = all_Filez_in(fbxs)



folders = ["0_33_0","0_33_1","0_33_2","0_33_3","0_33_4","0_33_5","0_34_0","0_34_1","0_34_2","0_34_3","0_34_4","0_34_5","0_35_0","0_35_1","0_35_2","0_35_3","0_35_4","0_35_5"]

for fold in folders:
    rs.AddLayer(fold)
    rs.CurrentLayer(fold)
    for r in riv_paths:
        name = r.split('\\')[-1]
        #print r
        if fold in name:
            #print name
            rs.Command("_Import " + r + " ")
            rs.Command("_SelLast ")
            thing = rs.SelectedObjects()
            rs.ObjectName(thing, name)
            rs.Command("_SelNone ")
