import rhinoscriptsyntax as rs

# Add FBX folder root path here:
fbxs = "C:\Users\Scott\Desktop\creampuffs"
rs.WorkingFolder(fbxs)

# Remember to Unlock what meshes you want to export
rivs = rs.ObjectsByType(32)

for r in rivs:
    name = rs.ObjectName(r)
    #name = name.split('.')[0] + "_cp." + name.split('.')[1]
    print name
    rs.SelectObject(r)
    rs.Command("_-Export " + name + " _Enter _Enter", True)
    rs.Command("_SelNone", True)

