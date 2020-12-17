# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:09:39 2020

@author: DELL
"""

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

# state field
# age of company


df['hourly']=df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)


df['employer_provided']=df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate']!='-1'] 
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('₹',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour',''))

df['min_salary']=min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary']=min_hr.apply(lambda x: int(x.split('-')[1].replace(',','')))

df['avg_salary']= (df.min_salary+df.max_salary)/2


df["Company Name"]=df['Company Name'].str.replace('\d.+', '')

df['job_state']=df['Location'].apply(lambda x: x.split(','))
#age of company
df['age']=df.Founded.apply(lambda x: x if x<1 else 2020-x)
# parsing of job description (python,etc)

#python
df['python']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python.value_counts()
#r studio
df['R']=df['Job Description'].apply(lambda x: 1 if 'r-studio' in x.lower() or 'r.studio' in x.lower() else 0)
df.R.value_counts()
#spark
df['spark']=df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()
#aws
df['aws']=df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()
#excel
df['excel']=df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.columns
df.to_csv('salary_data_cleaned.csv',index = False)
pd.read_csv('salary_data_cleaned.csv')