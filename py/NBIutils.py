import os
from os.path import isfile, join
"""
Utilities for NBI Vorticity Project, mainly filehandling.
"""



# Returns a flat list of all files in the directory
def all_files_in(directory):
    walk_dir = os.path.abspath(directory)
    allFiles = []
    for roots, subds, files in os.walk(directory):
        for filename in files:
            f_path = os.path.join(roots, filename)
            allFiles.append(f_path)
    return allFiles


# Returns a flat list of all empty folders in the directory (foldernames)
def empty_Subdirs(directory):
    emptyTimes = []
    for root, subdirs, files in os.walk(walk_dir):
        for subdir in subdirs:
            folder = os.path.join(root, subdir)
            if len(os.listdir(folder)) < 1:
                #print(subdir)
                emptyTimes.append(subdir)
    return emptyTimes

# Returns a flat list of all folders in the directory (foldernames)
def all_Folds_in(directory):
    allFolders = []
    for root, subdirs, files in os.walk(directory):
        for subdir in subdirs:
            folder = os.path.join(root, subdir)
            allFolders.append(folder)
    return allFolders


