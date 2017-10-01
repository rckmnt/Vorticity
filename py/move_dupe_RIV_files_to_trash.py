# Move Sim1 Dupe RIVs out of the Pile
# Read which ones are open from a .txt file
# Move them to a 'graveyard' folder to delete manually


import os

full_RIVs = 'C:\Users\Scott\Desktop\Sim1_FBXs_170814'
RIV_graveyard = 'C:\Users\Scott\Desktop\dupes_to_delete'

list_of_duped_RIVs = 'C:\Users\Scott\Desktop\dupes.txt'

RIVs =[]

# Read
with open(list_of_duped_RIVs, "r") as RIV_file:
    #read each line from the file
    contents = RIV_file.readlines()
    for c in contents:
        if len(c) > 11:
            RIVs.append(c)

print len(RIVs)

RIVs = [r[:-1] for r in RIVs]

for root, subdirs, files in os.walk(full_RIVs):
    for f in files:
        if f.split('.')[-1] == 'fbx':
            if f in RIVs:
                fullold = root + "\\" + f
                fullnew = RIV_graveyard + "\\" + f
                print fullold, ' -->> ', fullnew

                #os.rename(fullold, fullnew)
