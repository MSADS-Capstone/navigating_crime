---
title: "Data Dictionary"

---

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-fymr{border-color:inherit;font-weight:bold;text-align:left;vertical-align:top}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
<div class="tg-wrap"><table class="tg" style="undefined;table-layout: fixed; width: 708px">
<colgroup>
<col style="width: 121px">
<col style="width: 491px">
<col style="width: 96px">
</colgroup>
<thead>
  <tr>
    <th class="tg-fymr">Column&nbsp;&nbsp;&nbsp;Name</th>
    <th class="tg-7btt">Description</th>
    <th class="tg-fymr">Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">DR_NO</td>
    <td class="tg-0pky">Division&nbsp;&nbsp;&nbsp;of Records Number: Official file number made up of a 2 digit year, area ID,&nbsp;&nbsp;&nbsp;and 5 digits</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Date Rptd</td>
    <td class="tg-0pky">MM/DD/YYYY</td>
    <td class="tg-0pky">Date&nbsp;&nbsp;&nbsp;&amp; Time</td>
  </tr>
  <tr>
    <td class="tg-0pky">DATE OCC</td>
    <td class="tg-0pky">MM/DD/YYYY</td>
    <td class="tg-0pky">Date&nbsp;&nbsp;&nbsp;&amp; Time</td>
  </tr>
  <tr>
    <td class="tg-0pky">TIME OCC</td>
    <td class="tg-0pky">In 24 hour military time.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">AREA</td>
    <td class="tg-0pky">The&nbsp;&nbsp;&nbsp;LAPD has 21 Community Police Stations referred to as Geographic Areas within&nbsp;&nbsp;&nbsp;the department. These Geographic Areas are sequentially numbered from 1-21.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">AREA NAME</td>
    <td class="tg-0pky">The&nbsp;&nbsp;&nbsp;21 Geographic Areas or Patrol Divisions are also given a name designation&nbsp;&nbsp;&nbsp;that references a landmark or the surrounding community that it is&nbsp;&nbsp;&nbsp;responsible for. For example 77th Street Division is located at the&nbsp;&nbsp;&nbsp;intersection of South Broadway and 77th Street, serving neighborhoods in&nbsp;&nbsp;&nbsp;South Los Angeles.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Rpt Dist No</td>
    <td class="tg-0pky"><a href="http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4">A four-digit code that represents a sub-area within a Geographic Area. All&nbsp;&nbsp;&nbsp;crime records reference the "RD" that it occurred in for&nbsp;&nbsp;&nbsp;statistical comparisons. Find LAPD Reporting Districts on the LA City GeoHub&nbsp;&nbsp;&nbsp;at http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4</a></td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Part 1-2</td>
    <td class="tg-0pky"> </td>
    <td class="tg-0pky">Number</td>
  </tr>
  <tr>
    <td class="tg-0pky">Crm Cd</td>
    <td class="tg-0pky">Indicates&nbsp;&nbsp;&nbsp;the crime committed. (Same as Crime Code 1)</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Crm Cd Desc</td>
    <td class="tg-0pky">Defines&nbsp;&nbsp;&nbsp;the Crime Code provided.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Mocodes</td>
    <td class="tg-0pky"><a href="https://data.lacity.org/api/views/y8tr-7khq/files/3a967fbd-f210-4857-bc52-60230efe256c?download=true&filename=MO%20CODES%20(numerical%20order).pdf">Modus Operandi: Activities associated with the suspect in commission of&nbsp;&nbsp;&nbsp;the crime.See attached PDF for list of MO Codes in numerical&nbsp;&nbsp;&nbsp;order. https://data.lacity.org/api/views/y8tr-7khq/files/3a967fbd-f210-4857-bc52-60230efe256c?download=true&amp;filename=MO%20CODES%20(numerical%20order).pdf</a></td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Vict Age</td>
    <td class="tg-0pky">Two&nbsp;&nbsp;&nbsp;character numeric</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Vict Sex</td>
    <td class="tg-0pky">F&nbsp;&nbsp;&nbsp;- Female M - Male X - Unknown</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Vict Descent</td>
    <td class="tg-0pky">Descent&nbsp;&nbsp;&nbsp;Code: A - Other Asian B - Black C - Chinese D - Cambodian F - Filipino G -&nbsp;&nbsp;&nbsp;Guamanian H - Hispanic/Latin/Mexican I - American Indian/Alaskan Native J -&nbsp;&nbsp;&nbsp;Japanese K - Korean L - Laotian O - Other P - Pacific Islander S - Samoan U -&nbsp;&nbsp;&nbsp;Hawaiian V - Vietnamese W - White X - Unknown Z - Asian Indian</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Premis Cd</td>
    <td class="tg-0pky">The&nbsp;&nbsp;&nbsp;type of structure, vehicle, or location where the crime took place.</td>
    <td class="tg-0pky">Number</td>
  </tr>
  <tr>
    <td class="tg-0pky">Premis Desc</td>
    <td class="tg-0pky">Defines&nbsp;&nbsp;&nbsp;the Premise Code provided.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Weapon Used Cd</td>
    <td class="tg-0pky">The&nbsp;&nbsp;&nbsp;type of weapon used in the crime.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Weapon Desc</td>
    <td class="tg-0pky">Defines&nbsp;&nbsp;&nbsp;the Weapon Used Code provided.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Status</td>
    <td class="tg-0pky">Status&nbsp;&nbsp;&nbsp;of the case. (IC is the default)</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Status Desc</td>
    <td class="tg-0pky">Defines&nbsp;&nbsp;&nbsp;the Status Code provided.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Crm Cd 1</td>
    <td class="tg-0pky">Indicates&nbsp;&nbsp;&nbsp;the crime committed. Crime Code 1 is the primary and most serious one. Crime&nbsp;&nbsp;&nbsp;Code 2, 3, and 4 are respectively less serious offenses. Lower crime class&nbsp;&nbsp;&nbsp;numbers are more serious.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Crm Cd 2</td>
    <td class="tg-0pky">May&nbsp;&nbsp;&nbsp;contain a code for an additional crime, less serious than Crime Code 1.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Crm Cd 3</td>
    <td class="tg-0pky">May&nbsp;&nbsp;&nbsp;contain a code for an additional crime, less serious than Crime Code 1.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Crm Cd 4</td>
    <td class="tg-0pky">May&nbsp;&nbsp;&nbsp;contain a code for an additional crime, less serious than Crime Code 1.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">LOCATION</td>
    <td class="tg-0pky">Street&nbsp;&nbsp;&nbsp;address of crime incident rounded to the nearest hundred block to maintain&nbsp;&nbsp;&nbsp;anonymity.</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">Cross Street</td>
    <td class="tg-0pky">Cross&nbsp;&nbsp;&nbsp;Street of rounded Address</td>
    <td class="tg-0pky">Plain&nbsp;&nbsp;&nbsp;Text</td>
  </tr>
  <tr>
    <td class="tg-0pky">LAT</td>
    <td class="tg-0pky">Latitude</td>
    <td class="tg-0pky">Number</td>
  </tr>
  <tr>
    <td class="tg-0pky">LON</td>
    <td class="tg-0pky">Longtitude</td>
    <td class="tg-0pky">Number</td>
  </tr>
</tbody>
</table></div>