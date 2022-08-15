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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a. [Los Angeles Crime - Web Mapping Application](https://chrisrobinson.maps.arcgis.com/apps/webappviewer/index.html?id=5b3684334cf14070b09650392eecd26b)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b. [Los Angeles Crime - Exploratory Overview and Modeling](https://crime-data-la.herokuapp.com/)  

### Code Library

<div class="tg-wrap"><table>
<tbody>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Main_Notebook.ipynb" target="_blank" rel="noopener noreferrer">Main Notebook</a></td>
    <td>This notebook contains the primary code base for the data science portions of the project, consisting of Data Exploration Phase I, Data Preparation, Data Exploration Phase II, and Modeling.  </td>
  </tr>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/Python_CrimeData_Downloader.py" target="_blank" rel="noopener noreferrer">Python Crime Data Downloader</a></td>
    <td>This file downloads the data from the LAPD website and filters out non-violent crime.  </td>
  </tr>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/ArcGIS_Data_Processing.py" target="_blank" rel="noopener noreferrer">ArcGIS Data Processing</a></td>
    <td>This file georeferences the downloaded crime data and joins it to LA streets, creating the raw dataset for use in modeling.  </td>
  </tr>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_preparation.ipynb" target="_blank" rel="noopener noreferrer">Data Preparation</a></td>
    <td>This notebook provides a data report mapping to unique ID fields, column names, data types, null counts, and percentages in the dataframe. It also shows some basic bar graphs for an initial cursory overview of data exploration.  </td>
  </tr>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_exploration_phase1.ipynb" target="_blank" rel="noopener noreferrer">Data Exploration Phase I</a></td>
    <td>This notebook preprocesses the dataframe, allowing for further exploration to take place and sets the stage for modeling.  </td>
  </tr>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/data_exploration_phase2.ipynb" target="_blank" rel="noopener noreferrer">Data Exploration Phase II</a></td>
    <td>This notebook takes a more granular look into the columns of interest using boxplots, stacked bar graphs, histograms, and culminates with a correlation matrix.  </td>
  </tr>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/functions.py">Functions</a></td>
    <td>This file creates functions for data types and various plots that are used throughout the project pipeline.  </td>
  </tr>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/modeling.ipynb">Modeling</a></td>
    <td>This notebook contains all of the machine learning algorithms carried out in this project.  </td>
  </tr>
  <tr>
    <td><a href="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Code%20Library/Python_CrimeData_Uploader.py" target="_blank" rel="noopener noreferrer">Python Crime Data Uploader</a></td>
    <td>This file processes the final model output. Creates the final street predictions, dangerous street points, and filtered crime locations datasets.</td>
  </tr>
</tbody>
</table></div>

### Data 
[DataFolder](https://github.com/MSADS-Capstone/navigating_crime/tree/main/Data%20Folder)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a. [Data Dictionary](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Data%20Folder/Reports/data_dictionary.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b. [Data Report](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Data%20Folder/Reports/data_report.txt)



### Project Workflow Diagram  

<p align = "center">
  <img src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/EDA%20Images/Project_Workflow.jpeg">
</p>

### Visualizations
![](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/EDA%20Images/boxplot1.png)

`Summarizing Vict_Age`      
`The first quartile is 24.0.`    
`The third quartile is 46.0.`    
`The IQR is 22.0.`     
`The mean is 34.51.`    
`The standard deviation is 16.86.`      
`The median is 33.0.`    
`The distribution is positively skewed.`   

![](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/EDA%20Images/victim_sex_stacked_bar.png)

> Whereas there are more males than females in this dataset, it can be seen from both the regular and normalized distributions, respectively, that more serious crimes occur with a higher prevalence (69,370 or 64.24%) for the former than the latter (28,565 or 41.70%). For sexes unknown, there is a 36.70% prevalence rate for more serious crimes.

| **Victim_Sex** | **Less Serious** | **More Serious** | **Total** | **% More Serious** |
|---------------:|-----------------:|-----------------:|----------:|-------------------:|
|          **F** |            39936 |            28565 |     68501 |              41.70 |
|          **M** |            38615 |            69370 |    107985 |              64.24 |
|          **X** |             4219 |             2446 |      6665 |              36.70 |
|      **Total** |            82770 |           100381 |    183151 |              54.81 |




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
