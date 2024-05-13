import arcpy

folder = r'C:\Users\jinycai\OneDrive - University of Iowa\IOWA\GEOG Programming\quiz6\quiz6.gdb'
arcpy.env.workspace = folder
arcpy.env.overwriteOutput = True

# calculate the percetages of polygonA in polygonB and append them to a field in polygonB
def calculatePercentAreaOfPolygonAInPolygonB(input_geodatabase, fcPolygonA, fcPolygonB, idFieldPolygonB):
    try:
      desc_fcA = arcpy.Describe(fcA)
      desc_fcB = arcpy.Describe(fcB)

      if desc_fcA.shapeType != "Polygon":
         print("Error shapeType: ", fcA, "need to be a polygon type!")
         sys.exit(1)

      if desc_fcB.shapeType != "Polygon":
         print("Error shapeType: ", fcB, "need to be a polygon type!")
         sys.exit(1)

      if desc_fcA.spatialReference.name != desc_fcB.spatialReference.name:
         print("Coordinate system error: Spatial reference of", fcA, "and", fcB, "should be the same.")
         sys.exit(1)
    
        intersect_features = "intersect1"
        arcpy.analysis.SpatialJoin(
            target_features=fcPolygonB,
            join_features=fcPolygonA,
            out_feature_class=intersect_features,
            join_operation="JOIN_ONE_TO_ONE",
            join_type="KEEP_ALL",
            field_mapping=r'FIPS "FIPS" true true false 12 Text 0 0,First,#,block_groups,FIPS,0,11;Shape_Area_1 "Shape_Area" false true true 8 Double 0 0,First,#,parks_Intersect,Shape_Area,-1,-1;Shape_Area_Mean "Shape_Area_Mean" true true false 255 Double 0 0,Mean,#,C:\Users\jinycai\OneDrive - University of Iowa\IOWA\GEOG Programming\quiz6\quiz6project.gdb\parks_Intersect,Shape_Area,-1,-1',
            match_option="CONTAINS",
        )
        
        arcpy.management.AddField(intersect_features, idFieldPolygonB, "Float")
                
        with arcpy.da.UpdateCursor(intersect_features, ["Shape_Area_Mean", "Shape_Area", idFieldPolygonB]) as cursor:
            for row in cursor:
                if row[0]:
                    row[2] = 100 * row[0]/row[1]
                else:
                    row[2] = 0
                cursor.updateRow(row)
            
        arcpy.management.JoinField(fcPolygonB, "FIPS", intersect_features, "FIPS", [idFieldPolygonB])

   except Exception:
      e = sys.exc_info()[1]
      print(e.args[0])

calculatePercentAreaOfPolygonAInPolygonB(folder, "parks", "block_groups", "percentage")
