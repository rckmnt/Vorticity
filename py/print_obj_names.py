# print object names

import rhinoscriptsyntax as rs

#select what you want manually
objs = rs.SelectedObjects()

for o in objs:
    print rs.ObjectName(o)
    