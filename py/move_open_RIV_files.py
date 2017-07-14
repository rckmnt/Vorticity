# Move Open RIVs out of the Pile
# Read which ones are open from a .txt file
# Move them to a 'graveyard' folder to delete manually


import os

full_RIVs = 'C:\Users\Scott\Desktop\Sim0_FBXs_170612'
RIV_graveyard = 'C:\Users\Scott\Desktop\open_RIVs'

list_of_open_RIVs = 'C:\Users\Scott\Dropbox\NBI\Vorticity\documentation\open_RIVs.txt'

RIVs =[]

# Read
with open(list_of_open_RIVs, "r") as RIV_file:
    #read each line from the file
    contents = RIV_file.readlines()
    for c in contents:
        c =c[:-1]
        RIVs.append(c)

print len(RIVs)


for root, subdirs, files in os.walk(full_RIVs):
    for f in files:
        if f.split('.')[-1] == 'fbx':
            if f in RIVs:
                fullold = root + "\\" + f
                fullnew = RIV_graveyard + "\\" + f
                print fullold, ' -->> ', fullnew

                os.rename(fullold, fullnew)



