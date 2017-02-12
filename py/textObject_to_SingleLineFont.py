import Rhino
import rhinoscriptsyntax as rs

def ConvertTextToGeo():

    #Get Text objects
    obj_list = rs.GetObjects("Select text to convert to geometry", 512, True, True)
    if obj_list is None:
        pass

    #disable redraw
    rs.EnableRedraw(False)

    # Save the current construction plane
    saved_plane = rs.ViewCPlane()

    for obj in obj_list:

        #if Rhino.DocObjects.TextObject.IsValid():
        if rs.IsText(obj):
            rs.LayerName('text single line')
            #font = rs.TextObjectFont(obj)
            #font = rs.TextObjectFont(obj, font = "Machine Tool Gothic")
            font = "MecSoft_Font-1"
            height = rs.TextObjectHeight(obj)
            plane = rs.TextObjectPlane(obj)
            style = rs.TextObjectStyle(obj)
            text = rs.TextObjectText(obj)

            textplane = rs.TextObjectPlane(obj)
            rs.ViewCPlane(view=None, plane=textplane)

            # Add a new text object (geometry)
            cmd = "_-TextObject "
            cmd = cmd + "_GroupOutput=_Yes "
            cmd = cmd + "_FontName=" + font + " "
            #cmd = cmd + "_Italic=" + italic + " "
            #cmd = cmd + "_Bold=" + bold + " "
            cmd = cmd + "_Height=" + str(height) + " "
            cmd = cmd + "_Output=_Curves "
            cmd = cmd + "_AllowOpenCurves=_Yes "
            cmd = cmd + chr(34) + text + chr(34) + " "
            cmd = cmd + "0"
            #Rhino.Commands.Command(cmd, 0)
            rs.Command(cmd, 0)

            # Delete the original object
            rs.DeleteObject(obj)
    # Restore the saved construction plane
    rs.ViewCPlane(view=None, plane=saved_plane)

    # Enable screen redrawing
    rs.EnableRedraw(True)


if __name__ == '__main__':
    ConvertTextToGeo()