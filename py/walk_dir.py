import rhinoscriptsyntax as rs
import Rhino, time, datetime, os, copy
from os.path import isfile, join

rs.EnableRedraw(False)


# Walk all STLs in Dir and get names
thin_STLs = 'C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\Thin_STLs'

print os.walk(thin_STLs)

def all_Filez_in(dir):
    allFilez = []
    for roots, subds, filez in os.walk(dir):
        for fname in filez:
            f_path = os.path.join(roots, fname)
            allFilez.append(f_path)
            #print('\t- file %s (full path: %s)' % (filename, file_path))
    return allFilez

print all_Filez_in(thin_STLs)



"0_33_0",
"0_33_1",
"0_33_2",
"0_33_3",
"0_33_4",
"0_33_5",
"0_34_0",
"0_34_1",
"0_34_2",
"0_34_3",
"0_34_4",
"0_34_5",
"0_35_0",
"0_35_1",
"0_35_2",
"0_35_3",
"0_35_4",
"0_35_5",
