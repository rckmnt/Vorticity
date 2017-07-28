import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino.Geometry as rg
import Rhino, time, datetime, os, gc
from os.path import isfile, join
import time

def main():
    rs.EnableRedraw(False)
    
    #walkdir = r"C:\Users\Scott\Dropbox\NBI\Vorticity\OUTPUT\samples_to_test_capping\0_55_0"
    walkdir = r"C:\Users\Scott\Desktop\Sim0_FBXs_170716"

    #CSV can't be used in rhino.python :(
    with open("C:\Users\Scott\Desktop\RIV_data.csv", "wb") as fout:
        fout.write("File, Volume, Centroid, Is Open?, Is Non-Manifold?, Bbox corners, , , , , , , , Face count, Vertex count, \n")

        for roots, subds, files in os.walk(walkdir):
            
            
            for f in files:
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
                cent = rg.VolumeMassProperties.Compute(thing).Centroid
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
                    
                """
                print "     ", "Volume", vol
                print "     ", "Centroid", cent
                print "     ", "BBox..."
                print "     ", "F:", faces
                print "     ", "V:", vertices
                print "     ", "Is Open", isopen
                """
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