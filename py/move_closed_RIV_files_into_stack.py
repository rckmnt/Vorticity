# Move Closed RIVs back into the Pile
# Move them from their closed folder to the biggie

import os

full_RIVs = 'C:\Users\Scott\Desktop\Sim0_FBXs_170612'
closed_RIVS = 'C:\Users\Scott\Desktop\closed_fbxs'

RIVs = []

for root, subdirs, files in os.walk(closed_RIVS):
    for f in files:
        RIVs.append(root + "\\" + f)

#print len(RIVs)
#print RIVs



for r in RIVs:

    fullold = r
    subd = r.split('\\')[5][0:6]
    r = r.split('\\')[5]
    fullnew = full_RIVs + "\\" + subd + "\\" + r

    print fullold, ' -->> ', '\n \t', fullnew

    ### os.rename(fullold, fullnew)



