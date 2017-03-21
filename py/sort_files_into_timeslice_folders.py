import os

"""
Walks a dir for STLs and creates folders for each time slice
Moves file into corresponding folder
"""

sort_timeslices = 'C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\Sim_1\Thin_STLs'

'''
def all_Files_in(dir):
    allFiles = []
    for roots, subds, files in os.walk(dir):
        for fname in files:
            f_path = os.path.join(roots, fname)
            allFiles.append(f_path)
            #print('\t- file %s (full path: %s)' % (filename, file_path))
    return allFiles
print all_Files_in(thin_STLs)


for f in all_Files_in(thin_STLs):
    print f
'''

def putInFolders(directory, firstLetter):
    for root, subdirs, files in os.walk(directory):
        #print('--\nroot = ' + root)
        for filename in files:
            if filename[0] == firstLetter:

                # Folder name, paths
                timeslice = filename[:4]
                file_path = os.path.join(root, filename)
                folder_path = os.path.join(root, timeslice)
                new_f_path = os.path.join(folder_path, filename)

                # if folder exists, put it in folder
                if os.path.exists(folder_path):
                    print 'YES', new_f_path
                    print file_path, new_f_path
                    os.rename(file_path, new_f_path)

                # if it doesnt exist, make it and put it
                else:
                    os.makedirs(folder_path)
                    print file_path, new_f_path
                    os.rename(file_path, new_f_path)
                    #print ' have to make', new_f_path


putInFolders(sort_timeslices, '1')
