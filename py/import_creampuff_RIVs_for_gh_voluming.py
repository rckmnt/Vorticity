import rhinoscriptsyntax as rs
import os

"""
Rhino Python utility
    Used for importing the closed FBXs of 33-35 to manually combine donuts into one mes
    Import FBXs, name each object as filename of FBX 
"""

# Add FBX folder root path here:
fbxs = "C:\Users\Scott\Desktop\Sim0_FBXs_170716"

def all_Filez_in(dir):
    allFilez = []
    for roots, subds, filez in os.walk(dir):
        for fname in filez:
            f_path = os.path.join(roots, fname)
            allFilez.append(f_path)
            #print('\t- file %s (full path: %s)' % (filename, file_path))
    return allFilez

riv_paths = all_Filez_in(fbxs)

puffs = ['0_33_0_008_cp.fbx', '0_33_0_009_cp.fbx', '0_33_0_025_cp.fbx', '0_33_0_089_cp.fbx', '0_33_1_008_cp.fbx', '0_33_1_009_cp.fbx', '0_33_1_089_cp.fbx', '0_33_2_010_cp.fbx', '0_33_2_011_cp.fbx', '0_33_3_010_cp.fbx', '0_33_3_011_cp.fbx', '0_33_3_044_cp.fbx', '0_33_4_009_cp.fbx', '0_33_4_010_cp.fbx', '0_33_4_016_cp.fbx', '0_33_4_048_cp.fbx', '0_33_4_065_cp.fbx', '0_33_5_010_cp.fbx', '0_33_5_011_cp.fbx', '0_33_5_082_cp.fbx', '0_33_5_089_cp.fbx', '0_34_0_010_cp.fbx', '0_34_0_011_cp.fbx', '0_34_0_041_cp.fbx', '0_34_1_010_cp.fbx', '0_34_1_011_cp.fbx', '0_34_1_041_cp.fbx', '0_34_2_010_cp.fbx', '0_34_2_011_cp.fbx', '0_34_3_010_cp.fbx', '0_34_3_031_cp.fbx', '0_34_4_010_cp.fbx', '0_34_4_011_cp.fbx', '0_34_4_031_cp.fbx', '0_34_4_048_cp.fbx', '0_34_5_010_cp.fbx', '0_34_5_011_cp.fbx', '0_34_5_025_cp.fbx', '0_34_5_039_cp.fbx', '0_35_0_001_cp.fbx', '0_35_0_010_cp.fbx', '0_35_0_026_cp.fbx', '0_35_1_000_cp.fbx', '0_35_1_010_cp.fbx', '0_35_1_049_cp.fbx', '0_35_2_000_cp.fbx', '0_35_2_010_cp.fbx', '0_35_3_010_cp.fbx', '0_35_3_011_cp.fbx', '0_35_3_032_cp.fbx', '0_35_4_010_cp.fbx', '0_35_4_011_cp.fbx', '0_35_4_027_cp.fbx', '0_35_4_062_cp.fbx', '0_35_5_010_cp.fbx', '0_35_5_011_cp.fbx', '0_35_5_022_cp.fbx', '0_35_5_042_cp.fbx']

for p in puffs:
    name = p.split('\.')[0]
#    rs.AddLayer(name)
#    rs.CurrentLayer(name)
    for r in riv_paths:
        if p in r:
            #print name
            print 'YES - - ', p, r
            rs.Command("_Import " + r + " ")
            rs.Command("_SelLast ")
            thing = rs.SelectedObjects()
            rs.ObjectName(thing, name)
            rs.Command("_SelNone ")
