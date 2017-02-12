import rhinoscriptsyntax as rs
import os

#path = "C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\0"
path = r"C:\Users\Scott\Desktop\1"

def get_Files():
    fol = path #rs.BrowseForFolder()
    listing  = os.listdir(fol)
    rFiles = []
    for file in listing:
        #print os.path.splitext(file)[0]
        if os.path.splitext(file)[1] == ".stl":
            rFiles.append(fol + "\\" + file)

    if len(rFiles) == 0:
        return
    for rFile in rFiles:
        #rs.Command('_-Import ' + rFile + ' _Enter')
        print rFile
    return rFiles

files = get_Files()

for i in files:
    print i