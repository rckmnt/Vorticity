import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import time

objs = rs.GetObjects()

workingDir = rs.BrowseForFolder(r"C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT", "Pick a folder to save your files in")
rs.WorkingFolder(workingDir)


for i, obj in enumerate(objs):

    # String for filename
    strNum = str(i).zfill(3)
    exportname = 'test_open_' + strNum + ".fbx"
    print 'Exporting:', exportname

    # Rhino commands to do selection and export
    rs.Command("_SelNone", True)

    rs.SelectObject(obj)
    #rs.Command("_SelLast", True)
    rs.Command("_-Export " + exportname + " _Enter _Enter", True)
    time.sleep(0.1)
    rs.Command("_SelNone", True)
