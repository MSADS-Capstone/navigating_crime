# MSADS599: Capstone - Identifying Safer Pedestrian Routes in Los Angeles

<p align = "center">
  <img src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/Miscellaneous%20Images/la_safe_street_routes.gif">
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

<img align="left" width="150" height="150" src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/Miscellaneous%20Images/shpaner_leonid.jpg">

Leon is a Data Scientist at The Laura P. and Leland K. Whittier Virtual PICU at Children’s Hospital Los Angeles (CHLA). With over 10 years’ experience in analytics and teaching, he has collaborated on a wide variety of projects within financial services, education, personal development, and healthcare. He serves as a course facilitator for Data Analytics and Applied Statistics at Cornell University and is a newly minted lecturer of Statistics in Python for the University of San Diego’s M.S. Applied Artificial Intelligence program.

<img align="left" width="150" height="150" src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/Miscellaneous%20Images/robinson_chris.jpg">
For the past 15 years Chris has been working with local government, public safety, energy, and utility clients providing a variety of GIS consulting services. From environmental studies in Alaska to crime reporting in San Diego, Chris has worked in many disciplines at various levels within the GIS industry. Prior to joining Eckersall in 2020, Chris has worked for Michael Baker International, Intrado, Resource Data Inc., EagleView/Pictometry, The Omega Group, and Nielsen. &nbsp; &nbsp; 
</br>
</br>

<img align="left" width="150" height="150" src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/Miscellaneous%20Images/luis_estrada_jose.jpg">
During his professional career as a data scientist and engineer, Jose has not only revamped his soft skills, but has also demonstrated competitiveness using his analytical and technical skills in several projects and an internship at LinkedIn. &nbsp; &nbsp;
</br>
</br>
</br>

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
10. [Modeling & Model Evaluation](#modeling_&_model_evaluation)
11. [Conclusion](#conclusion)
12. [References](#references)
13. [License](#license)
14. [Acknowledements](#acknowledgements)
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
  <img src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/Miscellaneous%20Images/project_workflow_diagram.jpeg">
</p>

## Visualizations
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


![](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/EDA%20Images/time_day_stacked_bar.png)

> More serious crimes (35,396) occur in the morning than any other time of day. Evening crimes are generally more serious, but account for less crimes in total than those in the morning or afternoon. More serious night crimes account for only 9,814 (approximately 10%) of all such crimes. However, 60% of crimes occurring at night are more serious and crimes in the afternoon give no preference to severity, occurring at about equal rates.  


## Modeling & Model Evaluation
* Quadratic Discriminant Analysis (QDA)
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost

Determining the model for deployment involves a comprehensive inspection of all area under the receiver operating characteristic (AUROC) curves. As you can see here, we have our introductory QDA model with an auc of 0.54, which is barely above the baseline. Logistic regression makes a 10% improvement to an AUC of 0.64, followed by the Decision Tree that adds another 14% to an AUC of 0.78, and performance keeps improving, especially with these more complex tree-based classifiers, where we now see the best performing model of XGB with an auc of 0.94. However, sensitivity and false alarm rates should also be considered as additional measures of performance assessment.

|     Model                      | **    Accuracy   ** | **    Precision   ** | **    Recall   ** | **    F1-score   ** | **    AUC   ** | **    MSE   ** |
|--------------------------------|:-------------------:|:--------------------:|:-----------------:|:-------------------:|:--------------:|:--------------:|
| **    QDA   **                 |        0.4953       |         0.6071       |       0.1748      |        0.2715       |      0.5216    |      0.5047    |
| **    Decision Tree   **       |        0.6217       |         0.6233       |       0.7499      |        0.6807       |      0.6112    |      0.3783    |
| **    Logistic Regression   ** |        0.6986       |         0.7009       |       0.7668      |        0.7324       |      0.6923    |      0.3021    |
| **    Random Forest   **       |        0.8496       |         0.8376       |       0.8936      |        0.8647       |      0.8460    |      0.1504    |
| **    XGBoost   **             |        0.8885       |         0.8894       |       0.9053      |        0.8972       |      0.8871    |      0.1115    |


![](https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/Modeling%20Images/roc_curves.png)

## Conclusion

During this project, some key considerations came to light regarding safely navigating potentially dangerous areas. Model outcomes alone would likely not be sufficient for ensuring safety with a significant degree of confidence. While historical crime data adds a layer of information, more information may be required to get a complete picture of safety in a particular area. There may be other factors associated with location and crime that contribute to safety. For example, lighting and the presence of other people are not currently considered but could be useful for evaluating safety. To avoid a potentially dangerous main street, an individual may decide to alter their course and travel along an adjacent side street. An argument could be made that the side street may be more dangerous than the main street because of unknown factors. The side street could also have less crime because it is traveled less often. It can be difficult to identify the main factors that contribute to safety because those factors may be different depending on location. Ultimately, there may not be a safe route, and the safest option is to avoid the area altogether. Routing applications, such as the one created for this project, are best suited for planning purposes so that individuals can identify safer pedestrian routes prior to traveling.

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


## License

Copyright (c) 2022, Leonid Shpaner, Christopher Robinson, and Jose Luis Estrada.

All source code and software in this repository are made available under the terms of the MIT license.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgements
Thank you Professor [Dr. Tarshizi](https://github.com/behrang61) for your guidance in facilitating this capstone project. Moreover, thank you to everyone involved as contributors to this repository.