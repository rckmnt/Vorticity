import rhinoscriptsyntax as rs
import Rhino, time, datetime, os, gc
import NBIutils as nbi
from os.path import isfile, join
gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")


def main():
    rs.EnableRedraw(True)
    
    # Directory to Export Meshes to
    workingDir = rs.BrowseForFolder("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\OUTPUT\\FBXs", "Pick a folder to save your files in")
    rs.WorkingFolder(workingDir)
    
    start = datetime.datetime.now()
    print start
    
    # Walk all STLs in Dir and get names
    thin_STLs = r'C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\Sim_1\Thin_STLs'

    stls = nbi.all_files_in(thin_STLs)

    how_many = len(stls)
    print 'Total STLs to process -', how_many
    
    for k in range(6):
        
        foldername = stls[k].split('\\')[-1][:-9]
        print foldername
        
        if os.path.exists(workingDir + '\\' + foldername):
            rs.WorkingFolder(workingDir + '\\' + foldername)
        else:
            os.makedirs(workingDir + '\\' + foldername)
            rs.WorkingFolder(workingDir + '\\' + foldername)
        print rs.WorkingFolder()
        
        for j in range(k,420,6):
            print j
            gh.SetSliderValue("dddfcfab-73b2-45df-b21c-927f512d0ca9", j)
            gh.RunSolver("C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\ghx\\170403_Sim1_Vorticity_joinmesh9")    
            
            filename = stls[j].split('\\')[-1][:-9]
            
            rs.Command("-ViewCaptureToFile " + filename + ".jpg W=3840 H=2160 S=1 _EnterEnd")

    end = datetime.datetime.now()
    runtime = end - start
    
    print start
    print end
    print runtime
    print str(runtime)


if __name__ == '__main__':
    main()