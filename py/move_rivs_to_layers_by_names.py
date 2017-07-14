import rhinoscriptsyntax as rs

# moves mesh objects to layer of their name

for s in rs.SelectedObjects():
    lay = rs.ObjectName(s)[0:6]
    print lay
    rs.ObjectLayer(s, lay)

