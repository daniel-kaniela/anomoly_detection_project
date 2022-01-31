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

    #creates counter column for ip address question
    df['counter'] = 1

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

    #creates lesson column for df_ds and labels materials
    df_ds['lesson'] = np.where(df_ds.path.str.contains('appendix'), 'appendix',
    np.where(df_ds.path.str.contains('search'), 'search',
    np.where(df_ds.path.str.contains('classification'),'classification',
    np.where(df_ds.path.str.contains('sql'), 'sql',
    np.where(df_ds.path.str.contains('fundamentals'), 'fundamentals',
    np.where(df_ds.path.str.contains('regression'), 'regression',
    np.where(df_ds.path.str.contains('python'), 'python',
    np.where(df_ds.path.str.contains('stats'), 'stats', 
    np.where(df_ds.path.str.contains('anomaly'), 'anomaly',
    np.where(df_ds.path.str.contains('clustering'), 'clustering',
    np.where(df_ds.path.str.contains('nlp'), 'nlp',
    np.where(df_ds.path.str.contains('timeseries'), 'time_series',
    np.where(df_ds.path.str.contains('distributed-ml'), 'distributed_ml''',
    np.where(df_ds.path.str.contains('storytelling'), 'storytelling',

    np.where(df_ds.path.str.contains('advanced-topics'), 'advanced-topics',
    np.where(df_ds.path.str.contains('capstones'), 'capstones',
    'pending'))))))))))))))))
    df_ds.lesson.unique()


    # created lesson column with values for web dev lessons
    df_wd['lesson'] = np.where(df_wd.path.str.contains('search'),'search',
    np.where(df_wd.path.str.contains('index'),'index',
    np.where(df_wd.path.str.contains('javascript'),'javascript',
    np.where(df_wd.path.str.contains('toc'),'toc',
    np.where(df_wd.path.str.contains('java'),'java',
    np.where(df_wd.path.str.contains('html|css'),'html-css',
    np.where(df_wd.path.str.contains('spring'),'spring',
    np.where(df_wd.path.str.contains('jquery'),'jquery',
    np.where(df_wd.path.str.contains('mysql'),'mysql',
    np.where(df_wd.path.str.contains('capstone'),'capstone',
    np.where(df_wd.path.str.contains('array|syntax|object_oriented|polymorph|methods|collections|deployment'),'structure',
    np.where(df_wd.path.str.contains('php'),'php',
    np.where(df_wd.path.str.contains('larvel'),'larvel',
            
    'pending')))))))))))))
                                                                                                                                                
    df_wd.lesson.unique()

    ### remove lesson: pending, index, search, capstone

    df_ds = df_ds[(df_ds.lesson!='search') & (df_ds.lesson!='appendix') & (df_ds.lesson!='capstone') & (df_ds.lesson!='pending')]
    df_ds.lesson.unique()
    ### remove lesson: pending, index, search, capstone
    df_webdev = df_wd[(df_wd.lesson!='search') & (df_wd.lesson!='index') & (df_wd.lesson!='capstone') & (df_wd.lesson!='pending')]
    df_wd.lesson.unique()

    # # set datetime & index
    # df_ds.date = pd.to_datetime(df_ds.date)
    # df_ds =df_ds.set_index('date')
    # # set datetime & index
    # df_wd.date = pd.to_datetime(df_wd.date)
    # df_wd =df_wd.set_index('date')


    #returns the two dfs
    return df_wd, df_ds