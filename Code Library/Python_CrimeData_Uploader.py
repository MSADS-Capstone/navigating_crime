#########################################################################################
##  This file processes the final model output. Creates the final street predictions,  ## 
##  dangerous street points, and filtered crime locations datasets.                    ##
#########################################################################################

import arcpy
import os, sys
from arcgis.gis import GIS

# Set environment settings
workspace = arcpy.env.workspace = 'D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb'
outWorkspace = 'D:/data/projects/00000-Misc/USD/Capstone_Project/Data/MADS_CapstoneProject_Data.gdb'

# Set the local variables
table_path = 'D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader'

in_predictions = table_path + '/df_preds_xgb_final.csv'
Final_out_feature_class = 'LACity_Walking_Streets_with_Predictions'
df_preds_xgb_final = 'df_preds_xgb_final'

# Load the csv file into the database
arcpy.TableToTable_conversion(in_predictions, outWorkspace, df_preds_xgb_final)

# Join the predictions back to the original street data by OBJECTID
# Join the feature layer to a table

inFeatures = 'LA_Streets_with_Crimes'
joinTable = 'df_preds_xgb_final'
joinField = 'OBJECTID'
outFeature = 'LA_Streets_with_Predictions_Temp'

predictions_joined_table = arcpy.AddJoin_management(inFeatures, joinField, joinTable, joinField)

# Copy the layer to a new permanent feature class
arcpy.CopyFeatures_management(predictions_joined_table, outFeature)

summary_input = 'LA_Streets_with_Predictions_Temp'
statsFields = [['StreetOID", "Count']]
caseField = [['StreetOID']]
summary_table = 'Predictions_Summary'

# Summarize table on StreetOID taking Max Prediction
# This will give us the count of crimes on the street segment as well as the Max Probability that a crime will occur
arcpy.analysis.Statistics(summary_input, summary_table, statsFields, caseField)

fc = 'Predictions_Summary'
fields = ['MAX_df_preds_xgb_final_Predictions']

# Create update cursor for Predictions 
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        if (row[0] == None):
            row[0] = 0
        # Update the cursor with the updated list
        cursor.updateRow(row)

# Join variables
inFeatures2 = 'LACity_Walking_Streets'
joinTable2 = 'Predictions_Summary'
joinField2 = 'StreetOID'
joinField3 = 'LA_Streets_with_Crimes_StreetOID'

# Join summary table back to the Streets dataset
predictions_joined_table = arcpy.AddJoin_management(inFeatures2, joinField2, joinTable2, joinField3)

# Copy the layer to a new permanent feature class
arcpy.CopyFeatures_management(predictions_joined_table, Final_out_feature_class)

# Create dangerous street flag layer
outFeatureClass2 = 'Dangerous_LA_Streets_Points_temp'
outFeatureClass3 = 'Dangerous_LA_Streets_Points'
expression = '(MAX_df_preds_xgb_final_Predictions > .98) AND (FREQUENCY > 32)'

arcpy.FeatureClassToFeatureClass_conversion(Final_out_feature_class, outWorkspace, outFeatureClass2, expression)

arcpy.FeatureToPoint_management(outFeatureClass2, outFeatureClass3, "CENTROID")

# Upload the data to the ArcGIS Service used in the crime navigation app

aprxPath = 'D:/data/projects/00000-Misc/USD/Capstone_Project/MADS_Capstone_Project.aprx'

sd_fs_name = 'Los Angeles Crimes'
portal = 'http://www.arcgis.com'
user = 'username'
password = 'password'

shareOrg = True
shareEveryone = False
shareGroups = ""

relPath = 'D:/data/projects/00000-Misc/USD/Capstone_Project'
sddraft = os.path.join(relPath, 'Los_Angeles_Crimes.sddraft')
sd = os.path.join(relPath, 'Los_Angeles_Crimes.sd')

# Creating SD file
arcpy.env.overwriteOutput = True
prj = arcpy.mp.ArcGISProject(aprxPath)
mp = prj.listMaps()[0]

sharing_draft = mp.getWebLayerSharingDraft('HOSTING_SERVER", "FEATURE', sd_fs_name)
sharing_draft.summary = 'Draft Summary'
sharing_draft.tags = 'Draft Tags'
sharing_draft.description = 'Draft Description'
sharing_draft.credits = 'Draft Credits'
sharing_draft.useLimitations = 'Draft Use Limitations'

sharing_draft.exportToSDDraft(sddraft)
arcpy.StageService_server(sddraft, sd)

# Connecting to portal
gis = GIS(portal, user, password)

# Find the SD, update it, publish /w overwrite and set sharing and metadata
sdItem = gis.content.search(query=sd_fs_name, item_type='Service Definition')
i=0
while sdItem[i].title != sd_fs_name:
            i += 1

item = sdItem[i] 
item.update(data=sd)

# Overwriting existing feature service
fs = item.publish(overwrite=True)

if shareOrg or shrEveryone or shrGroups:
    fs.share(org=shrOrg, everyone=shrEveryone, groups=shrGroups)
