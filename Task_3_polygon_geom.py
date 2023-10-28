import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_7_Working_with_Geometry_Objects\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
output_fc_name = "Polygon"
output_fc_path = os.path.join(gdb_path, output_fc_name)

x_mumbai = 72.7897660288175
y_mumbai = 19.16541516127035

x_pune = 73.85224711622392
y_pune = 18.460479026562194

x_nashik = 73.789950488677
y_nashik = 19.997471004433873

pnt_mumbai_obj = arcpy.Point(x_mumbai, y_mumbai)
pnt_pune_obj = arcpy.Point(x_pune, y_pune)
pnt_nashik_obj = arcpy.Point(x_nashik, y_nashik)
# Spatial Reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")
# Array Object
polygon_array = arcpy.Array()
polygon_array.add(pnt_mumbai_obj)
polygon_array.add(pnt_pune_obj)
polygon_array.add(pnt_nashik_obj)

polygon_geom =arcpy.Polygon(polygon_array, spatial_ref)
arcpy.CopyFeatures_management(polygon_geom, output_fc_path)
print("Process Completed")
