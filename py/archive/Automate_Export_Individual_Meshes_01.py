import rhinoscriptsyntax as rs
import Rhino, time
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
#import Grasshopper as gh


rs.EnableRedraw(False)

# Directory to Export Meshes to
workingDir = rs.BrowseForFolder("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\export", "Pick a folder to save your files in")
rs.WorkingFolder(workingDir)

num = 0     # File naming number

for i in range(0,5,1):
    gh.SetSliderValue("e25b571c-3f5e-4afa-857a-de49a58b74d7",i)
    gh.RunSolver("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\export_individ_stls.gh")

    baked = gh.BakeDataInObject("d0868c3b-02e3-4ba9-b056-183ab5d0f737")
    #time.sleep(2)

    # String for filename
    strNum = str(num).zfill(2)
    filename = "Chip_" + strNum + ".stl"

    # Rhino commands to do selection and export
    rs.Command("_SelNone", True)
    rs.Command("_SelLast", True)
    rs.Command("_-Export " + filename + " _Enter _Enter", True)

    rs.Command("_SelNone", True)

    # Increment the filename
    num = num + 1

    # Delete the baked objects
    rs.Command("_SelLast", True)
    rs.Command("_Delete", True)

    rs.DeleteObjects(baked)



