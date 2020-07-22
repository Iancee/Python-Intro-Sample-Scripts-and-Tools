#Script to create a shapefile of bikeable businesses in SF
import os
import arcpy

#Set environmental workspace
arcpy.env.workspace = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\GIS_Data\SF_SHPs"

#Set location for output of geoprocessing tools
output_folder = r"C:\Users\ian.conroy\Desktop\Bay Geo Classes\Python Class\Output_Folder"

#Create buffer of bike network
print('Creating buffer')
arcpy.Buffer_analysis("SF_Bike_Network.shp", os.path.join(output_folder, 'SF_Bike_Network.shp'), "25 Feet", "FULL", "ROUND")

#Create shapefile of businesses along bike routes
print('Clipping businesses by bike route buffer')
arcpy.Clip_analysis("SF_Businesses.shp", os.path.join(output_folder, 'SF_Bike_Network.shp'), os.path.join(output_folder, 'Bikeable_Businesses.shp'))
