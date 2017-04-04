import rhinoscriptsyntax as rs
import Rhino, time
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
#import Grasshopper as gh


rs.EnableRedraw(False)

# Directory to Export Meshes to
workingDir = rs.BrowseForFolder("Q:\\CITA-Projects\\PROJECTS\\COMPLEX_MODELLING\\04_PROJECTS\\09_stressedSkins2\\02_Rhino\\11_Production\\04_PanelMeshes", "Pick a folder to save your files in")
rs.WorkingFolder(workingDir)

num = 0     # File naming number

for i in range(0,52):
    gh.SetSliderValue("18c77c47-34b0-4be9-82e8-4c40c6877f43",i)
    gh.RunSolver("Q:\\CITA-Projects\\PROJECTS\\COMPLEX_MODELLING\\04_PROJECTS\\09_stressedSkins2\\03_Grasshopper\\05_PanelLayout\\160615b_PanelJig_Layout.gh")
    baked = gh.BakeDataInObject("8d99a531-dffe-4afc-af92-75ee0b4480b8")
    time.sleep(.2)    
    # String for filename
    strNum = str(num).zfill(2)
    RHIfilename = "Panel_" + strNum + ".3dm"
    AIfilename = "Panel_" + strNum + ".ai"
    
    # Rhino commands to do selection and export
    rs.Command("_SelNone", True)
    rs.Command("_SelLast", True)
    rs.Command("_-Export _GeometryOnly=_Yes " + RHIfilename + " _Enter", True)
    #rs.Command("_-Export" + AIfilename + " _Enter", True)
    
    time.sleep(.2)   
    
    rs.Command("_SelNone", True)

    # Increment the filename
    num = num + 1
    
    # Delete the baked objects
    rs.Command("_SelLast", True)
    rs.Command("_Delete", True)
    

    rs.DeleteObjects(baked)    
    time.sleep(.1)
