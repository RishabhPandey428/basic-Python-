# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 07:56:43 2023

@author: Rishu
"""

df = pd.read_csv(r'C:\Users\Rishu\Desktop\new batch 11 spyder\modified ethnic.csv')
import numpy as np
import pandas as pd
df.isna().sum()
from sklearn.impute import SimpleImputer
mean_imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
df["Salaries"] = pd.DataFrame(mean_imputer.fit_transform(df[["Salaries"]]))
df["Salaries"].isna().sum()

df.isna().sum()
mode_imputer = SimpleImputer(missing_values = np.nan, strategy = 'most_frequent')
df["Sex"] = pd.DataFrame(mode_imputer.fit_transform(df[["Sex"]]))
df["MaritalDesc"] = pd.DataFrame(mode_imputer.fit_transform(df[["MaritalDesc"]]))
df.isnull().sum()  # all Sex, MaritalDesc records replaced by mode
#Sweetviz Auto EDA
pip install Sweetviz
import Sweetviz as sv
