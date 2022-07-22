####################################
## import the requisite libraries ##
####################################

import pandas as pd

# import plotting library
import matplotlib.pyplot as plt

# function definition for horizontal barplot of any column in this dataframe
def bar_plot(x, y, df, asc, kind, title, rotation, xlabel, ylabel, column, n):
    # sort values in ascending order and generate top n rows
    bar_plot = df[column].value_counts().sort_values(ascending=asc).head(n)  
    bar_plot.plot(kind=kind, width=0.9, figsize=(x,y)) # plot bar graph
    plt.title(title) # set plot title
    plt.xticks(rotation=rotation) # rotate x-axis labels to 90 degrees
    plt.xlabel(xlabel) # set plot x-axis label
    plt.ylabel(ylabel) # set plot y-axis label
plt.show()