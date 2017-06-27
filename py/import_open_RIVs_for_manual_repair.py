import rhinoscriptsyntax as rs

# Add FBX folder root path here:
fbxs = "C:\Users\Scott\Desktop\closed_fbxs"


rivs = rs.Command("_SelMesh", True)

print rivs
"""
for r in rivs:
    rs.Command('_SelNone', True)
    name = rs.ObjectName(r, name)

    rs.Command('_SelLast', True)
    thing = rs.SelectedObjects()
    name = r.split("\\")
    name = name[-1]
    rs.ObjectName(thing, name)
    rs.Command('_SelNone', True)
"""

