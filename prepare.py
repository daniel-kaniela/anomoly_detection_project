#prepare

import pandas as pd
import numpy as np


'''
Following the acquire function
'''
def clean_cohort(df):
    #drop columns
    columns_drop = ['slack', 'updated_at']
    df = df.drop(columns_drop, 1)

    #rename programs webdev or data_science
    conditions = [df.program_id == 1, df.program_id == 2, df.program_id == 3, df.program_id == 4]
    result = ['web_dev','web_dev','data_science','web_dev']
    df['program'] = np.select(conditions, result)

    #drop na - 1 value
    df.dropna(inplace = True)

    # eliminated staff from dataset as focus is students
    df = df[df['name'] != 'Staff']

    #define main path for url
    df['url'] = df['path'].str.split('/').str[0]

    # creating subpath for page hits
    df['subpath'] = df.path.apply(lambda x: x.split('/'))

    return df

def program_split(df):
    ### split between programs
    df_wd = df[df.program == 'web_dev']
    df_ds = df[df.program == 'data_science']

    # # this line eliminates all hits on url that are under 100 values 
    # # exploraiton in scratchpad - leaves 29 values for ds of course material viewed
    # df_ds['url'] = df_ds['url'].value_counts().loc[lambda x : x>100] 
    # # note: some values need to be grouped


    # # same as above for web dev - leaves 23 values
    # df_wd['url'] = df_wd['url'].value_counts().loc[lambda x : x>100]

    return df_wd, df_ds