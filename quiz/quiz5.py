import arcpy

folder = r'C:\Users\jinycai\OneDrive - University of Iowa\IOWA\GEOG Programming\quiz5'

arcpy.env.workspace = folder
arcpy.env.overwriteOutput = True
airport_features = folder + '\\airports.shp'
airport_features_projected = folder + '\\airports_AEAC.shp'

# project the layer with equal distance projected coordinate system to get unit in meter
# wkt generated from https://projectionwizard.org/
wkt = """PROJCS["ProjWiz_Custom_Equidistant_Conic",
 GEOGCS["GCS_WGS_1984",
  DATUM["D_WGS_1984",
   SPHEROID["WGS_1984",6378137.0,298.257223563]],
  PRIMEM["Greenwich",0.0],
  UNIT["Degree",0.0174532925199433]],
 PROJECTION["Equidistant_Conic"],
 PARAMETER["False_Easting",0.0],
 PARAMETER["False_Northing",0.0],
 PARAMETER["Central_Meridian",-155.9179688],
 PARAMETER["Standard_Parallel_1",54.4413937],
 PARAMETER["Standard_Parallel_2",68.3732619],
 PARAMETER["Latitude_Of_Origin",61.4073278],    
 UNIT["Meter",1.0]]"""

coordinate_system = arcpy.SpatialReference(text=wkt)
arcpy.management.Project(airport_features, airport_features_projected, coordinate_system)

# add a field to store the buffer distances based on different criteria 

arcpy.management.AddField(airport_features_projected, "distance", "SHORT")
    
with arcpy.da.UpdateCursor(airport_features_projected, ["FEATURE", "TOT_ENP", "distance"]) as cursor:
    for row in cursor:
        row[2] = 0
        if row[0] == "Airport":
            if row[1] > 10000:
                row[2] = 15000
            elif row[1] <= 10000:
                row[2] = 10000
        elif row[0] == "Seaplane Base":
            if row[1] > 1000:
                row[2] = 7500
        cursor.updateRow(row)

# generate buffer layer with distance field values
airport_feature_buffer = folder + "\\airport_buffer.shp"
arcpy.analysis.Buffer(airport_features_projected, airport_feature_buffer, "distance")
