import pandas as pd
import numpy as np
import json
import csv
from google.oauth2 import service_account
import pygsheets
import requests
import os
from datetime import datetime
import zipfile


client = pygsheets.authorize(service_account_file = 'D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/service_account.json')
sheet = client.open_by_key('1lbh-GfM6o_X1oN6Xa8Rl2z_CZt828o-4AHXfXLWXQQQ') 
wks = sheet.worksheet_by_title('GIS Data Sources')
DataSources_df = wks.get_as_df()

#Create State_County string for folder creation
DataSources_df['state_county'] = DataSources_df['State'] + '_' + DataSources_df['County']

#Get date
now = datetime.now()
dt_string = now.strftime("%Y%m%d")

# Parent Directory path
parent_dir = "D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data"

#Create list of state_county
state_county_list = DataSources_df['state_county'].tolist()

#Download and extract crimes
def downloadCrimes():

    #Replace "" with NaN for next step
    DataSources_df['Crimes'].replace('', np.nan, inplace=True)

    #Drop rows with NaN in target column
    DataSources_df.dropna(subset=['Crimes'], inplace=True)

    crimes_url_list = DataSources_df['Crimes'].tolist()

    for i, st_cnty in enumerate(state_county_list):
        crimes_url = crimes_url_list[i]
        print(f"URL for {st_cnty} is {crimes_url}")

        directory = f"{st_cnty}/Crimes"

        path = os.path.join(parent_dir, directory)

        os.makedirs(path, exist_ok=True)

        downloaded_obj = requests.get(crimes_url, allow_redirects=True)
        open(f'D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data/{st_cnty}/Crimes/incoming_{dt_string}.csv', 'wb').write(downloaded_obj.content)

        '''
        # If the data is zipped
        with zipfile.ZipFile(f'D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data/{st_cnty}/Parcels/incoming_{dt_string}.zip', 'r') as zip_ref:
            zip_ref.extractall(f'D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data/{st_cnty}/Parcels/incoming_{dt_string}')
    
        os.remove(f'D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data/{st_cnty}/Parcels/incoming_{dt_string}.zip')
        '''
        # Read in dowloaded crime data
        crimesdf = pd.read_csv(f'D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data/{st_cnty}/Crimes/incoming_{dt_string}.csv')

        # Filter out non-violent crime
        crimesdf = crimesdf[crimesdf["Crm Cd"].isin([110,113,121,122,210,220,230,231,235,236,237,251,434,435,436,451,452,622,622,
        623,624,625,626,627,753,761,762,763,805,806,810,812,813,814,815,820,821,822,830,840,850,860,910,920,921])]

        # Filter only crimes occuring on the street, sidewalk, alley, driveway, crosswalk, tunnel, parking lot, Park or vacant lot
        crimesdf = crimesdf[crimesdf["Premis Cd"].isin([100,101,102,103,104,105,106,107,108,109])]

        #Export filtered dataset
        crimesdf.to_csv(f'D:/data/projects/00000-Misc/USD/Capstone_Project/Python_CrimeData_Downloader/Data/{st_cnty}/Crimes/Filtered_{dt_string}.csv')
        

downloadCrimes()
