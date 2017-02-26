import rhinoscriptsyntax as rs
import os

#path = "C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\0"
path = "C:\\Users\\Scott\\Desktop\\1"

def test():
    fol = rs.BrowseForFolder()
    listing  = os.listdir(fol)
    rFiles = []
    for file in listing:
        print os.path.splitext(file)[1]
        if os.path.splitext(file)[1] == ".stl":
            rFiles.append(fol + "/" +file)

    if len(rFiles) == 0:
        return
    for rFile in rFiles:
        rs.Command('_-Import ' + rFile + ' _Enter')

test()
