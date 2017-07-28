
"""
Returns a pseudo-centroid, an average of all mesh Face centroid
"""

avg_pt = []

for m in mesh:

    face_ctrs = []
    totalFac = m.Faces.Count

    x = m.Faces.GetFaceCenter(0).X
    y = m.Faces.GetFaceCenter(0).Y
    z = m.Faces.GetFaceCenter(0).Z

    for i in range(0, m.Faces.Count, 10):       # ONLY AVERAGING EVERY 10
        face_ctrs.append(m.Faces.GetFaceCenter(i))

        center = m.Faces.GetFaceCenter(i)

        x += center.X
        y += center.Y
        z += center.Z

        print x
        #print totalFac * 10
    average = rg.Point3d(x/totalFac * 10, y/totalFac * 10, z/totalFac * 10)

    avg_pt.append(average)

    #averaged = [sum(y) / len(y) for y in zip(*x)]
print "# faces ", m.Faces.Count
