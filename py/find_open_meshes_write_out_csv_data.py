import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino.Geometry as rg
import Rhino, time, datetime, os, gc
from os.path import isfile, join
import time

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

def main():
    rs.EnableRedraw(False)
    
    #walkdir = r"C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\samples_to_test_capping\0_55_0"
    walkdir = r"C:\Users\Scott\Desktop\Sim1_FBXs_170905"

    #CSV can't be used in rhino.python :(
    with open("C:\Users\Scott\Desktop\Sim1_dataout_170915_after_1-69.csv", "wb") as fout:
        fout.write("File, Volume, Centroid, Is Open?, Is Non-Manifold?, Bbox corners, , , , , , , , Face count, Vertex count, \n")
        for roots, subds, files in os.walk(walkdir):
            if roots.split('_')[-2][0].startswith('F'):
                pass
            else:
                print int(roots.split('_')[-2][0:1])
                if int(roots.split('_')[-2]) > 68:
        
                    for f in files:
        
        #                if int(f[2:4]) < 30:
        #                    print f
        
                        path = os.path.join(roots, f)
                        
                        command = '-_Import ' + path
                        rs.Command(command, True)
                        rs.Command('_SelLast', True)
                        
                        
                        thing = rs.SelectedObjects()
                        thing = rs.coercemesh(thing[0])
        
                        # Get Data values
                        vol = rg.VolumeMassProperties.Compute(thing).Volume
                        if vol < 0:
                            vol = abs(vol)
                        cent = pseudo_centroid(thing)
                        bbox = rs.BoundingBox(thing)
                        #bboxvol = rg.VolumeMassProperties.Compute(bbox).Volume
                        faces = thing.Faces.Count
                        vertices = thing.Vertices.Count
        
                        if thing.IsClosed:
                            isopen = "-"
                        else:
                            isopen = "Yes"
                        if thing.IsManifold:
                            isnonman = "-"
                        else:
                            isnonman = "Yes"
                            
        
                        print "     ", "Volume", vol
                        print "     ", "Centroid", cent
                        print "     ", "BBox..."
                        print "     ", "F:", faces
                        print "     ", "V:", vertices
                        print "     ", "Is Open", isopen
        
        
                        RIV_data = [f, vol, cent, bbox[0:7], faces, vertices]
        
                        fout.write(f)
                        fout.write(', ')
                        fout.write(str(vol))
                        fout.write(', ')
                        fout.write(str(cent.X) + ";" + str(cent.Y) + ";" + str(cent.Z))
                        fout.write(', ')
                        fout.write(str(isopen))
                        fout.write(', ')
                        fout.write(str(isnonman))
                        fout.write(', ')
                        """
                        fout.write(str(bbox[0].X) + ";" + str(bbox[0].Y) + ";" + str(bbox[0].Z))
                        fout.write(', ')
                        fout.write(str(bbox[1].X) + ";" + str(bbox[1].Y) + ";" + str(bbox[1].Z))
                        fout.write(', ')
                        fout.write(str(bbox[2].X) + ";" + str(bbox[2].Y) + ";" + str(bbox[2].Z))
                        fout.write(', ')
                        fout.write(str(bbox[3].X) + ";" + str(bbox[3].Y) + ";" + str(bbox[3].Z))
                        fout.write(', ')
                        fout.write(str(bbox[4].X) + ";" + str(bbox[4].Y) + ";" + str(bbox[4].Z))
                        fout.write(', ')
                        fout.write(str(bbox[5].X) + ";" + str(bbox[5].Y) + ";" + str(bbox[5].Z))
                        fout.write(', ')
                        fout.write(str(bbox[6].X) + ";" + str(bbox[6].Y) + ";" + str(bbox[6].Z))
                        fout.write(', ')
                        fout.write(str(bbox[7].X) + ";" + str(bbox[7].Y) + ";" + str(bbox[7].Z))
                        fout.write(', ')
                        """
                        fout.write(str(faces))
                        fout.write(', ')
                        fout.write(str(vertices))
                        fout.write('\n')
        
                        rs.Command('_SelLast', True)
                        rs.Command('_Delete', True)
                        
                        
                        # Escape Control
                        if sc.escape_test(False):
                            break


        fout.close()

main()
