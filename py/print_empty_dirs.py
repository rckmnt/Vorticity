import os

walk_dir = r'C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\Sim_0\FBXs'

print('walk_dir = ' + walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

def all_Folds_in(dir):
    allFolders = []
    for root, subdirs, filez in os.walk(dir):
        for subdir in subdirs:
            folder = os.path.join(root, subdir)
            allFolders.append(folder)
    return allFolders

allFolds = all_Folds_in(walk_dir)


def emptySubdirs(dir):
    emptyTimes = []
    for root, subdirs, files in os.walk(walk_dir):
        for subdir in subdirs:
            folder = os.path.join(root, subdir)
            if len(os.listdir(folder)) < 1:
                #print(subdir)
                emptyTimes.append(subdir)
    return emptyTimes

empties = emptySubdirs(walk_dir)

for j, fi in enumerate(allFolds):
    if fi.split("\\")[-1] in empties:
        print j, ',', fi.split("\\")[-1]
