"""
Get a value from Ghx Python component into Rhino Py Editor
"""

import scriptcontext as sc
import Rhino
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

for i in range(0, 5, 1):
    print i
    gh.SetSliderValue("0be54755-1117-45ab-bf35-4edf64c1b2ae", i)
    gh.RunSolver("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\ghx\\get_Ghx_values")

    #try: 
    num_meshes = sc.sticky["Meshes_To_Export"]
    print 'Exporting %s meshes to FBX...' % (num_meshes) 
    #except:
    #    print 'Nothing', i
        


    # count objects in file for iteration - idk how to get this from Ghx, panel maybe?
    sc.sticky.clear()
    try:
        if sc.sticky.has_key("Meshes_To_Export"):
            num_meshes = sc.sticky["Meshes_To_Export"]
        else:
            num_meshes = sc.sticky["Meshes_To_Export"]
        print 'Exporting %s meshes to FBX...' % (num_meshes) 
    except:
        num_meshes = 120
        print 'no value has been assigned to \"Meshes_To_Export\" key'

