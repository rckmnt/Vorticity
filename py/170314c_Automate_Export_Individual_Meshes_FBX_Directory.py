import rhinoscriptsyntax as rs
import Rhino, time, datetime, os, gc
import NBIutils as nbi
from os.path import isfile, join
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")


def main():
    rs.EnableRedraw(False)
    
    # Directory to Export Meshes to
    workingDir = rs.BrowseForFolder("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\OUTPUT\\FBXs", "Pick a folder to save your files in")
    rs.WorkingFolder(workingDir)
    
    start = datetime.datetime.now()
    print start
    
    # Walk all STLs in Dir and get names
    thin_STLs = r'C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\Thin_STLs'

    stls = nbi.all_files_in(thin_STLs)

    how_many = len(stls)
    print 'Total STLs to process -', how_many
    
    for j in range(0,3,1):
        gh.SetSliderValue("dddfcfab-73b2-45df-b21c-927f512d0ca9", j)
    
        # File naming number
        num = 0     
    
        filename = stls[j].split('\\')[-1][:-9]
        timeslicename = filename[0:4]
        print 'timeslicename - ', timeslicename, ', file - ', filename
    
        if os.path.exists(workingDir + '\\' + filename):
            rs.WorkingFolder(workingDir + '\\' + filename)
    
        else:
            os.makedirs(workingDir + '\\' + filename)
            rs.WorkingFolder(workingDir + '\\' + filename)
    
        print rs.WorkingFolder()
        
        # Find out how many meshes to export
        
        for i in range(48,60,1):
            gh.SetSliderValue("c539ae3f-8a8b-412e-be3d-02c68af32a46",i)
            gh.RunSolver("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\ghx\\Vorticity_joinmesh_8")
    
            # String for filename
            strNum = str(num).zfill(2)
            exportname = filename + '_' + strNum + ".fbx"
            print 'Exporting:', exportname
    
            baked = gh.BakeDataInObject("80f6abb1-2b1c-4314-9a05-b18f8f267e49")
            if rs.IsObject(baked):
                # Rhino commands to do selection and export
                rs.Command("_SelNone", True)
                rs.Command("_SelLast", True)
                rs.Command("_-Export " + exportname + " _Enter _Enter", True)
            
                rs.Command("_SelNone", True)
            
                # Increment the filename
                num = num + 1
        
                # Delete the baked objects
                rs.Command("_SelLast", True)
                rs.Command("_Delete", True)
            
                rs.DeleteObjects(baked)
            else:
                print 'BREAKKKKKK'
                break
    
    end = datetime.datetime.now()
    runtime = end - start
    
    print start
    print end
    print runtime
    print str(runtime)


if __name__ == '__main__':
    main()