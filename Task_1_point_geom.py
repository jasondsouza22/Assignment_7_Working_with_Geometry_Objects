import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_7_Working_with_Geometry_Objects\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
fc_name = "Delhi"
fc_path = os.path.join(gdb_path, fc_name)

x_delhi = 77.21858050401974
y_delhi = 28.639806951102432

# Point Object
pnt_obj = arcpy.Point(x_delhi, y_delhi)

# Spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

# Point Geometry
pnt_geom = arcpy.PointGeometry(pnt_obj, spatial_ref)

arcpy.CopyFeatures_management(pnt_geom, fc_path)

print("Process Completed")