# pseudo centroids

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg


def pseudo_centroid(mesh):
    
    """
    Returns a pseudo-centroid, an average of all mesh Face centroid
    """

    face_ctrs = []
    totalFac = mesh.Faces.Count

    x = mesh.Faces.GetFaceCenter(0).X
    y = mesh.Faces.GetFaceCenter(0).Y
    z = mesh.Faces.GetFaceCenter(0).Z
    reduction = 1

    for i in range(0, mesh.Faces.Count, reduction):       # ONLY AVERAGING EVERY 10
        face_ctrs.append(mesh.Faces.GetFaceCenter(i))
        center = mesh.Faces.GetFaceCenter(i)
        x += center.X
        y += center.Y
        z += center.Z

    average = rg.Point3d(x/totalFac * reduction, y/totalFac * reduction, z/totalFac * reduction)
    #print "# faces ", mesh.Faces.Count
    
    return average




allms = rs.ObjectsByType(32)

for m in allms:
    #print m
    mesh = rs.coercemesh(m)
    print mesh
    rs.AddPoint(pseudo_centroid(mesh))