# MSADS599: Capstone - Identifying Safer Pedestrian Routes in Los Angeles

<p align = "center">
  <img src="https://c.tenor.com/9yaCKAT8LKYAAAAC/crime-scene.gif">
</p>

This is a Capstone project for the University of San Diego's M.S. in Applied Data Science program. 

### Project Status: Complete

### Installation

To use this project, first clone the repo on your device using the commands below:

`git init`

`git clone https://github.com/MSADS-Capstone/navigating_crime.git`

### Partner(s)/Contributor(s)  
**Authors:**  
* [Leonid Shpaner](https://github.com/lshpaner)  
* [Christopher Robinson](https://github.com/ChrisRobinsonUSD)  
* [Jose Luis Estrada](https://github.com/jose-luis-estrada)  

# Table of Contents
1. [Methods](#Methods)
2. [Technologies](#Technologies)
3. [Project Objective](#Project_Objective)


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

This project examines pedestrian safety using machine learning and recent crime data. The goal is to automate a process to identify the safest route between locations, as well as provide additional up to date crime information. This project is looking for the “safest” route, which does not guarantee the route is safe. In some instances, there is no “safe” route. Additionally, where crime is concerned, often factors such as time of day and traits relating to the victim such as age, sex, race, are elements of safety. The solution discussed here not only identifies the safest route but includes elements of situational awareness to assist in making the best decision possible regarding personal safety. When it comes to navigating an area safely, recommendations can be made, but ultimately it is up to the navigator to determine what level of risk is acceptable.

### Data Acquisition and Aggregation

The data was downloaded from the Los Angeles Police Department and preprocessed initially using the ArcGIS ArcPy library. Each crime data point was spatially joined to street segments within fifty feet, producing a one-to-many relationship between streets and crimes. The resulting dataset contained merged street and crime data. The merged dataset was then joined to Los Angeles police districts to extract the district description to validate the LAPD crime data and add the district description to streets which did not have crimes associated with them. Once all three datasets were joined, all records with null street ID values were dropped and the dataset was exported to .csv for exploratory data analysis and further preprocessing.

<p align = "center">
  <img src="https://github.com/MSADS-Capstone/navigating_crime/blob/main/Image%20Folder/EDA%20Images/Project_Workflow.jpeg">
</p>

### Visualization

### Modeling  
* Quadratic Discriminant Analysis (QDA)
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost

### References
Bura, D., Singh, M., \& Nandal, P. (2019). Predicting Secure and Safe Route for Women using Google Maps. 2019 International Conference on Machine Learning, Big Data, Cloud and Parallel Computing (COMITCon). https://doi.org/10.1109/comitcon.2019

Levy, S., Xiong, W., Belding, E., \& Wang, W. Y. (2020). SafeRoute: Learning to Navigate Streets Safely in an Urban Environment. ACM Transactions on Intelligent Systems and Technology, 11(6), 1-17. https://doi.org/10.1145/3402818

Lopez, G., 2022, April 17. A Violent Crisis. The New York Times. https://www.nytimes.com/2022/04/17/briefing /violent-crime-ukraine-war-week-ahead.html

Pavate, A., Chaudhari, A., \& Bansode, R. (2019). Envision of Route Safety Direction Using Machine Learning. Acta Scientific Medical Sciences, 3(11), 140–145. https://doi.org/10.31080/asms.2019.03.0452

Tarkelar, S., Bhat, A., Pandhe, S., \& Halarnkar, T. (2016). Algorithm to Determine the Safest Route. (IJCSIT) International Journal of Computer Science and Information Technologies, 7(3), 2016, 1536-1540. http://ijcsit.com/docs/Volume\%207/vol7issue 3/ijcsit20160703106.pdf

Vandeviver, C. (2014). Applying Google Maps and Google Street View in criminological research. Crime Science, 3(1). https://doi.org/10.1186/s40163-014-0013-2

Wang, Y. Li, Y., Yong S., Rong, X., Zhang, S. (2017). Improvement of ID3 algorithm based on simplified information entropy and coordination degree. 2017 Chinese Automation Congress (CAC), 1526-1530. https://doi.org/10.1109/CAC.2017.8243009