####################################
##   Data Types Report Function   ##
####################################

# import the requisite libraries 
import pandas as pd # import pandas library

# function for running a 
def data_types(df):
    '''
    Inputs:
        df: dataframe to run the datatypes report on
    Outputs:
        dat_type: report saved out to a dataframe showing column name, 
                  data type, count of null values in the dataframe, and 
                  percentage of null values in the dataframe
    '''
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
##   Bar Graph Plotting Function  ##
####################################

# import the requisite libraries
import pandas as pd # import pandas library
import matplotlib.pyplot as plt # import plotting library

# function definition for bar graph of any column in this dataframe
def bar_plot(x, y, df, asc, kind, title, rotation, xlabel, ylabel, column, n):
    '''
    Inputs:
    x: passed into figsize as width of the bar graph
    y: passed into figsize as height of the bar graph
    df: dataframe to pass into the function
    asc: ascending order of the data (bool)
    kind: type of barchart (regular or barh for horizontal)
    title: title of the plot
    rotation: rotation of axes labels
    xlabel: x-axis label
    ylabel: y-axis label
    column: column of interest
    n: top number of rows of interest for inspecting the column; some columns
       may have a large number of observations; in these particular cases, it is
       best to limit the number of observations for analysis.
    '''
    # set figure size
    fig, axes = plt.subplots(figsize=(x,y))
    # sort values in ascending order and generate top n rows
    bar_plot = df[column].value_counts().sort_values(ascending=asc).head(n)  
    bar_plot.plot(kind=kind, width=0.9) # plot horizontal bar graph
    plt.title(title) # set plot title
    plt.xticks(rotation=rotation) # rotate x-axis labels to 90 degrees
    plt.xlabel(xlabel) # set plot x-axis label
    plt.ylabel(ylabel) # set plot y-axis label