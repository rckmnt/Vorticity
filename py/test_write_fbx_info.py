import rhinoscriptsyntax as rs
import Rhino, time, datetime, os, gc
from os.path import isfile, join


def main():
    rs.EnableRedraw(False)

    walkdir = "C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\samples_to_test_capping"

    # Directory to Export Meshes to
    workingDir = rs.BrowseForFolder(r"C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\samples_to_test_capping", "Pick a folder to save your files in")
    rs.WorkingFolder(workingDir)

    for i, filename in enumerate(walkdir):
        print filename
