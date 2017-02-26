import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import Rhino, datetime

fileName = "0_29_4"  #rs.DocumentName()
filePath = rs.DocumentPath().rstrip(fileName)

# Select all mesh objects
meshes = rs.AllObjects()
print len(meshes)

# Cull tiny meshes
meshes = [m for m in rs.AllObjects() if rs.coercemesh(m).Faces.Count > 100]
print len(meshes)

count = 0

print meshes

rs.EnableRedraw(False)

print datetime.datetime.now()

# For each obj, export as FBX
def export_all(meshes):
    for i, m in enumerate(meshes):
        exportName = "C:\\Users\\Scott\\Desktop\\OUTPUT\\" + fileName + "_" + str(count).zfill(3)
    
        if len(meshes) > 0:
            rs.SelectObject(m)
            command = '-_Export ' + exportName + '.fbx _ExportNurbsObjectsAs=Mesh _ExportFileAs=Version7Binary _EnterEnd'
            rs.Command(command, True)
            rs.UnselectAllObjects()
            print 'exported ', exportName
    
        count += 1
    return


print datetime.datetime.now()

print "...export run DONE."