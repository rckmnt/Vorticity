import rhinoscriptsyntax as rs
import System
from System.IO import Path

name = rs.DocumentName()
path = rs.DocumentPath()

print name
print path