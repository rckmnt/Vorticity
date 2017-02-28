import rhinoscriptsyntax as rs
import Rhino, time, datetime, os
from os.path import isfile, join
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
import Grasshopper as gh


walk_dir = 'C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT thin STLs'
#print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

stls = []

for root, subdirs, files in os.walk(walk_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        stls.append(file_path)

how_many = len(stls)
print how_many

for s in stls:
    current_file = s.split('\\')[-1][:-9]
    print current_file

"""

TO DO 

Next is Iterate through Dir of STLs 
and Run GHX for each STL.

Def getListofSTLS(dir)
    return STLs

Use same exact def in RhinoPy and GhPy
MAKE SURE filenames align

then run GH solver and export FBXs in nest for loop

"""
rs.EnableRedraw(False)

# Directory to Export Meshes to
#workingDir = rs.BrowseForFolder("C:\\Users\\Scott\\Desktop\\OUTPUT", "Pick a folder to save your files in")
#rs.WorkingFolder(workingDir)

num = 0     # File naming number

start = datetime.datetime.now()
print start

"""
for i in range(0,52,1):
    gh.SetSliderValue("c539ae3f-8a8b-412e-be3d-02c68af32a46",i)
    gh.RunSolver("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\ghx\\Vorticity_joinmesh_6")

    baked = gh.BakeDataInObject("80f6abb1-2b1c-4314-9a05-b18f8f267e49")
    #time.sleep(2)

    # String for filename
    strNum = str(num).zfill(2)
    filename = "0_29_2_" + strNum + ".fbx"

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

"""