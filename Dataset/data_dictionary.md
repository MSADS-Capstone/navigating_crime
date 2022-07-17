## Data Dictionary    

### Los Angeles Crime  

<div class="tg-wrap"><table id="tg-iu8FS" style="undefined;table-layout: fixed; width: 1003px">
<colgroup>
<col style="width: 258px">
<col style="width: 494px">
<col style="width: 251px">
</colgroup>
<thead>
  <tr>
    <th>Column Name</th>
    <th>Description</th>
    <th>Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>DR_NO</td>
    <td>Division   of Records Number: Official file number made up of a 2 digit year, area ID, and 5 digits</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Date Rptd</td>
    <td>MM/DD/YYYY</td>
    <td>Date &amp; Time</td>
  </tr>
  <tr>
    <td>DATE OCC</td>
    <td>MM/DD/YYYY</td>
    <td>Date &amp; Time</td>
  </tr>
  <tr>
    <td>TIME OCC</td>
    <td>In 24 hour military time.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>AREA</td>
    <td>The   LAPD has 21 Community Police Stations referred to as Geographic Areas within   the department. These Geographic Areas are sequentially numbered from 1-21.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>AREA NAME</td>
    <td>The   21 Geographic Areas or Patrol Divisions are also given a name designation   that references a landmark or the surrounding community that it is   responsible for. For example 77th Street Division is located at the   intersection of South Broadway and 77th Street, serving neighborhoods in   South Los Angeles.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Rpt Dist No</td>
    <td><a href="http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4" target="_blank" rel="noopener noreferrer">A four-digit code that represents a sub-area within a Geographic Area. All   crime records reference the "RD" that it occurred in for   statistical comparisons. Find LAPD Reporting Districts on the LA City GeoHub   at http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4</a></td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Part 1-2</td>
    <td> </td>
    <td>Number</td>
  </tr>
  <tr>
    <td>Crm Cd</td>
    <td>Indicates   the crime committed. (Same as Crime Code 1)</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Crm Cd Desc</td>
    <td>Defines   the Crime Code provided.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Mocodes</td>
    <td><a href="https://data.lacity.org/api/views/y8tr-7khq/files/3a967fbd-f210-4857-bc52-60230efe256c?download=true&filename=MO%20CODES%20(numerical%20order).pdf" target="_blank" rel="noopener noreferrer">Modus Operandi: Activities associated with the suspect in commission of   the crime.See attached PDF for list of MO Codes in numerical   order. https://data.lacity.org/api/views/y8tr-7khq/files/3a967fbd-f210-4857-bc52-60230efe256c?download=true&amp;filename=MO%20CODES%20(numerical%20order).pdf</a></td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Vict Age</td>
    <td>Two   character numeric</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Vict Sex</td>
    <td>F   - Female M - Male X - Unknown</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Vict Descent</td>
    <td>Descent   Code: A - Other Asian B - Black C - Chinese D - Cambodian F - Filipino G -   Guamanian H - Hispanic/Latin/Mexican I - American Indian/Alaskan Native J -   Japanese K - Korean L - Laotian O - Other P - Pacific Islander S - Samoan U -   Hawaiian V - Vietnamese W - White X - Unknown Z - Asian Indian</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Premis Cd</td>
    <td>The   type of structure, vehicle, or location where the crime took place.</td>
    <td>Number</td>
  </tr>
  <tr>
    <td>Premis Desc</td>
    <td>Defines   the Premise Code provided.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Weapon Used Cd</td>
    <td>The   type of weapon used in the crime.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Weapon Desc</td>
    <td>Defines   the Weapon Used Code provided.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Status</td>
    <td>Status   of the case. (IC is the default)</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Status Desc</td>
    <td>Defines   the Status Code provided.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Crm Cd 1</td>
    <td>Indicates   the crime committed. Crime Code 1 is the primary and most serious one. Crime Code 2, 3, and 4 are respectively less serious offenses. Lower crime class   numbers are more serious.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Crm Cd 2</td>
    <td>May   contain a code for an additional crime, less serious than Crime Code 1.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Crm Cd 3</td>
    <td>May   contain a code for an additional crime, less serious than Crime Code 1.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Crm Cd 4</td>
    <td>May   contain a code for an additional crime, less serious than Crime Code 1.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>LOCATION</td>
    <td>Street   address of crime incident rounded to the nearest hundred block to maintain   anonymity.</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>Cross Street</td>
    <td>Cross   Street of rounded Address</td>
    <td>Plain Text</td>
  </tr>
  <tr>
    <td>LAT</td>
    <td>Latitude</td>
    <td>Number</td>
  </tr>
  <tr>
    <td>LON</td>
    <td>Longtitude</td>
    <td>Number</td>
  </tr>
</tbody>
</table></div>


### Los Angeles Streets


<div class="tg-wrap"><table id="tg-nLUGa">
<thead>
  <tr>
    <th>Field Name</th>
    <th>Alias</th>
    <th>Data Type</th>
    <th>Allow Null</th>
    <th>Domain</th>
    <th>Default Value</th>
    <th>Length</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>OBJECTID</td>
    <td> </td>
    <td>Object ID</td>
    <td>FALSE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>Shape</td>
    <td> </td>
    <td>Geometry</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>FullName</td>
    <td>FullName</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>255</td>
  </tr>
  <tr>
    <td>Type</td>
    <td>Type</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>40</td>
  </tr>
  <tr>
    <td>Elevation</td>
    <td>Elevation</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>30</td>
  </tr>
  <tr>
    <td>Surface</td>
    <td>Surface</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>15</td>
  </tr>
  <tr>
    <td>Status</td>
    <td>Status</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>25</td>
  </tr>
  <tr>
    <td>DrivingDir</td>
    <td>DrivingDir</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>30</td>
  </tr>
  <tr>
    <td>From_L</td>
    <td>From_L</td>
    <td>Long</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>From_R</td>
    <td>From_R</td>
    <td>Long</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>To_L</td>
    <td>To_L</td>
    <td>Long</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>To_R</td>
    <td>To_R</td>
    <td>Long</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>Parity_L</td>
    <td>Parity_L</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>7</td>
  </tr>
  <tr>
    <td>Parity_R</td>
    <td>Parity_R</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>7</td>
  </tr>
  <tr>
    <td>StPreDir</td>
    <td>StPreDir</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>2</td>
  </tr>
  <tr>
    <td>StPreMod</td>
    <td>StPreMod</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>15</td>
  </tr>
  <tr>
    <td>StPreType</td>
    <td>StPreType</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>50</td>
  </tr>
  <tr>
    <td>StArticle</td>
    <td>StArticle</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>10</td>
  </tr>
  <tr>
    <td>StName</td>
    <td>StName</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>50</td>
  </tr>
  <tr>
    <td>StPostType</td>
    <td>StPostType</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>50</td>
  </tr>
  <tr>
    <td>StPostDir</td>
    <td>StPostDir</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>2</td>
  </tr>
  <tr>
    <td>StPostMod</td>
    <td>StPostMod</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>15</td>
  </tr>
  <tr>
    <td>Zip_L</td>
    <td>Zip_L</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>5</td>
  </tr>
  <tr>
    <td>Zip_R</td>
    <td>Zip_R</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>5</td>
  </tr>
  <tr>
    <td>LCity_L</td>
    <td>LCity_L</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>30</td>
  </tr>
  <tr>
    <td>LCity_R</td>
    <td>LCity_R</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>30</td>
  </tr>
  <tr>
    <td>NameCat_L</td>
    <td>NameCat_L</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>10</td>
  </tr>
  <tr>
    <td>NameCat_R</td>
    <td>NameCat_R</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>10</td>
  </tr>
  <tr>
    <td>Accuracy</td>
    <td>Accuracy</td>
    <td>Double</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>Jurisdiction</td>
    <td>Jurisdiction</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>10</td>
  </tr>
  <tr>
    <td>Source</td>
    <td>Source</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>20</td>
  </tr>
  <tr>
    <td>SourceID</td>
    <td>SourceID</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>50</td>
  </tr>
  <tr>
    <td>UpdateDate</td>
    <td>UpdateDate</td>
    <td>Date</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>MSAG_LCity</td>
    <td>MSAG_LCity</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>20</td>
  </tr>
  <tr>
    <td>MSAG_RCity</td>
    <td>MSAG_RCity</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>20</td>
  </tr>
  <tr>
    <td>MSAG_LESN</td>
    <td>MSAG_LESN</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>3</td>
  </tr>
  <tr>
    <td>MSAG_RESN</td>
    <td>MSAG_RESN</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>3</td>
  </tr>
  <tr>
    <td>Shape_Length</td>
    <td> </td>
    <td>Double</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
</tbody>
</table></div>
