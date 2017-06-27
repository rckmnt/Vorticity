
import rhinoscriptsyntax as rs

ddupes = ['0_51_3_002.fbx', '0_47_0_002.fbx', '0_48_4_003.fbx', '0_51_2_002.fbx', '0_51_5_002.fbx', '0_48_2_002.fbx', '0_49_2_003.fbx', '0_46_2_003.fbx', '0_46_2_000.fbx', '0_51_3_001.fbx']

ids = []
for d in ddupes:

    rs.SelectObject(rs.ObjectsByName(d)[0])

