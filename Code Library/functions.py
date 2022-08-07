####################################
##   Data Types Report Function   ##
####################################

# import the requisite libraries 
import pandas as pd # import pandas library

# Data Types Report
def data_types(df):
    '''
    This function provides a data types report on every column in the dataframe,
    showing column names, column data types, number of nulls, and percentage 
    of nulls, respectively.
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

# Bar Graph For Any Column in the Dataframe
def bar_plot(x, y, df, asc, kind, title, rotation, xlabel, ylabel, column, n):
    '''
    This function allows for the plotting of a bar graph (regular or horizontal)
    of any column in the dataframe 
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
           may have a large number of observations; in these particular cases, 
           it is best to limit the number of observations for analysis.
    '''
    # set figure size
    fig, axes = plt.subplots(figsize=(x,y))
    # sort values in ascending order and generate top n rows
    bar_plot = df[column].value_counts().sort_values(ascending=asc).head(n)  
    bar_plot.plot(kind=kind, width=0.9) # plot horizontal bar graph
    plt.title(title, fontsize=12) # set plot title
    plt.xticks(rotation=rotation) # rotate x-axis labels to 90 degrees
    plt.xlabel(xlabel, fontsize=12) # set plot x-axis label
    plt.ylabel(ylabel, fontsize=12) # set plot y-axis label

# Using a contingency table allows for the data in any column of interest to be
# summarized by the values in the target column (crime severity).
def cont_table(df, col1, lev1, col2, lev2):
    '''
    A function for populating a contingency table is created such that it can be
    used with the variables of interest and the target column. 
    Inputs:
        df: dataframe to ingest for the contingency table
        col1: column of interest from the dataframe; more often than not this 
              is the ground truth (target) column - but this can be replaced
              with any binary outcome column
        col2: column that the dataframe is being grouped by
        lev1: if using ground truth column, these are the less severe crimes
        lev2: if using ground truth column, these are the more severe crimes
    Outputs:
        crime_res_comb.style.format("{:,.0f}"): returns the contingency table
        as a dataframe with values formatted to two decimal places        
    '''
    crime_less = df.loc[df[col1]==lev1].groupby([col2])[[col1]].count()
    crime_less.rename(columns = {col1:lev1}, inplace=True)
    crime_more = df.loc[df[col1]==lev2].groupby([col2])[[col1]].count()
    crime_more.rename(columns={col1:lev2}, inplace=True)
    crime_res_comb = pd.concat([crime_less, crime_more], axis=1)

    # sum row totals
    crime_res_comb['Total']=crime_res_comb.sum(axis=1)
    crime_res_comb.loc['Total']=crime_res_comb.sum(numeric_only=True, axis=0)
    # get % total of each row
    crime_res_comb['% More Serious']=round((crime_res_comb[lev2] / 
    (crime_res_comb[lev2]+crime_res_comb[lev1]))*100, 2)
    crime_res_comb[lev2]=crime_res_comb[lev2].fillna(0)
    crime_res_comb['% More Serious']=crime_res_comb['% More Serious'].fillna(0)
    # crime_res_comb.set_index('new_index_name')

    return crime_res_comb.style.format("{:,.0f}")

# Summary Statistics For Any Column in the Dataframe
def summ_stats(df, var1, var2):
    '''
    A function to provide 5 number summary for any column of interest
    Inputs:
        df: dataframe to ingest for the summary stats table
        var1: column of interest
        var2: numerical column (i.e., 'Vict_Age')
    Output:
        dfsummary: summary statistics report
    '''
    print("\033[1m"+'Summary Statistics by Age'+"\033[1m")
    pd.options.display.float_format = '{:,.2f}'.format
    summ_stats = df.groupby(var1)[var2].agg(['mean', 'median', 'std', 'min', 'max'])
    column_rename = {'mean': 'Mean', 'median': 'Median',
                        'std': 'Standard Deviation',\
                        'min':'Minimum','max': 'Maximum'}
    dfsummary = summ_stats.rename(columns = column_rename)
    return dfsummary

# Stacked Bar Graphs
def stacked_plot (x, y, p, df, col, truth, condition, kind, title1, xlabel1, 
                  ylabel1, width, rot, title2, xlabel2, ylabel2):
    '''
    This function provides a stacked and normalized bar graph of any column of 
    interest, colored by ground truth column
    Inputs:
        x: x-axis figure size
        y: y-axis figure size
        df: dataframe to ingest for the stacked plot
        col: column of interest
        truth: ground truth column
        condition: value from ground truth column
        kind: type of graph
        title1: title of first graph
        xlabel1: x-axis label of first graph
        ylabel1: y-axis label of first graph
        width: width of first graph
        rot: rotation of graph
        title2: title of second graph
        ylabel2: y-axis label of second graph
    '''

    fig, axes = plt.subplots(nrows=2, ncols=1,figsize=(x, y))
    flat = axes.flatten()
    fig.tight_layout(w_pad=5, pad=p, h_pad=5)
    flat = axes.flatten()
    # main title for both plots
    fig.suptitle('Absolute Distributions vs. Normalized Distributions', 
                 fontsize=12)

    # crosstabulation of column of interest and ground truth
    crosstabdest = pd.crosstab(df[col], df[truth]) \
                  .sort_values(by=[condition], ascending=False)

    # normalized crosstabulation 
    crosstabdestnorm = crosstabdest.div(crosstabdest.sum(1), axis = 0)

    # plotting the first stacked bar graph
    plotdest = crosstabdest.plot(kind=kind, stacked=True, title=title1, 
                                 ax=flat[0], 
                                 color=['#00BFC4', '#F8766D'], width=width, 
                                 rot=rot, fontsize=12)
    flat[0].set_xlabel(xlabel1, fontsize=12)
    flat[0].set_ylabel(ylabel1, fontsize=12)
    flat[0].legend(fontsize=12)
    # plotting the second, normalized stacked bar graph
    plotdestnorm = crosstabdestnorm.plot(kind=kind, stacked=True, title=title2,
                                         ylabel='Frequency', 
                                         ax=flat[1], color=['#00BFC4', 
                                                            '#F8766D'], 
                                         width=width, rot=rot, fontsize=12)
    flat[1].set_xlabel(xlabel2, fontsize=12)
    flat[1].set_ylabel(ylabel2, fontsize=12)
    flat[1].legend(fontsize=12)