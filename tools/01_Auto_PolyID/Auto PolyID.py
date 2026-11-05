import arcpy

fc = arcpy.GetParameterAsText(0)

field_name = "AutoPolyID"

fields = [f.name for f in arcpy.ListFields(fc)]

if field_name not in fields:
    arcpy.AddField_management(fc, field_name, "LONG")

counter = 1

with arcpy.da.UpdateCursor(fc, [field_name]) as cursor:
    for row in cursor:
        row[0] = counter
        cursor.updateRow(row)
        counter += 1

arcpy.AddMessage("AutoPolyID populated successfully.")
