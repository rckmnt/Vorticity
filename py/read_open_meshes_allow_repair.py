import rhinoscriptsyntax as rs

#prompt the user for a file to import
filter = "Text file (*.txt)|*.txt|All Files (*.*)|*.*||"
filename = rs.OpenFileName("Open Point File", filter)
if not filename: pass

# Add FBX folder root path here:
fbxs = "C:\Users\Scott\Desktop\Sim0_FBXs_170612"

riv_paths = []

#read each line from the file
file = open(filename, "r")
contents = file.readlines()
for c in contents:
    path = fbxs + "\\" +  c[:6] + "\\" + c[:-1]
    riv_paths.append(path)
file.close()

#print [r for r in riv_paths]

print len(riv_paths)
riv_paths = riv_paths[500:1592]


for r in riv_paths:
    
    command = '-_Import ' + r
    rs.Command(command, True)
    rs.Command('_SelLast', True)
    thing = rs.SelectedObjects()
    name = r.split("\\")
    name = name[-1]
    rs.ObjectName(thing, name)
    rs.Command('_SelNone', True)


