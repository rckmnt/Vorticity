import rhinoscriptsyntax as rs
import Rhino, time, datetime, os, gc
import NBIutils as nbi
from os.path import isfile, join
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

"""
        SIM 0   0   0   0   0   0   0   0
"""


def main():
    rs.EnableRedraw(True)
    
    # Directory to Export Meshes to
    #workingDir = rs.BrowseForFolder(r"C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\Sim_0\FBXs", "Pick a folder to save your files in")
    #rs.WorkingFolder(workingDir)
    
    start = datetime.datetime.now()
    print start
    
    # Walk all STLs in Dir and get names
    thin_STLs = r'C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\Sim_0\Thin_STLs'
    stls = nbi.all_files_in(thin_STLs)

    how_many = len(stls)
    print 'Total STLs to process -', how_many
    
    for j in range(0, how_many, 1):
    
        gh.SetSliderValue("dddfcfab-73b2-45df-b21c-927f512d0ca9", j)

        filename = stls[j].split('\\')[-1][:-9]
        timeslicename = filename[0:4]

        gh.RunSolver("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\ghx\\170705_Sim0_Export_Screencaps.gh")

        # String for filename
        exportname = "C:\\Users\\Scott\\Desktop\\flat\\" + filename + ".png"
        exportname_persp = "C:\\Users\\Scott\\Desktop\\persp\\" + filename + ".png"

        X = "E_Right_X"
        Y = "E_Front_Y"
        Z = "E_Top_Z"
        persp = "animation_2"

        baked = gh.BakeDataInObject("80f6abb1-2b1c-4314-9a05-b18f8f267e49")
        if baked:

            rs.Command("_SelNone", False)

            # Switch view depending on Section
            if filename[-1] == '0' or filename[-1] == '1':
                rs.Command("-NamedView r " + X + " _EnterEnd", True)
            elif filename[-1] == '2' or filename[-1] == '3':
                rs.Command("-NamedView r " + Y + " _EnterEnd", True)
            elif filename[-1] == '4' or filename[-1] == '5':
                rs.Command("-NamedView r " + Z + " _EnterEnd", True)
            rs.Command("-ViewCaptureToFile " + exportname + " _Enter W=3840 H=2160 S=1 _EnterEnd", True)
            
            rs.Command("-NamedView r " + persp + " _EnterEnd", True)
            rs.Command("-ViewCaptureToFile " + exportname_persp + " W=3840 H=2160 S=1 _EnterEnd", True)

            # Delete the baked objects
            rs.Command("_SelLast", True)
            rs.Command("_Delete", True)
        
            rs.DeleteObjects(baked)
        else:
            print 'BREAK'
            break

    end = datetime.datetime.now()
    runtime = end - start
    
    print 'Start -', start
    print 'End -', end
    print runtime
    print str(runtime)


if __name__ == '__main__':
    main()