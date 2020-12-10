# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:54:23 2020

@author: DELL
"""

import glassdoor_scrapper as gs
import pandas as pd
path="C:/Users/DELL/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',30,False, path, 30)