# import pandas library
import pandas as pd

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

