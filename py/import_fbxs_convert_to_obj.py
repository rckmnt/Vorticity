import rhinoscriptsyntax as rs
import os
from os.path import basename

"""
Rhino Python utility
    Used for importing the FBXs and saving out as OBJs to same directory
    Import FBXs, save as OBJ
"""

# Add FBX folder root path here:
fbxs = "C:\Users\Scott\Desktop\sim1_openRIV_sampleset"

def all_Filez_in(dir):
    allFilez = []
    for roots, subds, filez in os.walk(dir):
        for fname in filez:
            f_path = os.path.join(roots, fname)
            allFilez.append(f_path)
            #print('\t- file %s (full path: %s)' % (filename, file_path))
    return allFilez

riv_paths = all_Filez_in(fbxs)


for r in riv_paths:

    name = basename(r).split('.')[0]
    outname = os.path.splitext(r)[0] + '.obj'

    rs.Command("_Import " + r + " ")
    rs.Command("_SelLast ")
    thing = rs.SelectedObjects()
    rs.Command("_-Export " + outname + " _Enter _Enter", True)
    rs.Command("_SelNone ")
