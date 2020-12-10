# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:54:23 2020

@author: Pujain
"""

import glassdoor_scrapper as gs
import pandas as pd
path="C:/Users/DELL/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',30,False, path, 15)

df.to_csv('glassdoor_jobs.csv',index=False)