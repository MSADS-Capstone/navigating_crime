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


client = pygsheets.authorize(service_account_file=r'C:\Users\Chris\Desktop\Python_CrimeData_Downloader\service_account.json')
sheet = client.open_by_key('1lbh-GfM6o_X1oN6Xa8Rl2z_CZt828o-4AHXfXLWXQQQ') 
wks = sheet.worksheet_by_title('GIS Data Sources')
DataSources_df = wks.get_as_df()

#Create State_County string for folder creation
DataSources_df['state_county'] = DataSources_df['State'] + '_' + DataSources_df['County']

#Get date
now = datetime.now()
dt_string = now.strftime("%Y%m%d")

# Parent Directory path
parent_dir = "C:/Users/Chris/Desktop/Python_CrimeData_Downloader/Data"

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
        open(f'C:/Users/Chris/Desktop/Python_CrimeData_Downloader/Data/{st_cnty}/Crimes/incoming_{dt_string}.csv', 'wb').write(downloaded_obj.content)

        '''
        # If the data is zipped
        with zipfile.ZipFile(f'C:/Users/Chris/Desktop/Python_CrimeData_Downloader/Data/{st_cnty}/Parcels/incoming_{dt_string}.zip', 'r') as zip_ref:
            zip_ref.extractall(f'C:/Users/Chris/Desktop/Python_CrimeData_Downloader/Data/{st_cnty}/Parcels/incoming_{dt_string}')
    
        os.remove(f'C:/Users/Chris/Desktop/Python_CrimeData_Downloader/Data/{st_cnty}/Parcels/incoming_{dt_string}.zip')
        '''


downloadCrimes()