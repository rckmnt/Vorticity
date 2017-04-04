import rhinoscriptsyntax as rs
import Rhino, time, datetime
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
#import Grasshopper as gh

rs.EnableRedraw(False)

# Directory to Export Meshes to
workingDir = rs.BrowseForFolder("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\export", "Pick a folder to save your files in")
rs.WorkingFolder(workingDir)

num = 0     # File naming number

start = datetime.datetime.now()
print start


for i in range(0,87,1):
    gh.SetSliderValue("c539ae3f-8a8b-412e-be3d-02c68af32a46",i)
    gh.RunSolver("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\export_individ_stls.gh")

    baked = gh.BakeDataInObject("80f6abb1-2b1c-4314-9a05-b18f8f267e49")
    #time.sleep(2)

    # String for filename
    strNum = str(num).zfill(2)
    filename = "0_35_0_" + strNum + ".fbx"

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


end = datetime.datetime.now()
runtime = end - start

print start
print end
print runtime
print str(runtime)