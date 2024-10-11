# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 08:05:56 2023

@author: Rishu
"""
import pandas as pd
import numpy as num
import seaborn as sns
data = pd.read_csv(r"C:\Users\Rishu\Desktop\new batch 11 spyder\modified ethnic.csv")
df.dtypes
IQR = df['Salaries'].quantile(0.75) - df['Salaries'].quantile(0.25)

lower_limit = df['Salaries'].quantile(0.25) - (IQR * 1.5)
upper_limit = df['Salaries'].quantile(0.75) + (IQR * 1.5)
