import rhinoscriptsyntax as rs
import os

"""
Rhino Python utility
    Used for importing the FBXs into Rhino with Object Name from filename
"""

# Add FBX folder root path here:
#fbxs = "C:\Users\Scott\Desktop\sim1_openRIV_sampleset\FBXs"
fbxs = r"C:\Users\Scott\Desktop\Sim1_FBXs_171216\1_35_5"
# also used 0_31_0

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
    name = r.split('\\')[-1]
    print name
    rs.Command("_Import " + r + " ")
    rs.Command("_SelLast ")
    thing = rs.SelectedObjects()
    rs.ObjectName(thing, name)
    rs.Command("_SelNone ")