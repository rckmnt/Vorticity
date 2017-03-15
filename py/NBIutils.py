import os
from os.path import isfile, join
"""
Utilities for NBI Vorticity Project, mainly filehandling.
"""

def all_files_in(directory):

    walk_dir = os.path.abspath(directory)

    allFilez = []

    for roots, subds, filez in os.walk(directory):
        for fname in filez:
            f_path = os.path.join(roots, fname)
            allFilez.append(f_path)

    return allFilez
