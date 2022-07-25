import arcpy
import pandas as pd
from datetime import datetime

def arcgis_table_to_df(in_fc, input_fields=None, query=""):
    
    """Function will convert an arcgis table into a pandas dataframe with an object ID index, and the selected
    input fields using an arcpy.da.SearchCursor.
    :param - in_fc - input feature class or table to convert
    :param - input_fields - fields to input to a da search cursor for retrieval
    :param - query - sql query to grab appropriate values
    :returns - pandas.DataFrame"""
    
    OIDFieldName = arcpy.Describe(in_fc).OIDFieldName
    if input_fields:
        final_fields = [OIDFieldName] + input_fields
    else:
        final_fields = [field.name for field in arcpy.ListFields(in_fc)]
    data = [row for row in arcpy.da.SearchCursor(in_fc,final_fields,where_clause=query)]
    fc_dataframe = pd.DataFrame(data,columns=final_fields)
    fc_dataframe = fc_dataframe.set_index(OIDFieldName,drop=True)
    return fc_dataframe

#Get date
now = datetime.now()
dt_string = now.strftime("%Y%m%d")

# Set environment settings
workspace = arcpy.env.workspace = "D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb"
outWorkspace = "D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb"

# Set the local variables
in_table = f"D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data/CA_Los Angeles/Crimes/Filtered_{dt_string}.csv"
out_feature_class = f"LA_Crimes"
x_coords = "LON"
y_coords = "LAT"
z_coords = ""

# Make the XY event layer...
arcpy.management.XYTableToPoint(in_table, out_feature_class,
                                x_coords, y_coords, z_coords, 
                                arcpy.SpatialReference(4326, 115700))


LACity_Walking_Streets = "D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb/LACity_Walking_Streets"
LA_Crimes = "D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb/LA_Crimes"
LAPD_Divisions = "D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb/LAPD_Divisions"
LA_Streets_with_Crimes = "D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb/LA_Streets_with_Crimes"
LA_Streets_with_Crimes_by_Division = "D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb/LA_Streets_with_Crimes_by_Division"

arcpy.analysis.SpatialJoin(LACity_Walking_Streets, LA_Crimes, LA_Streets_with_Crimes, join_operation='JOIN_ONE_TO_MANY', match_option='WITHIN_A_DISTANCE', search_radius='50 feet')

arcpy.analysis.SpatialJoin(LA_Streets_with_Crimes, LAPD_Divisions, LA_Streets_with_Crimes_by_Division, join_operation='JOIN_ONE_TO_ONE', match_option='HAVE_THEIR_CENTER_IN')

LA_Streets_with_Crimes_by_Division_df = arcgis_table_to_df(LA_Streets_with_Crimes_by_Division)
LA_Streets_with_Crimes_by_Division_df = LA_Streets_with_Crimes_by_Division_df[LA_Streets_with_Crimes_by_Division_df['DR_NO'].notnull()]

LA_Streets_with_Crimes_by_Division_df.to_csv('D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data/CA_Los Angeles/Crimes/LA_Streets_with_Crimes_By_Division.csv')