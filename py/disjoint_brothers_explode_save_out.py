
import rhinoscriptsyntax as rs
import os

# Select a disjoint brother RIV
# explode it
# IF it makes 2 meshs
#   Export 1 as name
#   Export 2 as name + 'a'    
# IF it makes 1:
#   delete it    

rs.EnableRedraw(False)

rs.Command("_SelMesh")
meshes = []

#for s in rs.SelectedObjects():
#    meshes.append(s)


for m in meshes[0:50]:
    rs.ExplodeMeshes(m, True)
    rs.Command("_SelLast")
    if len(rs.SelectedObjects()) > 1:
        print len(rs.SelectedObjects())
        obj_1 = rs.SelectedObjects()[0]
        obj_2 = rs.SelectedObjects()[1]
        name_one = str(rs.ObjectName(obj_1))
        name_two = str(rs.ObjectName(obj_2)) + '_b'
        print name_one, name_two
         
    else:
        pass
        #print ' - no change - '


#for m in meshes[50:]:
#    rs.HideObject(m)
