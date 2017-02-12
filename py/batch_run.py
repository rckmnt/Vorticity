import rhinoscriptsyntax as rs
import os

#path = "C:\\Users\\Scott\\Dropbox\\NBI\\Vorticity\\0"
path = rs.BrowseForFolder(r"C:\Users\Scott\Desktop\TEST")

def all_files(path):
    listing  = os.listdir(path)
    rFiles = []
    for file in listing:
        # os.path.splitext(file)[1]
        if os.path.splitext(file)[1] == ".stl":
            rFiles.append([path, file])  
    return rFiles

def export_all(meshes, folder, filename):
    count = 0
    for i, m in enumerate(meshes):
        exportName = folder + '\\' + filename + "_" + str(count).zfill(3)
    
        if len(meshes) > 0:
            rs.SelectObject(m)
            command = '-_Export ' + exportName + '.fbx _ExportNurbsObjectsAs=Mesh _ExportFileAs=Version7Binary _EnterEnd'
            rs.Command(command, True)
            rs.UnselectAllObjects()
            print 'exported ', exportName

        count += 1
    return

files = all_files(path)

print files

for j, f in enumerate(files):

    print 'starting ', j
    rs.Command('_-Import ' + f[0] + '\\' + f[1] + ' _Enter')
    
    meshys = rs.AllObjects()
    
    # TODO make clear the path and filenaming
    # Export all things
    export_all(meshys, f[0], f[1].split('.')[0])
    
    # delete all things
    allObjs = rs.AllObjects()
    rs.DeleteObjects(allObjs)


