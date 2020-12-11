# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:09:39 2020

@author: DELL
"""

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
# Company name text only 
# state field
# age of company
# parsing of job description (python,etc)


df = df[df['Salary Estimate']!='-1'] 
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('₹',''))

df['hourly']=df['Salary Estimate'].apply(lambda x:1 if 'per hour' in x.lower() else 0)