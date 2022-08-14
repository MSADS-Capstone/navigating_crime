# MSADS599: Capstone - Identifying Safer Pedestrian Routes in Los Angeles

<p align = "center">
  <img src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/la_safe_street_routes.gif">
</p>

This is a Capstone project for the University of San Diego's M.S. in Applied Data Science program. 

## Project Status: Complete

## Installation

To use this project, first clone the repo on your device using the commands below:

`git init`

`git clone https://github.com/MSADS-Capstone/navigating_crime.git`

## Partners/Contributors/Authors  
* [Leonid Shpaner](https://github.com/lshpaner)  
* [Christopher Robinson](https://github.com/ChrisRobinsonUSD)  
* [Jose Luis Estrada](https://github.com/jose-luis-estrada)  

# Table of Contents
--------
1. [Methods](#Methods)
2. [Technologies](#Technologies)
3. [Project Objective](#Project_Objective)
4. [Project Overview](#project_overview)
5. [Web Applications](#web-applications)
6. [Code Library](#code-library)
7. [Data](#data)
8. [Project Workflow Diagram](#project-workflow-diagram)
9. [Visualizations](#visualizations)
--------

### Methods  
* Data Exploration  
* Pre-processing  
* Data Visualization  
* Statistical modeling  
* Data modeling metrics  

### Technologies  
* Python
* ArcGIS
* Dash Plotly

## Project Objective

This project examines pedestrian safety using machine learning and recent crime data. The goal is to automate a process to identify the safest route between locations, as well as provide additional up to date crime information. This project identifies the “safest” route, which does not guarantee the route is safe. In some instances, there is no “safe” route. Additionally, factors such as time of day and personal traits like age, sex, and race are elements of safety. The solution discussed here not only identifies the safest route but includes elements of situational awareness to assist in making the best decision possible regarding personal safety. When it comes to navigating an area safely, recommendations can be made, but ultimately it is up to the navigator to determine what level of risk is acceptable.

## Project Overview
The project commences by downloading the data from LAPD and filtering out non-violent crime. The data is georeferenced and spatially joined to the Los Angeles street GIS dataset. It is then preprocessed and a flat .csv file is provided for further examination, preprocessing, and modeling. The final model output is then incorporated into a [web mapping application](https://chrisrobinson.maps.arcgis.com/apps/webappviewer/index.html?id=5b3684334cf14070b09650392eecd26b) which allows the end-user to create turn-by-turn directions avoiding dangerous streets. 

### Web Applications
a. [Los Angeles Crime - Web Mapping Application](https://chrisrobinson.maps.arcgis.com/apps/webappviewer/index.html?id=5b3684334cf14070b09650392eecd26b)  
b. [Los Angeles Crime - Exploratory Overview and Modeling](https://crime-data-la.herokuapp.com/)  

### Code Library

<div class="tg-wrap"><table id="tg-ND3hE">
<thead>
  <tr>
    <th>[Main Notebook](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Main_Notebook.ipynb)</th>
    <th>this notebook contains the primary   code base for the data science portions of the project, consisting of Data   Exploration Phase I, Data Preparation, Data Exploration Phase II, and   Modeling.  </th>
    <th>Data Type</th>
    <th>Allow Null</th>
    <th>Domain</th>
    <th>Default Value</th>
    <th>Length</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>[Python   Crime Data Downloader](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/Python_CrimeData_Downloader.py)</td>
    <td>this file downloads the data from the LAPD website and filters   out non-violent crime.  </td>
    <td>Object ID</td>
    <td>FALSE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>[ArcGIS   Data Processing](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/ArcGIS_Data_Processing.py)</td>
    <td>this file georeferences the downloaded crime data and joins it   to LA streets, creating the raw dataset for use in modeling.  </td>
    <td>Geometry</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td>[Data   Preparation](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_preparation.ipynb)</td>
    <td>this notebook provides a data report mapping to unique ID   fields, column names, data types, null counts, and percentages in the   dataframe. It also shows some basic bar graphs for an initial cursory   overview of data exploration.  </td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>255</td>
  </tr>
  <tr>
    <td>[Data   Exploration Phase I](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_exploration_phase1.ipynb)</td>
    <td>this notebook preprocesses the dataframe, allowing for further   exploration to take place and sets the stage for modeling.  </td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>40</td>
  </tr>
  <tr>
    <td>[Data   Exploration Phase II](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_exploration_phase2.ipynb)</td>
    <td>this notebook takes a more granular look into the columns of   interest using boxplots, stacked bar graphs, histograms, and culimates with a   correlation matrix.  </td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>30</td>
  </tr>
  <tr>
    <td>[Functions](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/functions.py)</td>
    <td>this file creates functions for data types and various plots   that are used throughout the project pipeline.  </td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>15</td>
  </tr>
  <tr>
    <td>[Modeling](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/modeling.ipynb)</td>
    <td>this notebook contains all of the machine learning algorithms   carried out in this project.  </td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>25</td>
  </tr>
  <tr>
    <td>[Python  Crime Data Uploader](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/Python_CrimeData_Uploader.py)</td>
    <td>this file processes the final model output.  Creates the   final street predictions, dangerous street points, and filtered crime   locations datasets.</td>
    <td>Text</td>
    <td>TRUE</td>
    <td> </td>
    <td> </td>
    <td>30</td>
  </tr>
</tbody>
</table></div>
<script charset="utf-8">var TGSort=window.TGSort||function(n){"use strict";function r(n){return n?n.length:0}function t(n,t,e,o=0){for(e=r(n);o<e;++o)t(n[o],o)}function e(n){return n.split("").reverse().join("")}function o(n){var e=n[0];return t(n,function(n){for(;!n.startsWith(e);)e=e.substring(0,r(e)-1)}),r(e)}function u(n,r,e=[]){return t(n,function(n){r(n)&&e.push(n)}),e}var a=parseFloat;function i(n,r){return function(t){var e="";return t.replace(n,function(n,t,o){return e=t.replace(r,"")+"."+(o||"").substring(1)}),a(e)}}var s=i(/^(?:\s*)([+-]?(?:\d+)(?:,\d{3})*)(\.\d*)?$/g,/,/g),c=i(/^(?:\s*)([+-]?(?:\d+)(?:\.\d{3})*)(,\d*)?$/g,/\./g);function f(n){var t=a(n);return!isNaN(t)&&r(""+t)+1>=r(n)?t:NaN}function d(n){var e=[],o=n;return t([f,s,c],function(u){var a=[],i=[];t(n,function(n,r){r=u(n),a.push(r),r||i.push(n)}),r(i)<r(o)&&(o=i,e=a)}),r(u(o,function(n){return n==o[0]}))==r(o)?e:[]}function v(n){if("TABLE"==n.nodeName){for(var a=function(r){var e,o,u=[],a=[];return function n(r,e){e(r),t(r.childNodes,function(r){n(r,e)})}(n,function(n){"TR"==(o=n.nodeName)?(e=[],u.push(e),a.push(n)):"TD"!=o&&"TH"!=o||e.push(n)}),[u,a]}(),i=a[0],s=a[1],c=r(i),f=c>1&&r(i[0])<r(i[1])?1:0,v=f+1,p=i[f],h=r(p),l=[],g=[],N=[],m=v;m<c;++m){for(var T=0;T<h;++T){r(g)<h&&g.push([]);var C=i[m][T],L=C.textContent||C.innerText||"";g[T].push(L.trim())}N.push(m-v)}t(p,function(n,t){l[t]=0;var a=n.classList;a.add("tg-sort-header"),n.addEventListener("click",function(){var n=l[t];!function(){for(var n=0;n<h;++n){var r=p[n].classList;r.remove("tg-sort-asc"),r.remove("tg-sort-desc"),l[n]=0}}(),(n=1==n?-1:+!n)&&a.add(n>0?"tg-sort-asc":"tg-sort-desc"),l[t]=n;var i,f=g[t],m=function(r,t){return n*f[r].localeCompare(f[t])||n*(r-t)},T=function(n){var t=d(n);if(!r(t)){var u=o(n),a=o(n.map(e));t=d(n.map(function(n){return n.substring(u,r(n)-a)}))}return t}(f);(r(T)||r(T=r(u(i=f.map(Date.parse),isNaN))?[]:i))&&(m=function(r,t){var e=T[r],o=T[t],u=isNaN(e),a=isNaN(o);return u&&a?0:u?-n:a?n:e>o?n:e<o?-n:n*(r-t)});var C,L=N.slice();L.sort(m);for(var E=v;E<c;++E)(C=s[E].parentNode).removeChild(s[E]);for(E=v;E<c;++E)C.appendChild(s[v+L[E-v]])})})}}n.addEventListener("DOMContentLoaded",function(){for(var t=n.getElementsByClassName("tg"),e=0;e<r(t);++e)try{v(t[e])}catch(n){}})}(document)</script>

- [Main Notebook](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Main_Notebook.ipynb): this notebook contains the primary code base for the data science portions of the project, consisting of Data Exploration Phase I, Data Preparation, Data Exploration Phase II, and Modeling.  

- [Python Crime Data Downloader](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/Python_CrimeData_Downloader.py): this file downloads the data from the LAPD website and filters out non-violent crime.  

- [ArcGIS Data Processing](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/ArcGIS_Data_Processing.py): this file georeferences the downloaded crime data and joins it to LA streets, creating the raw dataset for use in modeling.  

IV. [Data Exploration Phase I](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_exploration_phase1.ipynb): this notebook provides a data report mapping to unique ID fields, column names, data types, null counts, and percentages in the dataframe. It also shows some basic bar graphs for an initial cursory overview of data exploration.  

V. [Data Preparation](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_preparation.ipynb): this notebook preprocesses the dataframe, allowing for further exploration to take place and sets the stage for modeling.  

VI. [Data Exploration Phase II](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_exploration_phase2.ipynb): this notebook takes a more granular look into the columns of interest using boxplots, stacked bar graphs, histograms, and culimates with a correlation matrix.  

VII. [Functions](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/functions.py): this file creates functions for data types and various plots that are used throughout the project pipeline.  

VIII. [Modeling](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/modeling.ipynb): this notebook contains all of the machine learning algorithms carried out in this project.  

IX. [Python Crime Data Uploader](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/Python_CrimeData_Uploader.py): this file processes the final model output.  Creates the final street predictions, dangerous street points, and filtered crime locations datasets.

### Data 
* [DataFolder](https://github.com/MSADS-Capstone/navigating_crime/tree/main/Data%20Folder)  
      a. [Data Dictionary](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Data%20Folder/Reports/data_dictionary.md)  
      b. [Data Report](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Data%20Folder/Reports/data_report.txt)



### Project Workflow Diagram  

<p align = "center">
  <img src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/EDA%20Images/Project_Workflow.jpeg">
</p>

### Visualizations
* Boxplots
* Histograms
* Bar Graphs
* Correlation Matrix

### Modeling  
* Quadratic Discriminant Analysis (QDA)
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost

## References

Bura, D., Singh, M., & Nandal, P. (2019). Predicting Secure and Safe Route for Women using Google Maps. *2019 International Conference on Machine Learning, Big Data, Cloud and Parallel Computing (COMITCon).* https://doi.org/10.1109/comitcon.2019  

Chen T. & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.* 785-794. https://doi.org/10.1145/2939672.2939785  

City of Los Angeles. (2022). *Street Centerline* [Data set]. Los Angeles Open Data. https://data.lacity.org/City-Infrastructure-Service-Requests/Street-Centerline/7j4e-nn4z  

City of Los Angeles. (2022). *City Boundaries for Los Angeles County* [Data set]. Los Angeles Open Data. https://controllerdata.lacity.org/dataset/City-Boundaries-for-Los-Angeles-County/sttr-9nxz  

Kuhn, M., & Johnson, K. (2016). *Applied Predictive Modeling.* Springer. https://doi.org/10.1007/978-1-4614-6849-3  

Levy, S., Xiong, W., Belding, E., & Wang, W. Y. (2020). *SafeRoute: Learning to Navigate Streets Safely in an Urban Environment. ACM Transactions on Intelligent Systems and Technology, 11*(6), 1-17. https://doi.org/10.1145/3402818  

Lopez, G., 2022, April 17. A Violent Crisis. *The New York Times.* https://www.nytimes.com/2022/04/17/briefing/violent-crime-ukraine-war-week-ahead.html.  

Los Angeles Police Department. (2022). *Crime Data from 2020 to Present* [Data set]. https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8  

Pavate, A., Chaudhari, A., & Bansode, R. (2019). Envision of Route Safety Direction Using Machine Learning. *Acta Scientific Medical Sciences, 3*(11), 140–145. https://doi.org/10.31080/asms.2019.03.0452  

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., and Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12(Oct), 2825–2830.  

Tarkelar, S., Bhat, A., Pandhe, S., & Halarnkar, T. (2016). Algorithm to Determine the Safest Route. *(IJCSIT) International Journal of Computer Science and Information Technologies, 7*(3), 2016, 1536-1540. http://ijcsit.com/docs/Volume%207/vol7issue3/ijcsit20160703106.pdf  

Vandeviver, C. (2014). Applying Google Maps and Google Street View in criminological research. *Crime Science, 3*(1). https://doi.org/10.1186/s40163-014-0013-2  

Wang, Y. Li, Y., Yong S., Rong, X., Zhang, S. (2017). Improvement of ID3 algorithm based on simplified information entropy and coordination degree. *2017 Chinese Automation Congress (CAC)*, 1526-1530. https://doi.org/10.1109/CAC.2017.8243009
