# Go through open Sim 1 RIVS
# Explode and see if they are two meshes
# If not 2 - delete
# If 2, export one as the same files, export other as file_b

import rhinoscriptsyntax as rs

rs.EnableRedraw(False)

meshes = rs.GetObjects(None, rs.filter.mesh)

for m in meshes:
    name = rs.ObjectName(m)

    rs.ExplodeMeshes(m)
    if len(rs.SelectedObjects()) > 1:
        #print rs.SelectedObjects()
        rs.Command("_Undo")
    else:
        rs.DeleteObject(m)

    rs.Command("_SelNone ")
rs.EnableRedraw(True)

