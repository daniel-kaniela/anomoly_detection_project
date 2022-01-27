import pandas as pd
import numpy as np
import os

from env import host, user, password
########################
def get_db_url(url):
    url = f'mysql+pymysql://{user}:{password}@{host}/{url}'
    return url

########################
def data():
#This function reads the curriculum_log from the codeup sql db into a df writes it to a csv file, and returns the df 
    sql_query = query = '''
    SELECT date, time, path, user_id, cohort_id, program_id, ip, name, slack, start_date, end_date, created_at, updated_at
    FROM logs
    JOIN cohorts on logs.cohort_id = cohorts.id'''
    df = pd.read_sql(sql_query, get_db_url('curriculum_logs'))

    return df

    ########################
def acquire():
    '''
    This function reads in curriculum_logs data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('logs.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('logs.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = data()
        
        # Write DataFrame to a csv file.
        df.to_csv('logs.csv')
        
    return df