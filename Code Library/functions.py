####################################
## import the requisite libraries ##
####################################

import pandas as pd # import pandas library

def data_types(df):
    # Features' Data Types and Their Respective Null Counts
    dat_type = df.dtypes

    # create a new dataframe to inspect data types
    dat_type = pd.DataFrame(dat_type)

    # sum the number of nulls per column in df
    dat_type['Null_Values'] = df.isnull().sum()

    # reset index w/ inplace = True for more efficient memory usage
    dat_type.reset_index(inplace=True)

    # percentage of null values is produced and cast to new variable
    dat_type['perc_null'] = round(dat_type['Null_Values'] / len(df)*100,0)

    # columns are renamed for a cleaner appearance
    dat_type = dat_type.rename(columns={0:'Data Type',
                                          'index': 'Column/Variable',
                                          'Null_Values': '# of Nulls',
                                          'perc_null': 'Percent Null'})

    return dat_type

####################################
## import the requisite libraries ##
####################################

import pandas as pd # import pandas library

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