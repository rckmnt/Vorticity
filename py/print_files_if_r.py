# rename_files

import os

walk_dir = "C:\Users\Scott\Desktop\Sim0_FBXs_170716_shortname"

for roots, subds, filez in os.walk(walk_dir):
    for filename in filez:

        if '_cp' in filename:
            print filename

"""
        if filename.split('.')[0][-3:] == '_cp':
            oldname = filename
            newname = filename[0:10] + '.fbx'
            f_path = os.path.join(roots, filename)

            oldpath = os.path.join(roots, oldname)
            newpath = os.path.join(roots, newname)
            print oldpath,'\t', newpath

            #os.rename(oldpath, newpath)
"""



