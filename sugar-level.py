import pandas as pd
from datetime import date
import sys
import os 

import warnings
warnings.filterwarnings("ignore")

def csv_checker():
    file ='sugar_chart.csv'
    isFile = os.path.isfile(file) 
    return isFile

def empty_append(df,date_cur,day_cur):
    f='-'
    b='-'
    l='-'
    d='-'
    i='6+4'
    new_row = {
        'Date' : date_cur,
        'Day'  : day_cur,
        'Fasting': f,
        '2HAB': b,
        '2HAL': l,
        '2HAD': d,
        'Unit': 'mmol/L',
        'Insulin':i,
             }
    df = df.append(new_row,ignore_index=True)
    return df 



def data_replace(first_argument,df):
    if first_argument[0] == 'f':
        df['Fasting'][-1:] = first_argument[1:]
    if first_argument[0] == 'b':
        df['2HAB'][-1:] = first_argument[1:]
    if first_argument[0] == 'l':
        df['2HAL'][-1:] = first_argument[1:]
    if first_argument[0] == 'd':
        df['2HAD'][-1:] = first_argument[1:]
    if first_argument[0] == 'i':
        df['Insulin'][-1:] = first_argument[1:]
    return df    

first_argument = sys.argv[1]
today = date.today()
date_cur = today.strftime("%b-%d-%Y")
day_cur = today.strftime("%A")

if __name__ == "__main__":
    if csv_checker() == True:
        df = pd.read_csv('sugar_chart.csv')
        if df['Date'].iloc[-1] == date_cur :
            df = data_replace(first_argument,df)
            df.to_csv('sugar_chart.csv',index=False,encoding='utf-8')
        else :
            df = data_append(first_argument,df,date_cur,day_cur)
            df = data_replace(first_argument,df)
            df.to_csv('sugar_chart.csv',index=False,encoding='utf-8')
        
    else:
        d = {
        'Date' : date_cur,
        'Day'  : day_cur,
        'Fasting': ['-'],
        '2HAB': ['-'],
        '2HAL': ['-',],
        '2HAD': ['-'],
        'Unit': 'mmol/L',
        'Insulin':['-']
        }
        df = pd.DataFrame(data=d)
        df = data_replace(first_argument,df)
        df.to_csv('sugar_chart.csv',index=False,encoding='utf-8')    
