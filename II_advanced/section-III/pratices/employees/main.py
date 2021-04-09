import pandas as pd
import numpy as np
import os
import re

def getCurrentDirname():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    return dirname

def normalizeColumns(records):
    columns = []
    for column in records.columns:
        column = column.lower()
        column = column.replace("\'s",'')
        column = column.replace(".",'')
        column = column.replace("%",'')
        column = column.replace(' (years)','')
        column = column.replace('  ','_')
        column = column.replace(' ','_')
        columns.append(column)
    records.columns  = columns
    return records


records = pd.read_csv(getCurrentDirname()+'/records.csv') 
records =  normalizeColumns(records)

employees = records.drop(columns=['user_name','password', 'last_hike'])
users = records[
    ['emp_id',"user_name", "password"]
]

print(records.info())