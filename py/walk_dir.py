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
