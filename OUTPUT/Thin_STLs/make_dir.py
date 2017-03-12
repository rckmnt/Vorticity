import os


#timeslices = ['0_' + str(x) + '_' + str(y) for x in range(30,100) for y in range(0,6)]
timeslices = ['0_' + str(x) for x in range(43,100)]


print timeslices


def make_Folders(names):
    for n in names:
        if not os.path.exists(n):
            os.makedirs(n)

make_Folders(timeslices)
